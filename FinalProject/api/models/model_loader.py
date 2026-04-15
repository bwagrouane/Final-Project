from . import orders, order_details, recipes, sandwiches, resources

from ..dependencies.database import engine


def index():
    menu.Base.metadata.create_all(engine)
    orders.Base.metadata.create_all(engine)
    promotions.Base.metadata.create_all(engine)
    reviews.Base.metadata.create_all(engine)
    resources.Base.metadata.create_all(engine)
