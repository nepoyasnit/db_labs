SELECT dishes.name, dishes.price FROM dishes_orders
INNER JOIN dishes ON dishes_orders.dish_id = dishes.dish_id
WHERE order_id = %s;