from db_engine.engine import engine, DbEngine
from services.constants import (COURIER_REVIEWS_CREATE_PATH, COURIER_REVIEWS_READ_PATH, COURIER_REVIEWS_UPDATE_PATH,
                                COURIER_REVIEWS_DELETE_PATH)
from constants import OK_CODE
from services.utils import check_errors


class CourierReviewsService:
    engine: DbEngine

    def __init__(self):
        self.engine = engine

    def create(self, rating, description, review_time, user_id, courier_id):
        query = self.engine.get_query_result(sql_path=COURIER_REVIEWS_CREATE_PATH, fields=(rating, description,
                                                                                           review_time, user_id,
                                                                                           courier_id))
        return check_errors(query)

    def read(self, review_id):
        query = self.engine.get_query_result(sql_path=COURIER_REVIEWS_READ_PATH, fields=(review_id,))

        result = check_errors(query)
        if result == OK_CODE:
            return query
        return result

    def update(self, review_id, rating, description, review_time, user_id, courier_id):
        query = self.engine.get_query_result(sql_path=COURIER_REVIEWS_UPDATE_PATH, fields=(rating, description,
                                                                                           review_time, user_id,
                                                                                           courier_id, review_id))
        return check_errors(query)

    def delete(self, review_id):
        query = self.engine.get_query_result(sql_path=COURIER_REVIEWS_DELETE_PATH, fields=(review_id,))

        return check_errors(query)
