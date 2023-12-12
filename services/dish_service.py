from db_engine.engine import engine, DbEngine
from services.constants import DISH_CREATE_SCRIPT_PATH, DISH_READ_SCRIPT_PATH, \
    DISH_UPDATE_SCRIPT_PATH, DISH_DELETE_SCRIPT_PATH, RESTAURANT_BY_NAME_SCRIPT_PATH, OK_CODE, ERROR_CODE


class DishService:
    engine: DbEngine

    def __init__(self):
        self.engine = engine

    def create(self, restaurant_name, name, price, promo,
               description, category, weight, photo_url):
        restaurant_id = self.engine.get_query_result(sql_path=RESTAURANT_BY_NAME_SCRIPT_PATH,
                                                     fields=(restaurant_name,))[0][0]
        query = self.engine.get_query_result(sql_path=DISH_CREATE_SCRIPT_PATH,
                                             fields=(restaurant_id, name, price, promo,
                                                     description, category, weight, photo_url))
        if query:
            return OK_CODE
        else:
            return ERROR_CODE

    def read(self, name):
        query = self.engine.get_query_result(sql_path=DISH_READ_SCRIPT_PATH,
                                             fields=(name,))
        if query:
            return query
        else:
            return ERROR_CODE

    def update(self, restaurant_name, old_name, new_name, price, promo,
               description, category, weight, photo_url):
        restaurant_id = self.engine.get_query_result(sql_path=RESTAURANT_BY_NAME_SCRIPT_PATH,
                                                     fields=(restaurant_name,))[0][0]
        query = self.engine.get_query_result(sql_path=DISH_UPDATE_SCRIPT_PATH,
                                             fields=(restaurant_id, new_name, price,
                                                     promo, description, category,
                                                     weight, photo_url, old_name))
        if query:
            return OK_CODE
        else:
            return ERROR_CODE

    def delete(self, name):
        query = self.engine.get_query_result(sql_path=DISH_DELETE_SCRIPT_PATH,
                                             fields=(name,))
        if query:
            return OK_CODE
        else:
            return ERROR_CODE
