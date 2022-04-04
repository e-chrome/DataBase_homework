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
select performer.alias from performer
    join performer_album on performer.id = performer_album.performer_id 
    join album on album.id = performer_album.album_id
    where performer.alias not in
        (select performer.alias from performer
	        join performer_album on performer.id = performer_album.performer_id 
	        join album on album.id = performer_album.album_id
	        where album.year_of_issue = 2020); 
     
--5
select collection.name from collection 
    join collection_track on collection.id = collection_track.collection_id
    join track on collection_track.track_id = track.id
    join album on track.album_id = album.id
    join performer_album on album.id = performer_album.album_id
    join performer on performer_album.performer_id = performer.id 
    where performer.alias = 'Êמבחמם';
	       
--6
select album.name from album
    join performer_album on album.id = performer_album.album_id 
    where performer_album.performer_id in 
    (select performer_id from genre_performer
        group by performer_id 
        having count(genre_id) > 1);
        
--7
select name from track t
    left join collection_track ct
    on t.id = ct.track_id
    where ct.track_id is null;
   
--8
select performer.alias from performer
    join performer_album on performer.id = performer_album.performer_id
    where performer_album.album_id in 
        (select track.album_id from track
            where track.duration = (select min(duration) from track));
   
   
--9 
select album.name from album
    where album.id in 
        (select track.album_id from track
            group by track.album_id
            having count(track.id) = 
                (select min(track_count) from
                    (select count(id) as track_count from track
                        group by album_id) as t));
                     
		


       