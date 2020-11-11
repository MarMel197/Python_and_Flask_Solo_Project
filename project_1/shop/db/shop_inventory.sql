DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS manufacturers;

CREATE TABLE manufacturers (
    id SERIAL PRIMARY KEY,
    manufacturer_name VARCHAR(255),
    product_type VARCHAR(255)
);

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    product_name VARCHAR(255),
    product_description VARCHAR(255),
    stock_on_hand INT,
    out_of_stock BOOLEAN,
    item_cost INT,
    item_sell INT,
    manufacturers_id INT REFERENCES manufacturers(id)
);

