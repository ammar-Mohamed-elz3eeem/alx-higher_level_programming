-- script that lists all shows contained in hbtn_0d_tvshows with thier genre id or null instead

SELECT shows.title, genere.genre_id FROM tv_shows AS shows 
LEFT JOIN tv_show_genres AS genere 
ON shows.id = genere.show_id
ORDER BY shows.title ASC, genere.genre_id ASC;
