-- Homework ¹2
create table if not exists Genre (
    Id serial primary key,
    Name varchar(40) not null
);

create table if not exists Performer (
    Id serial primary key,
    Genre_id integer references Genre(Id),
    Alias varchar(40) not null
);

create table if not exists Album (
    Id serial primary key,
    Performer_id integer references Performer(Id),
    Name varchar(40) not null,
    Year_of_issue integer check(Year_of_issue > 1900 and Year_of_issue < 3000)
);

create table if not exists Track (
    Id serial primary key,
    Album_id integer references Album(Id),
    Name varchar(40) not null,
    Duration numeric(4,2) check(duration > 0)
);

alter table Album alter column Year_of_issue set not null;
alter table Track alter column Duration set not null;

-- Homework ¹3

alter table Performer drop column Genre_id cascade;

create table if not exists Genre_Performer (
    Genre_id integer references Genre(Id),
    Performer_id integer references Performer(Id)
);

alter table Album drop column Performer_id cascade;

create table if not exists Performer_Album (
    Performer_id integer references Performer(Id),
    Album_id integer references Album(Id)
);

create table if not exists Collection (
    Id serial primary key,
    Name varchar(40) not null,
    Year_of_issue integer not null check(Year_of_issue > 1900 and Year_of_issue < 3000)
);

create table if not exists Collection_track (
    Collection_id integer references Collection(Id),
    Track_id integer references Track(Id)
);

alter table genre_performer 
    add constraint genre_performer_pk
    primary key(genre_id, performer_id);

alter table collection_track 
    add constraint collection_track_pk
    primary key(collection_id, track_id);
   
alter table performer_album  
    add constraint performer_album_pk
    primary key(performer_id, album_id);
   

