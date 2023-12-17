SELECT dishes.name, dishes.price, dishes_orders.order_id FROM dishes_orders
INNER JOIN dishes ON dishes_orders.dish_id = dishes.dish_id;