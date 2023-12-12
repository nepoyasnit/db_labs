DELETE FROM shop_addresses
WHERE address_id = %s
returning TRUE;