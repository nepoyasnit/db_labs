DELETE FROM restaraunt_addresses
WHERE address_id = %s
returning TRUE;