from db_engine.engine import engine, DbEngine
from services.constants import PRODUCT_CREATE_SCRIPT_PATH, PRODUCT_READ_SCRIPT_PATH, \
    PRODUCT_UPDATE_SCRIPT_PATH, PRODUCT_DELETE_SCRIPT_PATH, PRODUCT_ALL_PATH
from constants import OK_CODE
from services.utils import check_errors


class ProductService:
    engine: DbEngine

    def __init__(self):
        self.engine = engine

    def create(self, shop_id, name, price, promo, producer,
               country, description, category, weight, photo_url):
        query = self.engine.get_query_result(sql_path=PRODUCT_CREATE_SCRIPT_PATH,
                                             fields=(shop_id, name, price, promo, producer,
                                                     country, description, category,
                                                     weight, photo_url))
        return check_errors(query)

    def read(self, shop_name):
        query = self.engine.get_query_result(sql_path=PRODUCT_READ_SCRIPT_PATH,
                                             fields=(shop_name,))
        result = check_errors(query)
        if result == OK_CODE:
            return query
        return result

    def read_all(self, shop_name):
        query = self.engine.get_query_result(sql_path=PRODUCT_ALL_PATH, fields=(shop_name,))

        result = check_errors(query)
        if result == OK_CODE:
            return query
        return result

    def update(self, shop_id, name, price, promo, producer,
               country, description, category, weight, photo_url, product_id):
        query = self.engine.get_query_result(sql_path=PRODUCT_UPDATE_SCRIPT_PATH,
                                             fields=(shop_id, name, price, promo, producer,
                                                     country, description, category,
                                                     weight, photo_url, product_id))
        return check_errors(query)

    def delete(self, product_id):
        query = self.engine.get_query_result(sql_path=PRODUCT_DELETE_SCRIPT_PATH,
                                             fields=(product_id,))
        return check_errors(query)
