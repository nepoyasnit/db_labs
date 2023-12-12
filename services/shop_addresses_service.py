from db_engine.engine import engine, DbEngine
from services.constants import SHOP_ADDRESS_CREATE_PATH, SHOP_ADDRESS_READ_PATH, SHOP_ADDRESS_UPDATE_PATH, \
                            SHOP_ADDRESS_DELETE_PATH
from services.utils import check_errors


class ShopAddressesService:
    engine: DbEngine

    def __init__(self):
        self.engine = engine

    def create(self, address, shop_id):
        query = self.engine.get_query_result(sql_path=SHOP_ADDRESS_CREATE_PATH, fields=(address, shop_id))
        return check_errors(query)

    def read(self, address_id):
        query = self.engine.get_query_result(sql_path=SHOP_ADDRESS_READ_PATH, fields=(address_id,))
        result_code = check_errors(query)
        if result_code:
            return query
        return result_code

    def update(self, address, shop_id, address_id):
        query = self.engine.get_query_result(sql_path=SHOP_ADDRESS_UPDATE_PATH, fields=(address, shop_id, address_id))
        return check_errors(query)

    def delete(self, address_id):
        query = self.engine.get_query_result(sql_path=SHOP_ADDRESS_DELETE_PATH, fields=(address_id,))
        return check_errors(query)
