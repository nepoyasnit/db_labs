from db_engine.engine import engine, DbEngine
from services.constants import DISH_CREATE_SCRIPT_PATH, DISH_READ_SCRIPT_PATH, \
    DISH_UPDATE_SCRIPT_PATH, DISH_DELETE_SCRIPT_PATH, RESTARAUNT_BY_NAME_SCRIPT_PATH, OK_CODE


class DishService:
    engine: DbEngine

    def __init__(self):
        self.engine = engine

    def create(self, restaurant_name, name, price, promo,
               description, category, weight, photo_url):
        restaurant_id = self.engine.get_query_result(sql_path=RESTARAUNT_BY_NAME_SCRIPT_PATH,
                                                     fields=(restaurant_name,))[0][0]
        query = self.engine.get_query_result(sql_path=DISH_CREATE_SCRIPT_PATH,
                                             fields=(restaurant_id, name, price, promo,
                                                     description, category, weight, photo_url))
        if query:
            return OK_CODE
