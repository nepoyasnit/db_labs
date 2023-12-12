UPDATE restaraunt_addresses
SET address = %s, restaraunt_id = %s
WHERE address_id = %s
returning TRUE;