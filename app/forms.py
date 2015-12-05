from flask.ext.wtf import Form
from wtfforms import StringField, BooleanField
from wtffroms.validators import DataRequired


class LoginForm(Form):
    openid = StringField('openid', validators = [DataRequired()])
    remember_me = BooleanField('remember_me', default=False)
