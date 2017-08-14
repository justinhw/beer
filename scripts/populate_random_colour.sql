create or replace function populate_random()
returns bigint as $row_complete$
declare
	counter bigint := 1;
	total bigint;
begin
	select count(*) into total from public.beers;
	while counter < total LOOP
		update public.beers
			set colour = trunc(random()*6)
			where public.beers.id = counter;
		counter:= counter + 1;
	end LOOP;
	return counter;
end; $row_complete$ language plpgsql;

select populate_random();