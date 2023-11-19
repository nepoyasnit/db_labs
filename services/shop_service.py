from db_engine.engine import engine, DbEngine
from services.constants import OK_CODE, SHOP_CREATE_SCRIPT_PATH, \
    SHOP_UPDATE_SCRIPT_PATH, SHOP_READ_SCRIPT_PATH, SHOP_DELETE_SCRIPT_PATH


class ShopService:
    engine: DbEngine

    def __init__(self):
        self.engine = engine

    def create(self, name, phone_number, email,
               owner, work_time, category):
        query = self.engine.get_query_result(sql_path=SHOP_CREATE_SCRIPT_PATH,
                                             fields=(name, phone_number, email,
                                                     owner, work_time, category))
        if query:
            return OK_CODE

    def read(self, name):
        query = self.engine.get_query_result(sql_path=SHOP_READ_SCRIPT_PATH,
                                             fields=(name,))
        if query:
            return query

    def update(self, old_name, new_name, phone_number, email, owner,
               work_time, category):
        query = self.engine.get_query_result(sql_path=SHOP_UPDATE_SCRIPT_PATH,
                                             fields=(new_name, phone_number, email,
                                                     owner, work_time, category, old_name))
        if query:
            return OK_CODE
