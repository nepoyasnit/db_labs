from db_engine.engine import engine, DbEngine
from services.constants import RESTAURANT_CREATE_SCRIPT_PATH, RESTAURANT_READ_SCRIPT_PATH, \
    RESTAURANT_UPDATE_SCRIPT_PATH, RESTAURANT_DELETE_SCRIPT_PATH
from constants import OK_CODE
from services.utils import check_errors


class RestaurantService:
    engine: DbEngine

    def __init__(self):
        self.engine = engine

    def create(self, name, phone_number, email, owner, stars,
               price, category, work_time):
        query = self.engine.get_query_result(sql_path=RESTAURANT_CREATE_SCRIPT_PATH,
                                             fields=(name, phone_number, email, owner, stars,
                                                     price, category, work_time))
        return check_errors(query)

    def read(self, restaurant_id):
        query = self.engine.get_query_result(sql_path=RESTAURANT_READ_SCRIPT_PATH,
                                             fields=(restaurant_id,))
        result_code = check_errors(query)
        if result_code == OK_CODE:
            return query
        return result_code

    def update(self, name, phone_number, email, owner, stars,
               price, category, work_time, restaurant_id):
        query = self.engine.get_query_result(sql_path=RESTAURANT_UPDATE_SCRIPT_PATH,
                                             fields=(name, phone_number, email, owner, stars,
                                                     price, category, work_time, restaurant_id))
        return check_errors(query)

    def delete(self, restaurant_id):
        query = self.engine.get_query_result(sql_path=RESTAURANT_DELETE_SCRIPT_PATH,
                                             fields=(restaurant_id,))
        return check_errors(query)
