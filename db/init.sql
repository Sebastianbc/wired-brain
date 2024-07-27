create database if not exists products

use products

create table if not exists products (
    id integer auto_increment primary key,
    name varchar(128) not null
) engine=INNODB