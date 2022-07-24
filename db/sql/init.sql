create schema postgres_test;

set search_path to postgres_test;

create table users (
    id text primary key,
    name text not null,
    bio text not null
);

insert into users(id, name, bio) values
    ('AAA', 'AAA AA', 'Hi, Im AAA.\nI like apple.'),
    ('BBB', 'BBB BB', 'Hello world!'),
    ('CCC', 'CCC CC', '<a>This is a link</a>');
