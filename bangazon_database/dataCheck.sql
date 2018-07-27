-- Use this to verify that there is data in the database

SELECT 'Employee', COUNT(*) as 'Number of Records' FROM bangazonapi_employee UNION ALL
SELECT 'Employee_Training', COUNT(*) as 'Number of Records' FROM bangazonapi_employee_training UNION ALL
SELECT 'Computer', COUNT(*) as 'Number of Records' FROM bangazonapi_computer UNION ALL
SELECT 'Cust_Order', COUNT(*) as 'Number of Records' FROM bangazonapi_cust_order UNION ALL
SELECT 'Department', COUNT(*) as 'Number of Records' FROM bangazonapi_department UNION ALL
SELECT 'Employment_Dates', COUNT(*) as 'Number of Records' FROM bangazonapi_employment_dates UNION ALL
SELECT 'Ordered_Products', COUNT(*) as 'Number of Records' FROM bangazonapi_ordered_products UNION ALL
SELECT 'Payment_Options', COUNT(*) as 'Number of Records' FROM bangazonapi_payment_options UNION ALL
SELECT 'Payment_Type', COUNT(*) as 'Number of Records' FROM bangazonapi_payment_type UNION ALL
SELECT 'Product', COUNT(*) as 'Number of Records' FROM bangazonapi_product UNION ALL
SELECT 'Product_Type', COUNT(*) as 'Number of Records' FROM bangazonapi_product_type UNION ALL
SELECT 'Training_Program', COUNT(*) as 'Number of Records' FROM bangazonapi_training_program UNION ALL
SELECT 'Training_Program_Sessions', COUNT(*) as 'Number of Records' FROM bangazonapi_training_program_sessions UNION ALL
SELECT 'User', COUNT(*) as 'Number of Records' FROM bangazonapi_user;