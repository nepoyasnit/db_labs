UPDATE shop_addresses
SET address = %s, shop_id = %s
WHERE address_id = %s
returning TRUE;