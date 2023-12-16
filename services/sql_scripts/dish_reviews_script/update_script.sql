UPDATE dish_reviews
SET rating = %s, description = %s, review_time = %s,
    dish_id = %s, user_id = %s
WHERE review_id = %s
returning TRUE;