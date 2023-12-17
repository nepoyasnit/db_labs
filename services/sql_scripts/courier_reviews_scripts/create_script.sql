INSERT INTO courier_reviews(rating, description, review_time, user_id, courier_id)
VALUES
(%s, %s, %s, %s, %s)
returning TRUE;