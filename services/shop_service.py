from db_engine.engine import engine, DbEngine
from services.constants import SHOP_CREATE_SCRIPT_PATH, SHOP_UPDATE_SCRIPT_PATH, \
    SHOP_READ_SCRIPT_PATH, SHOP_DELETE_SCRIPT_PATH
from services.utils import check_errors


class ShopService:
    engine: DbEngine

    def __init__(self):
        self.engine = engine

    def create(self, name, phone_number, email,
               owner, work_time, category):
        query = self.engine.get_query_result(sql_path=SHOP_CREATE_SCRIPT_PATH,
                                             fields=(name, phone_number, email,
                                                     owner, work_time, category))
        return check_errors(query)

    def read(self, name):
        query = self.engine.get_query_result(sql_path=SHOP_READ_SCRIPT_PATH,
                                             fields=(name,))
        return check_errors(query)

    def update(self, old_name, new_name, phone_number, email, owner,
               work_time, category):
        query = self.engine.get_query_result(sql_path=SHOP_UPDATE_SCRIPT_PATH,
                                             fields=(new_name, phone_number, email,
                                                     owner, work_time, category, old_name))
        return check_errors(query)

    def delete(self, name):
        query = self.engine.get_query_result(sql_path=SHOP_DELETE_SCRIPT_PATH,
                                             fields=(name,))
        return check_errors(query)
