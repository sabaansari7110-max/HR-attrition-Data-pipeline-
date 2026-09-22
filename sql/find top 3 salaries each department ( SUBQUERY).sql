-- ----Find Top 3 Salaries in Each Department-------

USE sqli_project;

SELECT * FROM 
(SELECT first_name, age, office_type, department, SALARY, DOB, level,
ROW_NUMBER() OVER( PARTITION BY department ORDER BY salary DESC) AS ranking
FROM  company_data
WHERE department IS NOT NULL) AS ranked_data
where ranking <= 3;

SELECT * FROM company_data;