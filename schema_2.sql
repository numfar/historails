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