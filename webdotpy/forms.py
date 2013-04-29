from web import form

loginForm = form.Form(
		form.Textbox('username',
			form.notnull),
		form.Password('password',
			form.notnull,
			form.Validator('Must be more than 5', 
				lambda x:int(x)>5)),
		form.Checkbox('Remember username'),
		form.Dropdown('Membership',['Advanced','intermediate','new']),
		form.Button('Login'),
            )

