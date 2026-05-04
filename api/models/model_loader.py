from . import orders, order_details, recipes, reviews, resources, items

from ..dependencies.database import engine


def index():
    orders.Base.metadata.create_all(engine)
    order_details.Base.metadata.create_all(engine)
    recipes.Base.metadata.create_all(engine)
    reviews.Base.metadata.create_all(engine)
    resources.Base.metadata.create_all(engine)
    items.Base.metadata.create_all(engine)
