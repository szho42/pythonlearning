import web
import forms
import hashlib
import sqlite3

web.config.debug = False

#render = web.template.render('templates/',globals={'session': session})

db = web.database(dbn='sqlite', db='./db/db1')

urls = (
    '/', 'index',
    '/add', 'add',
    '/login', 'login',
    '/logoff', 'logoff',
    '/ctx', 'ctx',
    '/count', 'count',
    '/reset', 'reset',
    '/setcookie', 'setcookie',
    '/getcookie','getcookie',
)

app = web.application(urls, globals())

#store in disk
session = web.session.Session(app, web.session.DiskStore('sessions'),initializer={'count': 0,'username': 'guest'})

#store in db
#store = web.session.DBStore(db,'sessions')
#session = web.session.Session(app,store,initializer={'count':0})


def notfound():
    return web.notfound("Sorry, not found!")


def internalerror():
    return web.internalerror("Bad, bad server.")

class index:
    def GET(self):
	todos = db.select('todo')
	return render.index(todos)

class add:
    def POST(self):
	data = web.input()
	n = db.insert('todo',title=data.title)
	raise web.seeother('/')

class login:
    def GET(self):
        loginform = forms.loginForm()
	return render.formtest(loginform)
    def POST(self):
        form = forms.loginForm()
	if not form.validates():
            return render.formtest(form)
        else:
	    i = web.input()
	    username = i.username
	    passwd = i.password
            pwdhash = hashlib.md5(passwd).hexdigest()
	    authdb = sqlite3.connect('db/db1')
	    check = authdb.execute('select * from users where username=?\
			    and password=?',(username,pwdhash))
            if check:
                session.loggedin = True
		session.username = username
		raise web.seeother('/')
            else:
                return render.base('Login failed, please try again!')

class logoff:
    def GET(self):
        if session.loggedin:
            session.loggedin = False
	    session.username = 'guest'
	    raise web.seeother('/')
        else:
            raise web.seeother('/')

class ctx:
    def GET(self):
        referer = web.ctx.env.get('HTTP_REFERER', 'http://google.com')
	raise web.seeother(referer)

class count:
    def GET(self):
        session.count += 1
	return str(session.count)

class reset:
    def GET(self):
        session.kill()
	return ""

class setcookie:
    def GET(self):
        web.setcookie('cookie','cookieVal',3600)
	return "Cookie set up..."

class getcookie:
    def GET(self):
        try:
            return "Cookie value: " + web.cookies().cookie 
                                  # or web.cookie().get('cookie')
        except:
            return "Cookie does not exist"

render = web.template.render('templates/',globals={'session': session})

if __name__ == "__main__":
    app.notfound = notfound
    app.internalerror = internalerror
    app.run()


