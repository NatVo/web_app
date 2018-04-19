sudo -u postgres psql

create user admin with password 'password';
create database users_info;
grant all privileges on database users_info to admin;

\c users_info

CREATE EXTENSION pgcrypto;

\q

psql -h localhost users_info admin
