drop table if exists connections;
drop table if exists route;
drop table if exists stop;

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

insert into stop (id,stop_name,longitude,latitude) values (1,'Stopy1',23.4,33.0);
insert into stop (id,stop_name,longitude,latitude) values (2,'Stopy2',11.4,3.0);
insert into route (id,route_name) values (1,'Route1');
insert into connections (node1,node2,route) values (1,2,1); 