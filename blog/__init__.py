from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import database_exists, create_database
from uuid import uuid4
from flask_marshmallow import Marshmallow, fields

app = Flask(__name__)
app.app_context().push()
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@my_mysql_db:3306/blog"
app.config["SECRET_KEY"] = uuid4().hex

db = SQLAlchemy(app)

from blog.blueprints.articles.articles import blueprint as article_blueprint
from blog.blueprints.videos.videos import blueprint as video_blueprint
app.register_blueprint(article_blueprint)
app.register_blueprint(video_blueprint)