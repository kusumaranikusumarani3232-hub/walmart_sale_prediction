CREATE DATABASE walmart_db;
CREATE TABLE walmart_sales (
    Store INT,
    Date DATE,
    Weekly_Sales FLOAT,
    Holiday_Flag INT,
    Temperature FLOAT,
    Fuel_Price FLOAT,
    CPI FLOAT,
    Unemployment FLOAT
);
SELECT SUM(Weekly_Sales) AS Total_Sales
FROM walmart_sales;
SELECT SUM(Weekly_Sales) AS Total_Sales
FROM walmart_sales;
USE walmart_db;
SELECT * 
FROM walmart_clean
LIMIT 10;
SELECT SUM(Weekly_Sales) AS Total_Sales
FROM walmart_clean;
SELECT Store,
SUM(Weekly_Sales) AS Total_Sales
FROM walmart_clean
GROUP BY Store
ORDER BY Total_Sales DESC
LIMIT 10;
SELECT Holiday_Flag,
AVG(Weekly_Sales) AS Avg_Sales
FROM walmart_clean
GROUP BY Holiday_Flag;
SELECT MONTH(Date) AS Month,
SUM(Weekly_Sales) AS Monthly_Sales
FROM walmart_clean
GROUP BY MONTH(Date)
ORDER BY MONTH(Date);
SELECT ROUND(AVG(Temperature),2) AS Avg_Temperature,
ROUND(AVG(Weekly_Sales),2) AS Avg_Sales
FROM walmart_clean;
