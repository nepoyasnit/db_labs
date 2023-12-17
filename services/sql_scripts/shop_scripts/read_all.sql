SELECT shops.*, shop_addresses.address FROM shops
INNER JOIN shop_addresses ON shops.shop_id = shop_addresses.shop_id;