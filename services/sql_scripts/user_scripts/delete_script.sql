DELETE FROM users
WHERE email = %s
returning TRUE;