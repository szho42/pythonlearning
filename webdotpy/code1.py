import web
from web import form

render = web.template.render('templates/')

urls = (
    '/', 'index'
)

app = web.application(urls, globals())

myform = form.Form(
    form.Textbox("boe"),
    form.Textbox("bax",
	form.notnull,
	form.regexp('\d+', 'Must be a digit'),
	form.Validator('Must be more than 5', lambda x: int(x)>5)),
    form.Textarea('moe'),
    form.Checkbox('curly'),
    form.Dropdown('french', ['mustard','fries','wine']))

class index:
    def GET(self):
	form = myform()
	return render.formtest(form)

    def POST(self):
	form = myform()
	if not form.validations():
            return render.formtest(form)
        else:
	    return "Grrreat success! boe: %s, bax: %s" % (form.d.boe, form['bax'].value)

if __name__ == '__main__':
    web.internalerror = web.debugerror
    app.run()

