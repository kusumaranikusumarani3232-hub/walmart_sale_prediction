# Walmart Sales Analysis Using MySQL

## Project Overview
This project analyzes Walmart sales data using MySQL to discover business insights, customer behavior, sales trends, and product performance.

The goal of this project is to practice SQL skills and perform real-world business data analysis.

---

## Dataset Information
The dataset contains Walmart sales transaction records including:

- Branch
- City
- Product Category
- Quantity Sold
- Total Sales
- Payment Method
- Customer Type
- Date and Time

---

## Tools & Technologies Used
- MySQL
- SQL
- GitHub
- Excel (Optional)
- Power BI / Tableau (Optional)

---

## SQL Concepts Used
- SELECT Statements
- WHERE Clause
- GROUP BY
- ORDER BY
- Aggregate Functions
- CASE Statements
- Subqueries
- Window Functions

---

## Business Questions Solved

### Sales Analysis
- Which branch has the highest sales?
- Which product line generates the most revenue?
- What are the monthly sales trends?

### Customer Analysis
- Which customer type spends more?
- Which payment method is used the most?

### Product Analysis
- Best selling product categories
- Highest rated product lines

---

## Key Insights
- Identified top-performing Walmart branches
- Found most profitable product categories
- Analyzed customer purchasing patterns
- Discovered peak sales periods

---

## Project Structure

```text
Walmart-SQL-Project/
│
├── data/
│   └── walmart_clean.csv
│
├── sql/
│   └── walmart.sql
│
├── screenshots/
│
└── README.md
SELECT branch, SUM(total) AS total_revenue
FROM walmart_sales
GROUP BY branch
ORDER BY total_revenue DESC;
How to Run This Project_


Import dataset into MySQL


Run SQL queries from walmart.sql


Analyze outputs and insights



Project Outcome
This project improved my practical SQL skills and helped me understand how SQL is used for real-world business analysis.

Author
Kusumarani
