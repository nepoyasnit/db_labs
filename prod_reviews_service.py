from db_engine.engine import engine, DbEngine
from services.constants import (DISH_REVIEWS_CREATE_PATH, DISH_REVIEWS_READ_PATH, DISH_REVIEWS_UPDATE_PATH,
                                DISH_REVIEWS_DELETE_PATH, OK_CODE)
from services.utils import check_errors


class DishReviewsService:
    engine: DbEngine

    def __init__(self):
        self.engine = engine

    def create(self, rating, description, review_time, dish_id, user_id):
        query = self.engine.get_query_result(sql_path=DISH_REVIEWS_CREATE_PATH, fields=(rating, description,
                                                                                        review_time, dish_id, user_id))
        return check_errors(query)

    def read(self, review_id):
        query = self.engine.get_query_result(sql_path=DISH_REVIEWS_READ_PATH, fields=(review_id,))

        if check_errors(query) == OK_CODE:
            return query

    def update(self, review_id, rating, description, review_time, dish_id, user_id):
        query = self.engine.get_query_result(sql_path=DISH_REVIEWS_UPDATE_PATH, fields=(rating, description,
                                                                                        review_time, dish_id, user_id,
                                                                                        review_id))
        return check_errors(query)

    def delete(self, review_id):
        query = self.engine.get_query_result(sql_path=DISH_REVIEWS_DELETE_PATH, fields=(review_id,))

        return check_errors(query)


