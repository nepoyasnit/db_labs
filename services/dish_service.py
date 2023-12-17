from db_engine.engine import engine, DbEngine
from services.constants import DISH_CREATE_SCRIPT_PATH, DISH_READ_SCRIPT_PATH, \
    DISH_UPDATE_SCRIPT_PATH, DISH_DELETE_SCRIPT_PATH, DISH_ALL_PATH
from services.utils import check_errors
from constants import OK_CODE


class DishService:
    engine: DbEngine

    def __init__(self):
        self.engine = engine

    def create(self, restaurant_id, name, price, promo,
               description, category, weight, photo_url):
        query = self.engine.get_query_result(sql_path=DISH_CREATE_SCRIPT_PATH,
                                             fields=(restaurant_id, name, price, promo,
                                                     description, category, weight, photo_url))
        return check_errors(query)

    def read(self, dish_name):
        query = self.engine.get_query_result(sql_path=DISH_READ_SCRIPT_PATH,
                                             fields=(dish_name,))
        result = check_errors(query)
        if result == OK_CODE:
            return query
        return result

    def read_all(self, restaurant_name):
        query = self.engine.get_query_result(sql_path=DISH_ALL_PATH, fields=(restaurant_name,))

        result_code = check_errors(query)
        if result_code == OK_CODE:
            return query
        return result_code

    def update(self, restaurant_id, new_name, price, promo,
               description, category, weight, photo_url, dish_id):
        query = self.engine.get_query_result(sql_path=DISH_UPDATE_SCRIPT_PATH,
                                             fields=(restaurant_id, new_name, price,
                                                     promo, description, category,
                                                     weight, photo_url, dish_id))
        return check_errors(query)

    def delete(self, dish_id):
        query = self.engine.get_query_result(sql_path=DISH_DELETE_SCRIPT_PATH,
                                             fields=(dish_id,))
        return check_errors(query)
