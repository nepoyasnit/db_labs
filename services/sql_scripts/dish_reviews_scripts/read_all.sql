SELECT dishes.name, dish_reviews.rating, dish_reviews.description, dish_reviews.review_time FROM dish_reviews
INNER JOIN dishes ON dish_reviews.dish_id = dishes.dish_id;