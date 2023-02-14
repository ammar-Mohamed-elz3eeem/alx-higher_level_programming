-- display average temperature (Fahrenheit) by city ordered by temperature (descending)
SELECT city, AVG(value) AS city_temp FROM temperatures GROUP BY city ORDER BY city_temp DESC
