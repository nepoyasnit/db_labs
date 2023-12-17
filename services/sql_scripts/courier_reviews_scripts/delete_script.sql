DELETE FROM courier_reviews
WHERE review_id = %s
returning TRUE;