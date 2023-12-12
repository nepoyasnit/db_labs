INSERT INTO shop_addresses(address, shop_id)
VALUES(%s, %s)
returning TRUE;