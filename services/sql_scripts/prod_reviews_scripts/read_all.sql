SELECT products.name, product_reviews.rating, product_reviews.description, product_reviews.review_time FROM product_reviews
INNER JOIN products ON product_reviews.product_id = products.product_id;