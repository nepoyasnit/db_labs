DELETE FROM products
WHERE product_id = %s
returning TRUE;