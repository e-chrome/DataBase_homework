--1
select name, count(performer_id) from genre
    join genre_performer
    on genre.id = genre_performer.genre_id
    group by name;
    
--2
select count(*) from track
    join album
    on track.album_id = album.id
    where album.year_of_issue between 2019 and 2020;
    
--3
select a.name, avg(t.duration) from album a
    join track t 
    on a.id = t.album_id
    group by a.name;
    
--4
select p.alias, a.name as album_name, a.year_of_issue from
    (select performer.alias, performer_album.album_id from performer
        join performer_album
        on performer.id = performer_album.performer_id) as p
    join album a
    on p.album_id = a.id
    where a.year_of_issue <> 2020;
  
--5
select col.collection_name, per.alias from
    (select ca.collection_name, t.album_id from
        (select c.name as collection_name, ct.track_id from collection c
            join collection_track ct 
            on c.id = ct.collection_id) as ca
        join track t
        on ca.track_id = t.id) as col
    join
        (select p.alias, pa.album_id from performer p
            join performer_album pa 
            on p.id = pa.performer_id) as per
    on col.album_id = per.album_id
    where per.alias = 'Êמבחמם';
   
--6
select album.name from album
    join
	(select pa.album_id from performer_album pa 
	    join
	    (select perf.id as perf_id from
	        (select p.alias, p.id, gp.genre_id from performer p 
	            join genre_performer gp 
	            on p.id = gp.performer_id) as perf
	        group by perf.id
	        having count(perf.genre_id) > 1) as p_id
	    on pa.performer_id = p_id.perf_id) as a_id
	on album.id = a_id.album_id;
   
--7
select name from track t
    left join collection_track ct
    on t.id = ct.track_id
    where ct.track_id is null;
   
--8
select alias from performer
    join
	(select performer_id from performer_album as pa
	    join
		(select album_id from track
		    where duration = (select min(duration) from track)) as a_id
		on pa.album_id = a_id.album_id) as p_id
    on performer.id = p_id.performer_id;
   
--9
select a.name from album a
    join
	(select album_id from
	    (select album_id, count(id) as track_count from track
		    group by album_id) as t
	    where track_count =
			(select min(track_count) from 
		        (select album_id, count(id) as track_count from track
		        group by album_id) as t)) as a_id
    on a.id = a_id.album_id;
		


       