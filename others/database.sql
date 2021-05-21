CREATE TABLE info (
id SERIAL PRIMARY KEY,
create_date timestamp without time zone,
write_date timestamp without time zone,
sequence varchar(255) NOT NULL,
passkey varchar(255) NOT NULL,
url varchar(255) NOT NULL,
title varchar(255) NOT NULL,
description text NOT NULL,
preview text NOT NULL,
content text NOT NULL
);