-- Initialize the database.
-- Drop any existing data and create empty tables.

DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;
drop table if exists connection;
drop table if exists route;
drop table if exists stop;


CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

create table stop (
[id] integer primary key autoincrement not null,
[stop_name] text,
[stop_type] numeric,
[description] text,
[start_year] text,
[longitude] numeric,
[latitude] numeric);

create table route (
[id] integer primary key autoincrement not null,
[route_name] text);

create table connection (
[node1] integer not null,
[node2] integer not null,
[route] integer not null,
foreign key ([node1]) references "stop" ([id]),
foreign key ([node2]) references "stop" ([id]),
foreign key ([route]) references "route" ([id])
);

insert into stop (stop_name,stop_type,description,start_year,latitude,longitude) values ('Kärrgruvan',1,'Kärrgruvan utanför Norberg','1856-06-29',15.9365462,60.0913360);
insert into stop (stop_name,stop_type,description,start_year,latitude,longitude) values ('Ängelsberg station',1,'Ängelsberg station','1856-06-29',16.0098471, 59.9585172);
insert into route (route_name) values ('Rutt1');
insert into connection (node1,node2,route) values (1,2,1);

insert into stop (stop_name,stop_type,description,start_year,latitude,longitude) values ('Södertälje station',1,'Start på Stockholms järnväg','1860-01-01',17.6271663,59.1964289);
insert into stop (stop_name,stop_type,description,start_year,latitude,longitude) values ('Stockholm centralstation',1,'Stockholm C','1860-01-01',18.0710935,59.3251172);
insert into route (route_name) values ('Rutt2');
insert into connection (node1,node2,route) values (3,4,2);

insert into stop (stop_name,stop_type,description,start_year,latitude,longitude) values ('Göteborg C',1,'Västra stambanan','1862-01-01',11.9670171,57.7072326);
insert into stop (stop_name,stop_type,description,start_year,latitude,longitude) values ('Malmö Station',1,'Södra stambanan','1864-01-01',13.0001566, 55.6052931);
insert into route (route_name) values ('Rutt3');
insert into connection (node1,node2,route) values (5,6,3);

insert into stop (stop_name,stop_type,description,start_year,latitude,longitude) values ('Nora station',1,'Norra station i Danderyd','1856-06-05',18.0198648, 59.4130938);
insert into stop (stop_name,stop_type,description,start_year,latitude,longitude) values ('Örebro station',1,'Välkommen till Örebro','1856-06-05',15.2149988, 59.2747378);
insert into route (route_name) values ('Rutt4');
insert into connection (node1,node2,route) values (7,8,4);
