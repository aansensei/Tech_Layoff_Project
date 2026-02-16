# Final Project Reflection: From Raw Data to Economic Insight
**Author:** Nguyen, Cao Thien An  
**Date:** February 15, 2026  
**Institution:** University of Wisconsin-Madison  

---

## 🇬🇧 English Version

### 1. Ideation & Motivation
The genesis of this project came from a simple yet troubling observation: In early 2025, despite many tech giants reporting stable profits, thousands of employees were being laid off. As a double major in **Data Science and Economics**, I wanted to investigate whether these layoffs were purely operational necessities or strategic reactions to financial market pressure. I aimed to build a bridge between **Macroeconomic Theory** (The Fed) and **Microeconomic Reality** (The Employee).

### 2. Data Selection Strategy
To build a holistic view, I curated three distinct datasets:
* **Macro Level:** I chose **FRED (Federal Reserve Economic Data)** for Interest Rates and CPI because it is the "gold standard" for economic reliability.
* **Market Level:** I used **Yahoo Finance (`yfinance`)** to track stock prices of Big Tech companies (MAMAA), serving as a proxy for shareholder sentiment.
* **Labor Level:** I utilized **Layoffs.fyi**, a crowdsourced database, to get granular, company-specific layoff numbers that official government statistics often aggregate too broadly.

### 3. Methodology & Quantitative Hypotheses
My core approach relied on the **"Lagged Transmission Theory"**. I didn't just look for connections; I established specific numerical hypotheses before running the models:

* **Hypothesis 1 (The Time Lag):** I hypothesized that the correlation between Stock Returns at $(t-3)$ and Layoffs at $(t)$ would be **strongly negative (r < -0.5)**, significantly stronger than the immediate correlation at $(t-0)$.
* **Hypothesis 2 (The Interest Rate Trigger):** I expected a threshold effect, where layoffs would only spike exponentially once the Federal Funds Rate crossed the **4.0% mark**, signalling the end of "Cheap Money."

### 4. Key Findings & Data Evidence
* **The "3-Month Rule" Confirmed:** The data analysis validated my hypothesis. The correlation coefficient for the **3-month lag** was significantly stronger than the current-month correlation. This confirms that management takes roughly one fiscal quarter to execute workforce reductions after a stock crash.
* **Sector Vulnerability:** SQL analysis revealed a sharp divergence. **Retail Tech (E-commerce)** and **Consumer Services** were hit the hardest, correlating directly with inflation spikes.
* **The "Pivot to Efficiency":** The transition from Zero Interest Rate Policy (ZIRP) to high rates (5%+) caused a fundamental shift in corporate strategy from "Growth-at-all-costs" to "Profitability per Employee."

### 5. Surprising Discoveries (The "Aha!" Moments)
* **The "AI Shield":** While general tech layoffs were rampant, data showed that sectors related to **AI Infrastructure** were remarkably resilient. This suggests a capital reallocation: firing in legacy divisions to hire in AI divisions.
* **The "Social Contagion" & Model Error:** My Random Forest model correctly predicted the *rising trend* of 2025 layoffs but underestimated the *magnitude* (Prediction: ~10k vs. Actual: ~24k).
    * *Insight:* This 14k gap is likely the "Psychological Multiplier." Companies laid off workers not just for financial reasons, but to mimic competitors (Herd Mentality)—a behavioral factor that my rational economic model could not capture.

### 6. Conclusion
This project taught me that **Data Science provides the "What", but Economics provides the "Why".** The ability to code a Random Forest model is valuable, but the ability to interpret *why* it failed (due to psychological herd behavior) is what differentiates a Data Scientist from a coder.

---

## 🇻🇳 Phiên bản Tiếng Việt

### 1. Khởi nguồn Ý tưởng (Ideation)
Dự án này bắt đầu từ một thắc mắc cá nhân của mình khi quan sát thị trường: Tại sao vào đầu năm 2025, dù nhiều công ty công nghệ vẫn báo lãi, nhưng làn sóng sa thải lại diễn ra ồ ạt?
Là một sinh viên song ngành **Khoa học Dữ liệu và Kinh tế**, mình không muốn chỉ đọc tin tức thụ động. Mình muốn dùng dữ liệu để kiểm chứng xem liệu đây là sự cắt giảm cần thiết hay chỉ là một "nước cờ" để làm đẹp lòng nhà đầu tư. Mình quyết định xây dựng một mô hình để kết nối các chính sách vĩ mô của Fed với số phận của từng nhân viên công nghệ.

