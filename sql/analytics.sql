-- E-Commerce Sales Analytics
-- These queries analyze the data loaded into the sales table.


-- 1. Total completed revenue
SELECT
    ROUND(SUM(total_amount), 2) AS total_revenue
FROM sales
WHERE status = 'Completed';


-- 2. Total number of completed orders
SELECT
    COUNT(DISTINCT order_id) AS total_orders
FROM sales
WHERE status = 'Completed';


-- 3. Revenue by country
SELECT
    country,
    ROUND(SUM(total_amount), 2) AS revenue
FROM sales
WHERE status = 'Completed'
GROUP BY country
ORDER BY revenue DESC;


-- 4. Revenue by product category
SELECT
    category,
    ROUND(SUM(total_amount), 2) AS revenue
FROM sales
WHERE status = 'Completed'
GROUP BY category
ORDER BY revenue DESC;


-- 5. Top 5 products by revenue
SELECT
    product_name,
    ROUND(SUM(total_amount), 2) AS revenue
FROM sales
WHERE status = 'Completed'
GROUP BY product_name
ORDER BY revenue DESC
LIMIT 5;


-- 6. Monthly revenue
SELECT
    strftime('%Y-%m', order_date) AS month,
    ROUND(SUM(total_amount), 2) AS revenue
FROM sales
WHERE status = 'Completed'
GROUP BY month
ORDER BY month;


-- 7. Average order value
SELECT
    ROUND(
        SUM(total_amount) / COUNT(DISTINCT order_id),
        2
    ) AS average_order_value
FROM sales
WHERE status = 'Completed';


-- 8. Customers ranked by spending
SELECT
    customer_id,
    customer_name,
    ROUND(SUM(total_amount), 2) AS total_spent
FROM sales
WHERE status = 'Completed'
GROUP BY customer_id, customer_name
ORDER BY total_spent DESC;


-- 9. Cancelled orders
SELECT
    COUNT(DISTINCT order_id) AS cancelled_orders
FROM sales
WHERE status = 'Cancelled';


-- 10. Daily sales summary
SELECT
    order_date,
    COUNT(DISTINCT order_id) AS orders,
    ROUND(SUM(total_amount), 2) AS revenue
FROM sales
WHERE status = 'Completed'
GROUP BY order_date
ORDER BY order_date;