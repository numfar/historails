-- Initialize the database.
-- Drop any existing data and create empty tables.

DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;
drop table if exists connections;
drop table if exists route;
drop table if exists stop;


CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE post (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  author_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  FOREIGN KEY (author_id) REFERENCES user (id)
);

create table stop (
[id] integer primary key autoincrement not null,
[stop_name] text,
[longitude] numeric,
[latitude] numeric);

create table route (
[id] integer primary key autoincrement not null,
[route_name] text);

create table connections (
[node1] integer not null,
[node2] integer not null,
[route] integer not null,
foreign key ([node1]) references "stop" ([id]),
foreign key ([node2]) references "stop" ([id]),
foreign key ([route]) references "route" ([id])
);