### 2. Chiến lược Chọn Dữ liệu (Data Selection)
Để có cái nhìn đa chiều, mình đã chọn lọc 3 nguồn dữ liệu khác nhau:
* **Vĩ mô (Macro):** Mình chọn **FRED** (Dữ liệu Kinh tế Liên bang) cho Lãi suất và Lạm phát. Đây là nguồn chính thống và đáng tin cậy nhất.
* **Thị trường (Market):** Mình dùng thư viện `yfinance` để lấy giá cổ phiếu các ông lớn (Big Tech). Mình coi giá cổ phiếu là "nhiệt kế" đo tâm trạng của cổ đông.
* **Lao động (Labor):** Mình chọn **Layoffs.fyi** thay vì số liệu chính phủ, vì nó chi tiết đến từng công ty và cập nhật theo thời gian thực.

### 3. Phương pháp & Các Giả thuyết Định lượng
Phương pháp cốt lõi của mình dựa trên **"Lý thuyết Truyền dẫn có Độ trễ"**. Mình không chỉ tìm kiếm mối liên hệ chung chung, mà đặt ra các giả thuyết con số cụ thể trước khi chạy mô hình:

* **Giả thuyết 1 (Độ trễ thời gian):** Mình dự đoán hệ số tương quan giữa Giá cổ phiếu tháng $(t-3)$ và Sa thải tháng $(t)$ sẽ là **âm mạnh (r < -0.5)**, mạnh hơn nhiều so với tương quan tức thời tại tháng hiện tại $(t-0)$.
* **Giả thuyết 2 (Ngưỡng Lãi suất):** Mình kỳ vọng sẽ có một "hiệu ứng ngưỡng", nơi sa thải chỉ thực sự bùng nổ theo cấp số nhân khi Lãi suất Fed vượt qua mốc **4.0%**, đánh dấu sự kết thúc của kỷ nguyên "Tiền rẻ".

### 4. Kết quả Nổi bật & Bằng chứng Số liệu
* **Quy luật 3 Tháng:** Dữ liệu đã chứng minh giả thuyết của mình là đúng. Tương quan ở độ trễ **3 tháng** mạnh hơn hẳn so với hiện tại. Điều này xác nhận rằng ban lãnh đạo thường mất khoảng một quý tài chính để thực thi cắt giảm nhân sự sau khi cổ phiếu sập.
* **Sự tổn thương theo Ngành:** Phân tích SQL cho thấy sự phân hóa rõ rệt. Các ngành **Bán lẻ Công nghệ (E-commerce)** và **Dịch vụ Tiêu dùng** bị ảnh hưởng nặng nề nhất, tỷ lệ thuận với sự tăng vọt của lạm phát.
* **Chuyển dịch sang "Hiệu quả":** Việc chuyển từ chính sách Lãi suất bằng 0 (ZIRP) sang lãi suất cao (5%+) đã buộc các công ty thay đổi chiến lược từ "Tăng trưởng bằng mọi giá" sang "Tối ưu hóa lợi nhuận trên đầu người".

### 5. Những Phát hiện Bất ngờ (Surprising Discoveries)
* **Hiệu ứng "Lá chắn AI":** Trong khi sa thải diễn ra khắp nơi, dữ liệu cho thấy các mảng liên quan đến **Cơ sở hạ tầng AI** lại trụ vững đáng ngạc nhiên. Điều này gợi ý sự tái phân bổ dòng vốn: sa thải ở các mảng cũ để dồn tiền tuyển dụng cho mảng AI.
* **"Lây lan Xã hội" & Sai số Mô hình:** Mô hình AI của mình dự đoán đúng *xu hướng tăng* của năm 2025, nhưng lại đoán sai về *độ lớn* (Dự báo ~10k người, nhưng thực tế lên tới ~24k).
    * *Bài học:* Khoảng chênh lệch 14k này chính là "Hệ số nhân Tâm lý". Các công ty sa thải vì "thấy đối thủ làm vậy" (Tâm lý bầy đàn) - một yếu tố hành vi mà mô hình kinh tế lý trí của mình đã không nắm bắt được.

### 6. Kết luận
Qua dự án này, mình nhận ra rằng: **Khoa học Dữ liệu cho ta biết "Cái gì đang xảy ra", nhưng Kinh tế học giúp ta hiểu "Tại sao nó xảy ra".**
Việc viết được code chạy mô hình Random Forest là kỹ năng kỹ thuật, nhưng việc hiểu được *tại sao mô hình thất bại* (do yếu tố tâm lý đám đông) mới là tư duy thực sự của một người làm dữ liệu.

---
*Nguyen, Cao Thien An* *Data Science & Economics* *University of Wisconsin-Madison*