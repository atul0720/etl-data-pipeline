SELECT product_name, SUM(total_price) AS revenue
FROM sales
GROUP BY product_name
ORDER BY revenue DESC;