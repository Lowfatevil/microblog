from flask import Flask

app = Flask(__name__)
app.config.from_object('object')

from app import views
