DROP TABLE IF EXISTS manufacturer;
DROP TABLE IF EXISTS product;

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    product_name VARCHAR(255),
    product_description VARCHAR(255),
    stock_on_hand INT,
    out_of_stock BOOLEAN,
    item_cost FLOAT,
    item_sell FLOAT,
    product_id INT REFERENCES products(id)
);

CREATE TABLE manufacturers (
    id SERIAL PRIMARY KEY,
    manufacturer_name VARCHAR(255),
    product_type VARCHAR(255)
);