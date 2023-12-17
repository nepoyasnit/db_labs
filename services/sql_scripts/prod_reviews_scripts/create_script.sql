INSERT INTO product_reviews(rating, description, review_time, product_id, user_id)
VALUES
(%s, %s, %s, %s, %s)
returning TRUE;