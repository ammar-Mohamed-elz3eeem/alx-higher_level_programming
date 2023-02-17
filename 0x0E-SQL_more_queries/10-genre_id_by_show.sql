-- script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked

SELECT shows.title, genere.genre_id FROM tv_shows AS shows 
INNER JOIN tv_show_genres AS genere 
ON shows.id = genere.show_id
ORDER BY shows.title ASC, genere.genre_id ASC
