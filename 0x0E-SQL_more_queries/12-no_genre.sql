-- script that lists all shows contained in hbtn_0d_tvshows with that has no genres

SELECT shows.title, genere.genre_id FROM tv_shows AS shows
LEFT JOIN tv_show_genres AS genere 
ON shows.id = genere.show_id
WHERE genere.genre_id IS NULL
ORDER BY shows.title ASC, genere.genre_id ASC;
