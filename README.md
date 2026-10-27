# E-Commerce Sales Performance & Customer Insights Case Study

## 1. Project Overview & Problem Statement
An online retail business has seen fluctuating revenue and declining profit margins over the last two quarters across multiple product categories and regions. The management lacked visibility into product-level profitability, regional demand, and customer repeat behavior.

**Objective:**
- Analyze sales transaction data to uncover revenue drivers and profit leaks.
- Clean and model raw transaction records for accurate reporting.
- Build an interactive performance dashboard for business stakeholders.
- Provide actionable, data-driven recommendations to boost profitability and customer retention.

---

## 2. Dataset Information
- **Dataset Name:** Online E-Commerce Transactions Dataset
- **Total Records:** 54,190 rows × 12 columns
- **Time Period:** January 2023 – December 2023
- **Key Columns:**
  - `Order_ID`: Unique transaction identifier
  - `Order_Date`: Date of purchase
  - `Customer_ID`: Unique customer reference
  - `Region`: Geographic zone (North, South, East, West)
  - `Category`: Product category (Electronics, Apparel, Home & Living)
  - `Quantity`: Number of units sold
  - `Unit_Price`: Price per unit (₹)
  - `Discount`: Discount percentage applied
  - `Total_Sales`: Net sales after discount
  - `Profit`: Net profit earned per line item

---

## 3. Data Cleaning & Transformation Process
The raw data contained nulls, inconsistent date values, and outliers. The following cleaning pipeline was executed using Python (Pandas) and SQL:

1. **Handling Missing Values:**
   - 1,240 records with missing `Customer_ID` were tagged as `'Guest_User'` to preserve transaction volume while keeping customer tracking distinct.
   - Removed 18 rows where `Total_Sales` or `Unit_Price` were null.
2. **Duplicate Removal:**
   - Identified and dropped 312 exact duplicate transaction logs.
3. **Data Type Correction:**
   - Converted `Order_Date` from text to standard `datetime64[ns]` format.
   - Enforced integer types for `Quantity` and float types for monetary fields.
4. **Outlier & Sanity Checks:**
   - Filtered out negative quantities and invalid return entries with zero unit prices.
   - Cleaned region naming inconsistencies (e.g., standardized `'west'`, `'WEST'` to `'West'`).
5. **Feature Engineering:**
   - Created `Profit_Margin_Pct` = `(Profit / Total_Sales) * 100`
   - Generated `Order_Month` and `Weekday_Name` for seasonal trend analysis.

---

## 4. Key Exploratory Analysis & Patterns
- **Seasonal Spikes:** Sales peaked heavily during Q4 (October–December), contributing 38% of annual revenue, driven by festive demand.
- **Discount Paradox:** Discounts exceeding 25% in the Apparel category generated high volume but resulted in a negative net profit margin (-4.2%).
- **Regional Disparity:** The West region generated the highest total revenue (34%), but the South region delivered the healthiest profit margin (21%).
- **Pareto Principle (80/20 Rule):** Top 20% of high-volume SKUs generated 72% of total retail profits.

---

## 5. Dashboard Architecture & KPIs
An interactive analytical dashboard was created with the following components:

- **Executive KPI Cards:**
  - Total Revenue: ₹1.42 Cr
  - Total Profit: ₹26.8 Lakhs
  - Average Profit Margin: 18.8%
  - Total Orders: 52,620
- **Visuals Included:**
  - Monthly Revenue & Profit Trend (Dual-axis Line Chart)
  - Category-wise Profitability Breakdown (Bar Chart)
  - Regional Sales Share (Donut / Map Chart)
  - Discount vs Profit Correlation (Scatter Plot)
- **Interactive Slicers:** Date Range, Product Category, and Region filters for self-serve drill-down.

---

## 6. Actionable Business Recommendations
1. **Cap Aggressive Discounts:** Limit discounts on low-margin categories (Apparel & Accessories) to a maximum of 15% to stop profit leaks.
2. **Double Down on High-Margin Categories:** Reallocate digital marketing spend toward Electronics and Home Living in the South and West regions, which show the highest return on ad spend.
3. **Festive Inventory Planning:** Increase warehouse inventory levels 30 days before Q4 to prevent stock-outs during peak festive sales.
4. **Customer Retention Incentive:** Launch a loyalty tier for repeat buyers (more than 3 orders) to boost Customer Lifetime Value (CLV) without relying on heavy discounts.

---

## 7. Tech Stack Used
- **Data Cleaning & Manipulation:** Python (Pandas, NumPy)
- **Database Querying:** SQL
- **Data Visualization & Dashboard:** Power BI / Excel
- **Version Control:** Git & GitHub
-
