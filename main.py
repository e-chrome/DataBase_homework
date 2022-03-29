import sqlalchemy

db = 'postgresql://student:1234@localhost:5432/music'
engine = sqlalchemy.create_engine(db)
connection = engine.connect()

# Исполнители
connection.execute("""
insert into performer(alias)
    values('Игорь Николаев');
""")
connection.execute("""
insert into performer(alias)
    values('Михаил Круг');
""")
connection.execute("""
insert into performer(alias)
    values('Серж Танкян');
""")
connection.execute("""
insert into performer(alias)
    values('Игорь Растеряев');
""")
connection.execute("""
insert into performer(alias)
    values('Оксимирон');
""")
connection.execute("""
insert into performer(alias)
    values('Слава КПСС');
""")
connection.execute("""
insert into performer(alias)
    values('Кобзон');
""")
connection.execute("""
insert into performer(alias)
    values('Пудель');
""")

# Жанры
connection.execute("""
insert into genre(name)
    values('Поп');
""")
connection.execute("""
insert into genre(name)
    values('Рок');
""")
connection.execute("""
insert into genre(name)
    values('Инди');
""")
connection.execute("""
insert into genre(name)
    values('Рэп');
""")
connection.execute("""
insert into genre(name)
    values('Фольк');
""")
connection.execute("""
insert into genre(name)
    values('Метал');
""")
connection.execute("""
insert into genre(name)
    values('Кантри');
""")
connection.execute("""
insert into genre(name)
    values('Индастриал');
""")

# Исполнители-жанры
connection.execute("""
insert into genre_performer(genre_id, performer_id)
    values(1, 1);
""")
connection.execute("""
insert into genre_performer(genre_id, performer_id)
    values(2, 2);
""")
connection.execute("""
insert into genre_performer(genre_id, performer_id)
    values(3, 3);
""")
connection.execute("""
insert into genre_performer(genre_id, performer_id)
    values(4, 4);
""")
connection.execute("""
insert into genre_performer(genre_id, performer_id)
    values(5, 5);
""")
connection.execute("""
insert into genre_performer(genre_id, performer_id)
    values(6, 6);
""")
connection.execute("""
insert into genre_performer(genre_id, performer_id)
    values(7, 7);
""")
connection.execute("""
insert into genre_performer(genre_id, performer_id)
    values(8, 8);
""")

# Альбомы
connection.execute("""
insert into album(name, year_of_issue)
    values('Седая голова', 1993);
""")
connection.execute("""
insert into album(name, year_of_issue)
    values('Белые шахматы', 2020);
""")
connection.execute("""
insert into album(name, year_of_issue)
    values('Железный занавес', 2018);
""")
connection.execute("""
insert into album(name, year_of_issue)
    values('Жесткая вода', 2011);
""")
connection.execute("""
insert into album(name, year_of_issue)
    values('Кружка', 2012);
""")
connection.execute("""
insert into album(name, year_of_issue)
    values('Пьяный дятел', 2009);
""")
connection.execute("""
insert into album(name, year_of_issue)
    values('Баррикадная', 2001);
""")
connection.execute("""
insert into album(name, year_of_issue)
    values('Снимай тапки', 2008);
""")

# Исполнители-альбомы
connection.execute("""
insert into performer_album(performer_id, album_id)
    values(1, 1);
""")
connection.execute("""
insert into performer_album(performer_id, album_id)
    values(2, 2);
""")
connection.execute("""
insert into performer_album(performer_id, album_id)
    values(3, 3);
""")
connection.execute("""
insert into performer_album(performer_id, album_id)
    values(4, 4);
""")
connection.execute("""
insert into performer_album(performer_id, album_id)
    values(5, 5);
""")
connection.execute("""
insert into performer_album(performer_id, album_id)
    values(6, 6);
""")
connection.execute("""
insert into performer_album(performer_id, album_id)
    values(7, 7);
""")
connection.execute("""
insert into performer_album(performer_id, album_id)
    values(8, 8);
""")

# Треки
connection.execute("""
insert into track(album_id, name, duration)
    values(1, 'Ночь', 2.34);
""")
connection.execute("""
insert into track(album_id, name, duration)
    values(1, 'День', 3.34);
""")
connection.execute("""
insert into track(album_id, name, duration)
    values(2, 'Весна', 2.34);
""")
connection.execute("""
insert into track(album_id, name, duration)
    values(2, 'Лето', 3.34);
""")
connection.execute("""
insert into track(album_id, name, duration)
    values(3, 'Автобус', 1.34);
""")
connection.execute("""
insert into track(album_id, name, duration)
    values(3, 'Трамвай', 6.34);
""")
connection.execute("""
insert into track(album_id, name, duration)
    values(4, 'Горец', 1.34);
""")
connection.execute("""
insert into track(album_id, name, duration)
    values(4, 'Равнинец', 6.34);
""")
connection.execute("""
insert into track(album_id, name, duration)
    values(5, 'Петербуржец', 2.34);
""")
connection.execute("""
insert into track(album_id, name, duration)
    values(5, 'Москвич', 2.34);
""")
connection.execute("""
insert into track(album_id, name, duration)
    values(6, 'Луна', 2.34);
""")
connection.execute("""
insert into track(album_id, name, duration)
    values(6, 'Солнце', 3.34);
""")
connection.execute("""
insert into track(album_id, name, duration)
    values(7, 'Самопряха', 4.34);
""")
connection.execute("""
insert into track(album_id, name, duration)
    values(7, 'Конвейер', 7.34);
""")
connection.execute("""
insert into track(album_id, name, duration)
    values(8, 'Лодка', 2.34);
""")
connection.execute("""
insert into track(album_id, name, duration)
    values(8, 'Шлюпка', 6.34);
""")
connection.execute("""
insert into track(album_id, name, duration)
    values(8, 'Мой ковбой', 6.34);
""")


# Коллекция
connection.execute("""
insert into collection(name, year_of_issue)
    values('Сельская туса', 1998);
""")
connection.execute("""
insert into collection(name, year_of_issue)
    values('Московский пряник', 2020);
""")
connection.execute("""
insert into collection(name, year_of_issue)
    values('Космос-нефть-газ', 2019);
""")
connection.execute("""
insert into collection(name, year_of_issue)
    values('Голубые береты', 2011);
""")
connection.execute("""
insert into collection(name, year_of_issue)
    values('Пальмы на снегу', 2012);
""")
connection.execute("""
insert into collection(name, year_of_issue)
    values('Великие фантазеры', 2017);
""")
connection.execute("""
insert into collection(name, year_of_issue)
    values('Любо', 2016);
""")
connection.execute("""
insert into collection(name, year_of_issue)
    values('Включи телек', 2015);
""")

# Коллекция-трек
connection.execute("""
insert into collection_track(collection_id, track_id)
    values(1, 9);
""")
connection.execute("""
insert into collection_track(collection_id, track_id)
    values(2, 10);
""")
connection.execute("""
insert into collection_track(collection_id, track_id)
    values(3, 11);
""")
connection.execute("""
insert into collection_track(collection_id, track_id)
    values(4, 12);
""")
connection.execute("""
insert into collection_track(collection_id, track_id)
    values(5, 13);
""")
connection.execute("""
insert into collection_track(collection_id, track_id)
    values(6, 14);
""")
connection.execute("""
insert into collection_track(collection_id, track_id)
    values(7, 15);
""")
connection.execute("""
insert into collection_track(collection_id, track_id)
    values(8, 16);
""")