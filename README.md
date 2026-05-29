# Global Tech Layoffs Analysis (2020 - 2026)
### An Intersection of Macroeconomics, Financial Markets, and Data Science

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg) ![Machine Learning](https://img.shields.io/badge/Model-Random_Forest-orange.svg) ![Dashboard](https://img.shields.io/badge/Web_App-HuggingFace-yellow.svg) ![Status](https://img.shields.io/badge/Status-Project_Completed-success.svg)

---

[Ấn để xem bản Tiếng Việt](#phiên-bản-tiếng-việt)

---

## English Version

### Professional Profile
I am **Cao Thien An Nguyen** (Preffered name: An), an international student at the **University of Wisconsin-Madison** pursuing a **Double Major in Data Science and Economics**. My academic background allows me to bridge the gap between quantitative data engineering and theoretical economic modeling. I aspire to build a career at the intersection of **Data Science, Economic Analysis, and Quantitative Research**.

This project serves as a comprehensive case study on **Labor Economics and Market Dynamics**. By leveraging the research-driven environment at UW-Madison, I aim to decode how global financial shifts translate into internal corporate restructuring within the technology sector.

### Live Interactive Web Dashboard (Hugging Face Spaces)
To make the data accessible and actionable, I developed a live web application using **Streamlit**. This dashboard allows users to interactively explore the findings of this research in real-time.

* **Real-time Exploration:** Filter layoffs by year and specific industries to see localized trends.
* **AI vs. Reality Visualization:** An interactive Plotly chart comparing the Random Forest model's predictions against actual market events.
* **Dynamic Insights:** Automated insight generation based on selected data ranges, highlighting the "Social Contagion" gap.
* **Raw Data Access:** Transparent access to the processed dataset for independent verification.

**[Click Here to View the Live Dashboard](https://aansensei-tech-layoff-analytics.hf.space)**

### Project Architecture
1.  **Data Engineering:** Aggregated data from FRED (Macro), Yahoo Finance (Stocks), and Layoffs.fyi using Python & SQL.
2.  **Exploratory Analysis (EDA):** Identified the "3-month lag" correlation between stock crashes and layoffs using Dual-Axis Visualization.
3.  **Predictive Modeling (Phase 4):** Built **Linear Regression** and **Random Forest** models to forecast layoff trends based on lagged economic indicators.
4.  **Business Intelligence (Phase 5):** Designed an interactive **Streamlit Web App** and a Tableau Dashboard to visualize the "Forecast vs. Reality" gap for stakeholders.

---

## Phase 5: The Intelligence Dashboard
*Visualizing the correlation between AI predictions and actual market events.*

![Dashboard Preview](https://raw.githubusercontent.com/aansensei/Tech_Layoff_Project/main/images/dashboard_preview.png)
*(Screenshot of the final Dashboard showing Actual vs. Predicted Layoffs)*

---

## Phase 4: Critical Reflection
**"Why did the model under-predict the 2025 Spike?"**

In the forecasting phase, my Random Forest model correctly predicted a rising trend in layoffs but underestimated the sheer magnitude of the early 2025 spike (Actual: ~24k vs. Predicted: ~10k).

* **Insight 1 (The "Black Swan" Effect):** The model was trained on historical data (2020-2023). Machine Learning models are inherently conservative when facing unprecedented outliers that exceed historical maximums.
* **Insight 2 (Herd Mentality):** The model relies on quantitative metrics (Interest Rates, Stock Prices). However, the massive spike in 2025 was likely driven by **"Social Contagion"** (Copycat Layoffs)—where profitable companies laid off staff simply to match competitors. This psychological factor is invisible to standard economic models.

**Conclusion:** This demonstrates that while Data Science is powerful for identifying *Trends*, domain knowledge (Economics/Psychology) is essential to explain *Magnitude*.

---

## Key Insights & Findings
* **The "End of Cheap Money" Effect:** Analysis proves a statistically significant correlation between the Fed Funds Rate and layoff intensity. The transition from Zero Interest Rate Policy (ZIRP) to a high-rate environment triggered a pivot from "Growth-at-all-costs" to "Operational Efficiency".
* **Shareholder Pressure Analysis:** Using **Meta Platforms (META)** as a proxy, stock price collapses consistently precede layoff announcements by **3 to 4 months**. This confirms that layoffs are a delayed reaction to shareholder pressure.
* **Sector-Specific Vulnerability:** SQL analysis reveals that **Retail Tech (e-Commerce)** and **Consumer Services** experienced the most aggressive corrections compared to specialized AI infrastructure sectors.

### Technical Skillset
* **Programming:** Python (Pandas, NumPy, Scikit-Learn).
* **Database Management:** SQL (SQLite) for relational data aggregation.
* **Economic Tools:** FRED API (Macro) and `yfinance` (Market Data).
* **BI & Web Deployment:** **Streamlit** (Web Application), **Tableau** (Business BI), and Matplotlib/Seaborn for statistical plotting.

  \*More details are available in the FINAL_REPORT.md file.
---

## Phiên bản Tiếng Việt

### Hồ sơ Chuyên môn
Mình là **Nguyễn Cao Thiên Ân**, hiện là sinh viên quốc tế tại **Viện đại học Wisconsin-Madison** theo đuổi **Song ngành Khoa học Dữ liệu và Kinh tế học**. Với nền tảng kết hợp giữa tư duy định lượng và lý thuyết kinh tế, mình hướng tới mục tiêu trở thành một **Data Scientist, Nhà phân tích Kinh tế hoặc Chuyên viên Nghiên cứu Định lượng (Quant Researcher)**.

Dự án này được mình định hướng là một nghiên cứu điển hình về **Kinh tế học Lao động và Động lực học Thị trường**. Tận dụng môi trường học thuật chuyên sâu tại UW-Madison, mình đã và đang cố gắng tập trung giải mã cách các biến động tài chính toàn cầu chuyển hóa thành các quyết định tái cơ cấu nội bộ trong ngành công nghệ.

### Dashboard Trực tuyến (Hugging Face Spaces)
Để trực quan hóa các kết quả nghiên cứu, mình đã xây dựng một ứng dụng web tương tác bằng **Streamlit**, cho phép người dùng khám phá dữ liệu một cách linh hoạt.

* **Khám phá Thời gian thực:** Lọc dữ liệu sa thải theo năm và theo từng ngành cụ thể để thấy được xu hướng cục bộ.
* **Trực quan hóa Dự báo AI:** Biểu đồ tương tác so sánh dự báo từ mô hình Random Forest với diễn biến thực tế của thị trường.
* **Phân tích Tự động:** Dashboard tự động đưa ra các nhận định (insights) dựa trên khoảng dữ liệu được chọn, đặc biệt là khoảng cách "Herd Mentality".
* **Minh bạch Dữ liệu:** Cung cấp bảng dữ liệu thô ngay trên ứng dụng để người dùng có thể đối soát.

**[Truy cập Dashboard tại đây](https://aansensei-tech-layoff-analytics.hf.space)**

### Kiến trúc Dự án
1.  **Kỹ thuật Dữ liệu:** Tổng hợp dữ liệu từ FRED (Vĩ mô), Yahoo Finance (Chứng khoán) và Layoffs.fyi bằng Python & SQL.
2.  **Phân tích Khám phá (EDA):** Xác định mối tương quan "trễ 3 tháng" giữa sập giá cổ phiếu và sa thải nhân sự.
3.  **Mô hình hóa Dự báo (Giai đoạn 4):** Xây dựng mô hình **Hồi quy Tuyến tính** và **Random Forest** để dự báo xu hướng sa thải.
4.  **Báo cáo Quản trị (Giai đoạn 5):** Thiết kế **Streamlit Web App** và Tableau Dashboard để trực quan hóa khoảng cách giữa "Dự báo và Thực tế".

---

## Giai đoạn 5: Dashboard Report
*Hình ảnh thực tế từ Dashboard, so sánh dữ liệu thực và dự báo của AI.*

![Dashboard Preview](https://raw.githubusercontent.com/aansensei/Tech_Layoff_Project/main/images/dashboard_preview.png)

---

## Giai đoạn 4: Phản biện Mô hình AI (Critical Reflection)
**"Tại sao mô hình lại dự báo thấp hơn thực tế trong đợt cao điểm 2025?"**

Trong giai đoạn dự báo, mô hình Random Forest của mình đã đoán đúng **xu hướng tăng**, nhưng lại đánh giá thấp **cường độ** của đợt sa thải đầu năm 2025 (Thực tế: ~24k so với Dự báo: ~10k).

* **Góc nhìn 1 (Hiệu ứng Thiên nga đen):** Mô hình được huấn luyện trên dữ liệu quá khứ (2020-2023). Các mô hình Machine Learning thường có xu hướng "an toàn" (conservative) khi đối mặt với các giá trị ngoại lai chưa từng xuất hiện trong lịch sử.
* **Góc nhìn 2 (Tâm lý bầy đàn):** Mô hình dựa trên các chỉ số định lượng (Lãi suất, Giá cổ phiếu). Tuy nhiên, đợt bùng nổ năm 2025 có khả năng được thúc đẩy bởi **"Hiệu ứng lây lan xã hội"** (Social Contagion) - nơi các công ty sa thải nhân viên chỉ để chạy theo đối thủ dù tài chính vẫn ổn. Yếu tố tâm lý này là điểm mù của các mô hình kinh tế chuẩn.

**Kết luận:** Khoa học dữ liệu rất mạnh trong việc xác định *Xu hướng*, nhưng kiến thức chuyên ngành (Kinh tế/Tâm lý học) là bắt buộc để giải thích *Quy mô*.

---

### Kết quả Phân tích Nổi bật
* **Hồi kết của kỷ nguyên "Tiền rẻ":** Phân tích chứng minh mối tương quan nghịch rõ rệt giữa Lãi suất Fed và cường độ sa thải. Việc chuyển dịch sang môi trường lãi suất cao đã buộc các doanh nghiệp phải thay đổi chiến lược sang "Tối ưu hóa hiệu quả".
* **Áp lực từ Cổ đông:** Lấy **Meta Platforms (META)** làm đại diện, giá cổ phiếu sụt giảm thường diễn ra trước các thông báo sa thải từ **3 đến 4 tháng**. Điều này xác nhận sa thải là phản ứng có độ trễ nhằm trấn an nhà đầu tư.
* **Phân hóa Ngành:** Truy vấn SQL cho thấy Bán lẻ trực tuyến và Dịch vụ tiêu dùng chịu ảnh hưởng nặng nề nhất, trong khi mảng Cơ sở hạ tầng AI chống chịu tốt hơn.

### Kỹ năng Chuyên ngành
* **Lập trình:** Python (Pandas, NumPy, Scikit-Learn).
* **Cơ sở dữ liệu:** SQL (SQLite).
* **Công cụ Kinh tế:** FRED API và `yfinance`.
* **BI & Triển khai Web:** **Streamlit** (Ứng dụng Web), **Tableau** (Dashboard quản trị) và Matplotlib/Seaborn.

---

## Contact Information
* **Full Name:** Nguyen, Cao Thien An
* **University:** University of Wisconsin-Madison
* **LinkedIn:** [linkedin.com/in/cao-thien-an-nguyen-0a92a4396/](https://www.linkedin.com/in/cao-thien-an-nguyen-0a92a4396/)
* **Major:** Data Science & Economics

  \*Thông tin chi tiết hơn được đề cập ở file FINAL_REPORT.md.
---
*Last Updated: February 2026*
