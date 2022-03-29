select name, year_of_issue from album
    where year_of_issue = 2018;
    
select name, duration from track
    order by duration desc 
    limit 1;

select name from track
    where duration >= 3.5;
    
select name from collection
    where year_of_issue between 2018 and 2020;
    
select alias from performer
    where alias not like '% %';
    
select name from track
    where name like '%Мой%';