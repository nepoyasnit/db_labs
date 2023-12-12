from db_engine.engine import engine, DbEngine
from services.constants import ORDER_CREATE_SCRIPT_PATH, ORDER_READ_SCRIPT_PATH, ORDER_UPDATE_SCRIPT_PATH, \
                            ORDER_DELETE_SCRIPT_PATH, OK_CODE, ERROR_CODE


class OrderService:
    engine: DbEngine

    def __init__(self):
        self.engine = engine

    def create(self, is_active, order_time, user_id, courier_id):
        query = self.engine.get_query_result(sql_path=ORDER_CREATE_SCRIPT_PATH, fields=(is_active, order_time,
                                                                                        user_id, courier_id))
        if query:
            return OK_CODE
        else:
            return ERROR_CODE

    def read(self, order_id):
        query = self.engine.get_query_result(sql_path=ORDER_READ_SCRIPT_PATH, fields=(order_id,))

        if query:
            return query
        else:
            return ERROR_CODE

    def update(self, is_active, order_time, user_id, courier_id, order_id):
        query = self.engine.get_query_result(sql_path=ORDER_UPDATE_SCRIPT_PATH, fields=(is_active, order_time,
                                                                                        user_id, courier_id, order_id))

        if query:
            return OK_CODE
        else:
            return ERROR_CODE

    def delete(self, order_id):
        query = self.engine.get_query_result(sql_path=ORDER_DELETE_SCRIPT_PATH, fields=(order_id,))

        if query:
            return OK_CODE
        else:
            return OK_CODE
