import pandas as pd
from fredapi import Fred
import os

# Initialize FRED API with the key
fred = Fred(api_key='555f8c5c9fac92d3c858d9a9926e02f8')

# --- DEFINING INDICATORS (Các chỉ số kinh tế) ---
# FEDFUNDS: Federal Funds Rate (Lãi suất)
# CPIAUCSL: Consumer Price Index (Lạm phát - Inflation)
# UNRATE: Unemployment Rate (Tỷ lệ thất nghiệp)
# GDP: Gross Domestic Product (Tổng sản phẩm quốc nội)
indicators = {
    'FEDFUNDS': 'Interest_Rate',
    'CPIAUCSL': 'Inflation_CPI',
    'UNRATE': 'Unemployment_Rate',
    'GDP': 'GDP'
}


def fetch_macro_data():
    print(" Downloading data from FRED...")
    all_data = pd.DataFrame()

    for series_id, name in indicators.items():
        try:
            # 1. Fetch data from 2018 to present
            # (Lấy dữ liệu từ 2018 đến nay)
            data = fred.get_series(series_id, observation_start='2018-01-01')
            df = pd.DataFrame(data, columns=[name])

            # 2. Merge specific data into the main dataframe
            # (Gộp vào bảng dữ liệu chung)
            if all_data.empty:
                all_data = df
            else:
                all_data = all_data.join(df, how='outer')

            print(f" Finished downloading: {name}")
        except Exception as e:
            print(f" Error downloading {name}: {e}")

    # 3. Data Processing (Xử lý dữ liệu)

    # Resample to Month Start (MS) to synchronize all dates
    # (Đưa tất cả về ngày đầu tháng để khớp thời gian với nhau)
    all_data = all_data.resample('MS').first()

    # Forward fill missing values (Important for GDP because it's reported quarterly, not monthly)
    # (Lấp đầy dữ liệu bị thiếu bằng giá trị tháng trước - đặc biệt cần cho GDP vì nó báo cáo theo quý)
    all_data = all_data.ffill()

    return all_data


if __name__ == "__main__":
    # Create directory if it doesn't exist
    os.makedirs('data/raw', exist_ok=True)

    macro_df = fetch_macro_data()

    # Save to CSV file
    # (Lưu kết quả ra file CSV)
    output_path = 'data/raw/macro_economics_data.csv'
    macro_df.to_csv(output_path)

    print(f"\n Success! Data saved at: {output_path}")
    print(macro_df.tail())
