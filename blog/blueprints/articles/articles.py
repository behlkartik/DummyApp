from blog.models.models import Article
from flask import request, jsonify, Blueprint
from blog.schemas.schemas import ArticleSchema, validate_request
from blog.blueprints.articles import article_util

blueprint = Blueprint('articles', __name__, url_prefix='/articles')

article_schema = ArticleSchema()
article_all_schema = ArticleSchema(many=True)

@blueprint.route("/", methods=["GET"])
def get_all_articles():
    articles = Article.query.all()
    return jsonify(article_all_schema.dump(articles)), 200

@blueprint.route("/", methods=["POST"])
@validate_request(article_schema)
def add_article():
    content_type = request.headers.get("Content-Type")
    if content_type == "application/json":
        article = Article(**request.json)
        article_util.add_article(article)
        return article_schema.dump(article), 201
    else:
        return "Incorrect Content-type sent (required json)", 400


@blueprint.route("/<int:article_id>")
def article_by_id(article_id):
    article = Article.query.filter_by(id=article_id).first()
    return article_schema.dump(article), 200

