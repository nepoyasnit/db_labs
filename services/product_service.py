from db_engine.engine import engine, DbEngine
from services.constants import PRODUCT_CREATE_SCRIPT_PATH, PRODUCT_READ_SCRIPT_PATH, \
    PRODUCT_UPDATE_SCRIPT_PATH, PRODUCT_DELETE_SCRIPT_PATH, SHOP_BY_NAME_SCRIPT_PATH
from services.utils import check_errors


class ProductService:
    engine: DbEngine

    def __init__(self):
        self.engine = engine

    def create(self, shop_name, name, price, promo, producer,
               country, description, category, weight, photo_url):
        shop_id = self.engine.get_query_result(sql_path=SHOP_BY_NAME_SCRIPT_PATH,
                                               fields=(shop_name,))[0][0]
        query = self.engine.get_query_result(sql_path=PRODUCT_CREATE_SCRIPT_PATH,
                                             fields=(shop_id, name, price, promo, producer,
                                                     country, description, category,
                                                     weight, photo_url))
        return check_errors(query)

    def read(self, name):
        query = self.engine.get_query_result(sql_path=PRODUCT_READ_SCRIPT_PATH,
                                             fields=(name,))

        return check_errors(query)

    def update(self, shop_name, old_name, new_name, price, promo, producer,
               country, description, category, weight, photo_url):
        shop_id = self.engine.get_query_result(sql_path=SHOP_BY_NAME_SCRIPT_PATH,
                                               fields=(shop_name,))[0][0]
        query = self.engine.get_query_result(sql_path=PRODUCT_UPDATE_SCRIPT_PATH,
                                             fields=(shop_id, new_name, price, promo, producer,
                                                     country, description, category,
                                                     weight, photo_url, old_name))
        return check_errors(query)

    def delete(self, name):
        query = self.engine.get_query_result(sql_path=PRODUCT_DELETE_SCRIPT_PATH,
                                             fields=(name,))
        return check_errors(query)
