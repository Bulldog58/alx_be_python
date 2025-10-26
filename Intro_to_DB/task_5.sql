-- FILE: task_5.sql
-- This script inserts a single customer record into the CUSTOMERS table.

INSERT INTO CUSTOMERS (
    CUSTOMER_ID, 
    CUSTOMER_NAME, 
    EMAIL, 
    ADDRESS
) 
VALUES (
    1, 
    'Cole Baidoo', 
    'cbaidoo@sandtech.com', 
    '123 Happiness Ave.'
);