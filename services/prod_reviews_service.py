from db_engine.engine import engine, DbEngine
from services.constants import (PRODUCT_REVIEWS_CREATE_PATH, PRODUCT_REVIEWS_READ_PATH, PRODUCT_REVIEWS_UPDATE_PATH,
                                PRODUCT_REVIEWS_DELETE_PATH, PRODUCT_REVIEWS_ALL_PATH)
from constants import OK_CODE
from services.utils import check_errors


class ProductReviewsService:
    engine: DbEngine

    def __init__(self):
        self.engine = engine

    def create(self, rating, description, review_time, product_id, user_id):
        query = self.engine.get_query_result(sql_path=PRODUCT_REVIEWS_CREATE_PATH, fields=(rating, description,
                                                                                           review_time, product_id,
                                                                                           user_id))
        return check_errors(query)

    def read(self, review_id):
        query = self.engine.get_query_result(sql_path=PRODUCT_REVIEWS_READ_PATH, fields=(review_id,))

        result = check_errors(query)
        if result == OK_CODE:
            return query
        return result

    def read_all(self):
        query = self.engine.get_query_result(sql_path=PRODUCT_REVIEWS_ALL_PATH, fields=None)

        result_code = check_errors(query)
        if result_code == OK_CODE:
            return query
        return result_code

    def update(self, review_id, rating, description, review_time, product_id, user_id):
        query = self.engine.get_query_result(sql_path=PRODUCT_REVIEWS_UPDATE_PATH, fields=(rating, description,
                                                                                           review_time, product_id,
                                                                                           user_id, review_id))
        return check_errors(query)

    def delete(self, review_id):
        query = self.engine.get_query_result(sql_path=PRODUCT_REVIEWS_DELETE_PATH, fields=(review_id,))

        return check_errors(query)


