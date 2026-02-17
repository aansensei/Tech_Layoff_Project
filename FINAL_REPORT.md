# Final Project Reflection: From Raw Data to Economic Insight
**Author:** Nguyen, Cao Thien An
**Date:** February 15, 2026
**Institution:** University of Wisconsin-Madison

---

## Table of Contents
1.  [Executive Summary: The Discovery Journey](#executive-summary-the-discovery-journey)
2.  [English Version](#english-version)
    * [1. Ideation & Motivation](#1-ideation--motivation)
    * [2. Data Selection Strategy](#2-data-selection-strategy)
    * [3. Methodology & Hypothesis](#3-methodology--hypothesis)
    * [4. Key Results & Critical Findings](#4-key-results--critical-findings)
    * [5. Conclusion](#5-conclusion)
    * [6. Future Directions](#6-future-directions)
3.  [Vietnamese Version](#vietnamese-version)
    * [1. Khởi nguồn Ý tưởng](#1-khởi-nguồn-ý-tưởng-ideation)
    * [2. Chiến lược Chọn Dữ liệu](#2-chiến-lược-chọn-dữ-liệu-data-selection)
    * [3. Phương pháp & Giả định](#3-phương-pháp--giả-định-methodology)
    * [4. Kết quả Nổi bật](#4-kết-quả-nổi-bật-key-results)
    * [5. Kết luận](#5-kết-luận-1)
    * [6. Hướng phát triển](#6-hướng-phát-triển)

---

## Executive Summary: The Discovery Journey
> "I started with a simple hypothesis: Interest rates kill jobs. But the data told a different story."

My investigation went through 3 emotional stages:
1.  **The Assumption:** I believed stock crashes caused immediate layoffs.
    * *Discovery:* Data showed a consistent **3-month lag**.
2.  **The Confusion:** My Rational Model predicted 10k layoffs in 2025, but reality hit 24k.
    * *The Pivot:* I realized Economic Data wasn't enough.
3.  **The Realization:** The missing variable was **Human Psychology** (Herd Mentality).
    * *Result:* I pivoted from a pure technical analysis to a behavioral economics study.

---

## English Version

### 1. Ideation & Motivation
The genesis of this project came from a simple yet troubling observation: In early 2025, despite many tech giants reporting stable profits, thousands of employees were being laid off. As a double major in **Data Science and Economics**, I wanted to investigate whether these layoffs were purely operational necessities or strategic reactions to financial market pressure. I aimed to build a bridge between **Macroeconomic Theory** (The Fed) and **Microeconomic Reality** (The Employee).

### 2. Data Selection Strategy
To build a holistic view, I curated three distinct datasets:
* **Macro Level:** I chose **FRED (Federal Reserve Economic Data)** for Interest Rates and CPI because it is the "gold standard" for economic reliability.
* **Market Level:** I used **Yahoo Finance (yfinance)** to track stock prices of Big Tech companies (MAMAA), serving as a proxy for shareholder sentiment.
* **Labor Level:** I utilized **Layoffs.fyi**, a crowdsourced database, to get granular, company-specific layoff numbers.

![Top Industries](images/top_industries_layoffs.png)
*Figure 1: Sector Vulnerability Analysis (SQL Aggregation). The data reveals that Retail and Consumer sectors—most sensitive to inflation and interest rates—suffered the highest volume of layoffs, validating the connection to macro-economic shifts.*

### 3. Methodology & Hypothesis
My core hypothesis was the **"Lagged Transmission Theory"**: *Economic shocks do not cause immediate layoffs; there is a delay while management assesses the damage.*

* **Hypothesis:** Stock market crashes precede layoffs by exactly one fiscal quarter (3 months).
* **Execution:**
    1.  **Cleaning:** I standardized daily stock data and monthly economic data into a unified time series.
    2.  **Feature Engineering:** This was the most critical step. I created **Lagged Variables (t-1, t-2, t-3)** to test if past stock returns predict future layoffs.
    3.  **Modeling:** I compared Linear Regression vs. **Random Forest** to capture non-linear patterns.

![Perfect Storm Chart](images/advanced_recession_analysis.png)
*Figure 2: "The Perfect Storm" (Dual-Axis Analysis). The blue line represents Meta's stock price, and the grey bars represent layoffs. Visual inspection confirms the hypothesis: a stock crash at month (t) is consistently followed by a layoff spike at month (t+3).*

### 4. Key Results & Critical Findings
* **The "3-Month Rule":** The data confirmed my hypothesis. A statistically significant correlation exists between a stock price drop at month t and a layoff spike at month t+3.
* **Feature Importance:** The Machine Learning model independently validated the economic theory. As shown below, the model ranked "Lagged Stock Returns" and "Interest Rates" as the most critical predictors for layoffs.

![Feature Importance](images/feature_importance.png)
*Figure 3: Random Forest Feature Importance. The model identifies 'Interest Rate' and 'Lagged Returns' as the primary drivers of layoffs, outweighing other factors.*

* **The "Social Contagion" Discovery:** While my Machine Learning model correctly predicted the *rising trend* of layoffs in 2025, it underestimated the *magnitude* (predicting ~10k vs. actual ~24k).
    * *Insight:* This suggests that the 2025 spike was driven by **Herd Mentality**. Companies laid off workers not just for financial reasons, but to mimic competitors.

![Prediction vs Reality](images/model_prediction_comparison.png)
*Figure 4: Forecast vs. Reality. The Green line (ML Prediction) captures the upward trend but fails to reach the peak of the Black line (Actual). This gap represents the "Psychological Factor" or Social Contagion that standard economic models miss.*

### 5. Conclusion
This project has been a **transformative journey** for me as a student exploring the intersection of **numbers and human behavior**. While the **Random Forest model** identified the patterns, the unexplained gap in the **2025 data** helped me ultilize the true power of **social contagion**. It proved that behind every data point lies a story of **collective psychology** that no algorithm can fully capture. This experience has deeply reinforced my belief that **Data Science provides the "What" but Economics provides the "Why"**. Moving forward, I am more inspired than ever to look **beyond the code** to find the heart of every story.

### 6. Future Directions
To further refine this analysis, future iterations of this project should focus on:
* **Sentiment Analysis (NLP):** Integrating news sentiment data (via GDELT or Financial Times APIs) to quantify the "Social Contagion" factor directly.
* **Granular Sector Analysis:** Breaking down layoffs by specific roles (e.g., HR vs. Engineering) to see which departments are leading indicators of recession.

---

## Vietnamese Version

### 1. Khởi nguồn Ý tưởng (Ideation)
Dự án này bắt đầu từ một thắc mắc nhỏ nhoi của cá nhân mình khi quan sát thị trường: Tại sao vào đầu năm 2025, dù nhiều công ty công nghệ vẫn báo lãi, nhưng làn sóng sa thải lại diễn ra ồ ạt?
Là một sinh viên song ngành **Khoa học Dữ liệu và Kinh tế**, mình không muốn chỉ đọc tin tức một cách thụ động. Mình muốn dùng dữ liệu để kiểm chứng xem liệu đây là sự cắt giảm cần thiết hay chỉ là một "nước cờ" để làm đẹp lòng nhà đầu tư. Vì vậy, mình quyết định xây dựng một mô hình để kết nối các chính sách vĩ mô của Fed với số phận của từng nhân viên công nghệ.

### 2. Chiến lược Chọn Dữ liệu (Data Selection)
Để có cái nhìn đa chiều, mình đã chọn lọc 3 nguồn dữ liệu khác nhau:
* **Vĩ mô (Macro):** Mình chọn **FRED** (Dữ liệu Kinh tế Liên bang) cho Lãi suất và Lạm phát. Đây là nguồn chính thống và đáng tin cậy nhất.
* **Thị trường (Market):** Mình dùng thư viện `yfinance` để lấy giá cổ phiếu các ông lớn (Big Tech). Mình coi giá cổ phiếu là "nhiệt kế" đo tâm trạng của cổ đông.
* **Lao động (Labor):** Mình chọn **Layoffs.fyi** thay vì số liệu chính phủ, vì nó chi tiết đến từng công ty.

![Phân loại ngành](images/top_industries_layoffs.png)
*Hình 1: Phân tích mức độ tổn thương theo ngành (SQL). Dữ liệu cho thấy ngành Bán lẻ và Tiêu dùng - những ngành nhạy cảm nhất với lạm phát và lãi suất - chịu thiệt hại nặng nề nhất, chứng minh mối liên hệ vĩ mô.*

### 3. Phương pháp & Giả định (Methodology)
Giả định cốt lõi của mình là **"Lý thuyết Truyền dẫn có Độ trễ"**: *Cú sốc kinh tế không gây ra sa thải ngay lập tức, mà cần thời gian để ngấm.*

* **Giả định:** Khi cổ phiếu sập, các CEO sẽ mất khoảng một quý (3 tháng) để ra quyết định sa thải.
* **Thực thi:**
    1.  **Làm sạch:** Đồng bộ hóa dữ liệu chứng khoán (ngày) và vĩ mô (tháng).
    2.  **Kỹ thuật đặc trưng:** Tạo các **Biến trễ (Lagged Variables)** lùi lại 1, 2, và 3 tháng.
    3.  **Mô hình hóa:** So sánh Random Forest (phi tuyến tính) với Hồi quy tuyến tính.

![Biểu đồ Perfect Storm](images/advanced_recession_analysis.png)
*Hình 2: "Cơn bão hoàn hảo" (Phân tích trục kép). Đường màu xanh là giá cổ phiếu Meta, cột màu xám là số lượng sa thải. Biểu đồ xác nhận giả định: Cổ phiếu sập ở tháng (t) luôn kéo theo sa thải tăng vọt ở tháng (t+3).*

### 4. Kết quả Nổi bật (Key Results)
* **Quy luật 3 Tháng:** Dữ liệu đã chứng minh giả định của mình là đúng. Có một mối tương quan chặt chẽ giữa việc giá cổ phiếu giảm ở tháng t và lượng sa thải tăng vọt ở tháng t+3.
* **Yếu tố quan trọng:** Mô hình Machine Learning cũng xác nhận lý thuyết kinh tế này. Như hình dưới, mô hình xếp hạng "Lãi suất" và "Lợi nhuận cổ phiếu quá khứ" là những yếu tố dự báo quan trọng nhất.

![Độ quan trọng của biến](images/feature_importance.png)
*Hình 3: Mức độ quan trọng của các biến trong mô hình Random Forest. Mô hình xác định 'Lãi suất' và 'Biến động cổ phiếu' là động lực chính gây ra sa thải.*

* **Phát hiện về "Lây lan Xã hội":** Một điều thú vị là mô hình Machine Learning của mình dự đoán đúng *xu hướng tăng* của năm 2025, nhưng lại đoán sai về *độ lớn* (Dự báo ~10k người, nhưng thực tế lên tới ~24k).
    * *Bài học:* Điều này cho thấy đợt sa thải 2025 mang nặng tính **Tâm lý bầy đàn**. Các công ty sa thải vì "thấy đối thủ làm vậy", chứ không hẳn vì khó khăn tài chính.

![Dự báo vs Thực tế](images/model_prediction_comparison.png)
*Hình 4: So sánh Dự báo vs Thực tế. Đường màu xanh (Dự báo ML) bắt được xu hướng tăng nhưng thấp hơn đỉnh thực tế (Đường đen). Khoảng cách này đại diện cho "Yếu tố tâm lý" (Social Contagion) mà mô hình kinh tế thuần túy đã bỏ sót.*

### 5. Kết luận
Dự án này đóng vai trò như là một **hành trình thay đổi tư duy** đối với mình khi tìm hiểu về sự giao thoa giữa **những con số và hành vi con người**. Dù **mô hình Random Forest** đã tìm ra các quy luật, nhưng khoảng trống không thể lý giải được trong **dữ liệu năm 2025** lại giúp mình phát huy sức mạnh của **sự lây lan xã hội**. Điều này chứng minh rằng đằng sau mỗi điểm dữ liệu là một câu chuyện về **tâm lý tập thể** mà không thuật toán nào có thể nắm bắt trọn vẹn được. Trải nghiệm này đã củng cố niềm tin trong mình rằng **Khoa học dữ liệu cho ta biết "Cái gì" nhưng Kinh tế học mới giải thích được "Tại sao"**. Vì vậy, từ đây, mình đã được truyền cảm hứng mạnh mẽ để **tiến xa hơn những dòng code thông thường** để đi tìm linh hồn và cội nguồn của mọi câu chuyện.

### 6. Hướng phát triển
Để hoàn thiện nghiên cứu này, các bước phát triển tiếp theo sẽ nên tập trung vào:
* **Phân tích Cảm xúc (NLP):** Tích hợp dữ liệu tin tức (thông qua GDELT hoặc Financial Times API) để định lượng trực tiếp yếu tố "Lây lan xã hội".
* **Phân tích sâu theo vai trò:** Phân loại sa thải theo vị trí cụ thể (ví dụ: Nhân sự vs Kỹ sư) để xem bộ phận nào là chỉ báo sớm của suy thoái.

---
Nguyen Cao Thien An | Data Science & Economics | University of Wisconsin-Madison