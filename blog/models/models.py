from blog import db
from datetime import datetime, timezone


class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    created_at = db.Column(db.DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

class Article(BaseModel):
    __tablename__ = "article"
    title = db.Column(db.String(30), nullable=False, unique=True)
    author = db.Column(db.String(30), nullable=False, unique=True)
    content = db.Column(db.String(100), nullable=False)

db.create_all()