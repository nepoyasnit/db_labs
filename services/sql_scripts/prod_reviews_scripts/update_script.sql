UPDATE product_reviews
SET rating = %s, description = %s, review_time = %s,
    product_id = %s, user_id = %s
WHERE review_id = %s
returning TRUE;