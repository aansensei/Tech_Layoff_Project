# 📂 Data Directory / Thư mục Dữ liệu

## 🇬🇧 English Version
This directory contains all datasets used in the analysis, categorized by their processing stage.

### 1. Raw Data (`/raw`)
Unprocessed data fetched directly from APIs or sources.
* **`tech_layoffs_til_2025.csv`**: The primary dataset of global layoff events (Source: Layoffs.fyi).
* **`macro_economics_data.csv`**: Key economic indicators (Fed Funds Rate, CPI, GDP, Unemployment) fetched via FRED API.
* **`big_tech_stock_prices.csv`**: Daily historical stock prices for major tech companies (Meta, Amazon, etc.) fetched via `yfinance`.

### 2. Processed Data (`/processed`)
Cleaned and transformed data ready for analysis.
* **`tech_layoffs_clean.csv`**: Standardized layoff data (Dates formatted, nulls handled).
* **`big_tech_stock_clean.csv`**: Aggregated monthly stock data including calculated returns and monthly average prices.

---

## 🇻🇳 Vietnamese Version
Thư mục này chứa tất cả các tập dữ liệu được sử dụng, phân loại theo giai đoạn xử lý.

### 1. Dữ liệu thô (`/raw`)
Dữ liệu gốc được lấy trực tiếp từ API hoặc các nguồn khác.
* **`tech_layoffs_til_2025.csv`**: Dữ liệu chính về các đợt sa thải toàn cầu.
* **`macro_economics_data.csv`**: Các chỉ số kinh tế vĩ mô (Lãi suất Fed, CPI, GDP, Thất nghiệp) lấy từ FRED API.
* **`big_tech_stock_prices.csv`**: Giá cổ phiếu lịch sử theo ngày của các công ty công nghệ lớn, lấy qua `yfinance`.

### 2. Dữ liệu đã xử lý (`/processed`)
Dữ liệu đã được làm sạch và chuyển đổi để phục vụ phân tích.
* **`tech_layoffs_clean.csv`**: Dữ liệu sa thải đã chuẩn hóa (định dạng ngày tháng, xử lý giá trị rỗng).
* **`big_tech_stock_clean.csv`**: Dữ liệu chứng khoán đã được gộp theo tháng (tính toán lợi suất và giá trung bình tháng).