INSERT INTO dish_reviews(rating, description, review_time, dish_id, user_id)
VALUES
(%s, %s, %s, %s, %s)
returning TRUE;