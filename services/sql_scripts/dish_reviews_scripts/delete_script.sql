DELETE FROM dish_reviews
WHERE review_id = %s
returning TRUE;