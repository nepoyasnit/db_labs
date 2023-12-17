DELETE FROM product_reviews
WHERE review_id = %s
returning TRUE;