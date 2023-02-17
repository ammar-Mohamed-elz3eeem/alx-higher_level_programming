-- lists all genres of the show Dexter

SELECT name FROM tv_genres WHERE name NOT IN (
	SELECT tvg.name FROM tv_genres tvg 
	INNER JOIN tv_show_genres tv_g_s
	ON tv_g_s.genre_id = tvg.id
	INNER JOIN tv_shows tv_s
	ON tv_s.id = tv_g_s.show_id
	WHERE tv_s.title = 'Dexter'
	ORDER BY tvg.name ASC
);
ORDER BY name ASC;
