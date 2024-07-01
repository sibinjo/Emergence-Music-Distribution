from flask import Flask
import os
from public import public
from admin import admin
app=Flask(__name__)
app.secret_key="emg"
app.register_blueprint(admin,url_prefix='/admin')
app.register_blueprint(public)
app.run(debug=True,port=5039)
FILES_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'files')