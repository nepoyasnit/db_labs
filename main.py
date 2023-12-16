import datetime
from services.dish_reviews_service import DishReviewsService

# print(DishReviewsService().create(rating=4.9, description='test', review_time=datetime.datetime.utcnow(), dish_id=1, user_id=2))

# print(DishReviewsService().read(3))

# print(DishReviewsService().update(review_id=3, rating=4.3, description='test1', review_time=datetime.datetime.now(), dish_id=1, user_id=2))

print(DishReviewsService().delete(3))
