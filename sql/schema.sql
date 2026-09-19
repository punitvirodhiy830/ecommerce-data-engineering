CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER NOT NULL,
    order_date DATE NOT NULL,
    customer_id VARCHAR(50) NOT NULL,
    customer_name VARCHAR(100),
    country VARCHAR(100),
    product_id VARCHAR(50) NOT NULL,
    product_name VARCHAR(150),
    category VARCHAR(100),
    quantity INTEGER NOT NULL,
    unit_price DECIMAL(12, 2) NOT NULL,
    status VARCHAR(30),
    total_amount DECIMAL(14, 2) NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_orders_order_date
ON orders(order_date);

CREATE INDEX IF NOT EXISTS idx_orders_customer_id
ON orders(customer_id);

CREATE INDEX IF NOT EXISTS idx_orders_product_id
ON orders(product_id);