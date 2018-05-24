from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('gacha.config')
db = SQLAlchemy(app)

import gacha.views
