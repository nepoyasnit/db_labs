SELECT EXISTS (
    SELECT 1
    FROM users
    WHERE email = %s AND password = %s
);