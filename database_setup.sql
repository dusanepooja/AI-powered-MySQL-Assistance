create database sql_assistant ;

CREATE TABLE customer (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    email VARCHAR(100),
    join_date DATE
);

CREATE TABLE sales (
    sale_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT,
    product VARCHAR(100),
    amount DECIMAL(10,2),
    sale_date DATE,
    FOREIGN KEY (customer_id) REFERENCES customer(customer_id)
);

INSERT INTO customer (name, email, join_date) VALUES
('Ravi Kumar', 'ravi.kumar@example.com', '2023-01-10'),
('Priya Verma', 'priya.verma@example.com', '2023-02-18'),
('Arjun Mehta', 'arjun.mehta@example.com', '2023-03-05'),
('Sneha Iyer', 'sneha.iyer@example.com', '2023-04-12'),
('Suresh Reddy', 'suresh.reddy@example.com', '2023-05-20'),
('Kavita Desai', 'kavita.desai@example.com', '2023-06-25'),
('Anil Sharma', 'anil.sharma@example.com', '2023-07-15'),
('Anjali Gupta', 'anjali.gupta@example.com', '2023-08-30');

INSERT INTO sales (customer_id, product, amount, sale_date) VALUES
(1, 'Laptop', 55000.00, '2023-09-01'),
(2, 'Cosmetics', 2500.00, '2023-09-05'),
(3, 'Smartphone', 30000.00, '2023-09-10'),
(4, 'Washing Machine', 18000.00, '2023-09-15'),
(5, 'Groceries', 3500.00, '2023-09-20'),
(6, 'Air Conditioner', 40000.00, '2023-09-25'),
(7, 'Shoes', 2500.00, '2023-09-28'),
(8, 'Handbag', 4500.00, '2023-09-30');
