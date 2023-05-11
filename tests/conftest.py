from pytest_factoryboy import register

from tests.factories import AuthorFactory, CategoryFactory, AdFactory

pytest_plugins = "tests.fixtures"

register(AuthorFactory)
register(CategoryFactory)
register(AdFactory)
# register(SelectionFactory)
