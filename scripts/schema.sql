create table categories (
  id serial not null primary key,
  category_name text unique not null,
  last_updated timestamp(0) default now() not null
);

create table styles (
  id serial not null primary key,
  category_id int default null references categories(id),
  style_name text not null,
  last_updated timestamp(0) default now() not null
);

create table breweries (
  id serial not null primary key,
  name text not null,
  address text,
  city text,
  state text,
  country text,
  code text,
  phone text,
  website text,
  description text,
  last_updated timestamp(0) default now() not null
);

create table beers (
  id serial not null primary key,
  brewery_id int references breweries(id) on update cascade on delete cascade,
  name text not null,
  category_id int default null references categories(id) on update cascade on delete cascade,
  style_id int default null references styles(id) on update cascade on delete cascade,
  abv numeric default null,
  description text,
  last_updated timestamp(0) default now() not null
);

create table geocodes (
  id serial not null primary key,
  brewery_id int references breweries(id) on update cascade on delete cascade,
  latitude numeric,
  longitude numeric,
  accuracy text check (accuracy in ('APPROXIMATE', 'GEOMETRIC_CENTER', 'RANGE_INTERPOLATED', 'ROOFTOP'))
)
