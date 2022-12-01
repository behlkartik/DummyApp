from blog import db
from blog.models.models import Article

def add_article(article: Article):
    db.session.add(article)
    db.session.commit()