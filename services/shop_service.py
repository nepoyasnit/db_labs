from services.constants import OK_CODE, SHOP_CREATE_SCRIPT_PATH
from db_engine.engine import engine, DbEngine


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
