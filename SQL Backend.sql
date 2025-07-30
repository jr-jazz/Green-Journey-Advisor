USE green_journey;
DROP TABLE IF EXISTS travel_options;
CREATE TABLE travel_options (
    id INT AUTO_INCREMENT PRIMARY KEY,
    start_point VARCHAR(255) NOT NULL,
    end_point VARCHAR(255) NOT NULL,
    transport_mode VARCHAR(50) NOT NULL,
    carbon_footprint FLOAT NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);

INSERT INTO travel_options (start_point, end_point, transport_mode, carbon_footprint, price) VALUES
('London', 'Paris', 'Train', 0.05, 50.00),
('London', 'Paris', 'Bus', 0.08, 30.00),
('London', 'Paris', 'Electric Car', 0.1, 70.00),
('Paris', 'Amsterdam', 'Train', 0.04, 60.00),
('Paris', 'Amsterdam', 'Bus', 0.07, 35.00),
('Paris', 'Amsterdam', 'Electric Car', 0.09, 80.00),
('Amsterdam', 'London', 'Train', 0.06, 55.00),
('Amsterdam', 'London', 'Bus', 0.09, 40.00),
('Amsterdam', 'London', 'Electric Car', 0.11, 75.00);

SELECT * FROM travel_options;



CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);


INSERT INTO travel_options (start_point, end_point, transport_mode, carbon_footprint, price) VALUES
('Berlin', 'Rome', 'Train', 50.00, 120.00),
('Berlin', 'Rome', 'Bus', 80.00, 90.00),
('Rome', 'Madrid', 'Train', 60.00, 150.00),
('Rome', 'Madrid', 'Bus', 90.00, 110.00),
('Madrid', 'London', 'Train', 70.00, 200.00),
('Madrid', 'Paris', 'Bus', 85.00, 100.00),
('Berlin', 'Amsterdam', 'Train', 45.00, 130.00);



INSERT INTO travel_options (start_point, end_point, transport_mode, carbon_footprint, price) VALUES
('London', 'Amsterdam', 'Train', 0.06, 55.00),
('London', 'Amsterdam', 'Bus', 0.09, 40.00),
('London', 'Amsterdam', 'Electric Car', 0.11, 75.00),
('Amsterdam', 'London', 'Train', 0.06, 55.00),
('Amsterdam', 'London', 'Bus', 0.09, 40.00),
('Amsterdam', 'London', 'Electric Car', 0.11, 75.00),

('London', 'Berlin', 'Train', 0.12, 100.00),
('London', 'Berlin', 'Bus', 0.15, 80.00),
('London', 'Berlin', 'Electric Car', 0.18, 120.00),
('Berlin', 'London', 'Train', 0.12, 100.00),
('Berlin', 'London', 'Bus', 0.15, 80.00),
('Berlin', 'London', 'Electric Car', 0.18, 120.00),

('London', 'Rome', 'Train', 0.14, 130.00),
('London', 'Rome', 'Bus', 0.17, 110.00),
('London', 'Rome', 'Electric Car', 0.20, 150.00),
('Rome', 'London', 'Train', 0.14, 130.00),
('Rome', 'London', 'Bus', 0.17, 110.00),
('Rome', 'London', 'Electric Car', 0.20, 150.00),

('London', 'Madrid', 'Train', 0.16, 140.00),
('London', 'Madrid', 'Bus', 0.19, 120.00),
('London', 'Madrid', 'Electric Car', 0.22, 160.00),
('Madrid', 'London', 'Bus', 0.19, 120.00),
('Madrid', 'London', 'Electric Car', 0.22, 160.00),

('Paris', 'Berlin', 'Train', 0.09, 90.00),
('Paris', 'Berlin', 'Bus', 0.12, 70.00),
('Paris', 'Berlin', 'Electric Car', 0.14, 100.00),
('Berlin', 'Paris', 'Train', 0.09, 90.00),
('Berlin', 'Paris', 'Bus', 0.12, 70.00),
('Berlin', 'Paris', 'Electric Car', 0.14, 100.00),

('Paris', 'Rome', 'Train', 0.11, 100.00),
('Paris', 'Rome', 'Bus', 0.13, 85.00),
('Paris', 'Rome', 'Electric Car', 0.16, 120.00),
('Rome', 'Paris', 'Train', 0.11, 100.00),
('Rome', 'Paris', 'Bus', 0.13, 85.00),
('Rome', 'Paris', 'Electric Car', 0.16, 120.00),

('Paris', 'Madrid', 'Train', 0.13, 110.00),
('Paris', 'Madrid', 'Bus', 0.17, 95.00),
('Paris', 'Madrid', 'Electric Car', 0.18, 130.00),
('Madrid', 'Paris', 'Train', 0.13, 110.00),
('Madrid', 'Paris', 'Electric Car', 0.18, 130.00),

('Amsterdam', 'Berlin', 'Train', 0.08, 85.00),
('Amsterdam', 'Berlin', 'Bus', 0.10, 90.00),
('Amsterdam', 'Berlin', 'Electric Car', 0.12, 110.00),
('Berlin', 'Amsterdam', 'Bus', 0.10, 90.00),
('Berlin', 'Amsterdam', 'Electric Car', 0.12, 110.00),

('Amsterdam', 'Rome', 'Train', 0.15, 140.00),
('Amsterdam', 'Rome', 'Bus', 0.18, 120.00),
('Amsterdam', 'Rome', 'Electric Car', 0.20, 150.00),
('Rome', 'Amsterdam', 'Train', 0.15, 140.00),
('Rome', 'Amsterdam', 'Bus', 0.18, 120.00),
('Rome', 'Amsterdam', 'Electric Car', 0.20, 150.00),

('Amsterdam', 'Madrid', 'Train', 0.17, 150.00),
('Amsterdam', 'Madrid', 'Bus', 0.20, 130.00),
('Amsterdam', 'Madrid', 'Electric Car', 0.23, 170.00),
('Madrid', 'Amsterdam', 'Train', 0.17, 150.00),
('Madrid', 'Amsterdam', 'Bus', 0.20, 130.00),
('Madrid', 'Amsterdam', 'Electric Car', 0.23, 170.00),

('Berlin', 'Madrid', 'Train', 0.20, 160.00),
('Berlin', 'Madrid', 'Bus', 0.23, 140.00),
('Berlin', 'Madrid', 'Electric Car', 0.26, 180.00),
('Madrid', 'Berlin', 'Train', 0.20, 160.00),
('Madrid', 'Berlin', 'Bus', 0.23, 140.00),
('Madrid', 'Berlin', 'Electric Car', 0.26, 180.00),

('Madrid', 'Rome', 'Electric Car', 0.22, 160.00),
('Rome', 'Madrid', 'Electric Car', 0.22, 160.00);
