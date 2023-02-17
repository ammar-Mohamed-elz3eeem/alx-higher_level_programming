-- list all comedy shows

SELECT title FROM tv_shows tvs
INNER JOIN tv_show_genres tvsg
ON tvs.id = tvsg.show_id
INNER JOIN tv_genres tvg
ON tvg.id = tvsg.genre_id
WHERE tvg.name = 'Comedy'
ORDER BY tvs.title
