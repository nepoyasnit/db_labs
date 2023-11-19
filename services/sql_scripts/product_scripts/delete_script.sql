DELETE FROM products
WHERE name = %s
returning TRUE;