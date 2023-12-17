UPDATE courier_reviews
SET rating = %s, description = %s, review_time = %s,
    user_id = %s, courier_id = %s
WHERE review_id = %s
returning TRUE;