from . import orders, order_details, recipes, sandwiches, resources

from ..dependencies.database import engine
from . import orders, order_details, recipes, sandwiches, resources


def index():
    orders.Base.metadata.create_all(engine)
    order_details.Base.metadata.create_all(engine)
    recipes.Base.metadata.create_all(engine)
    sandwiches.Base.metadata.create_all(engine)
    resources.Base.metadata.create_all(engine)
    reviews.Base.metadata.create_all(engine)
