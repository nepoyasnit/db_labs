SELECT users.name AS courier_name, courier_reviews.rating, courier_reviews.description, courier_reviews.review_time FROM courier_reviews
INNER JOIN users ON courier_reviews.courier_id = users.user_id;