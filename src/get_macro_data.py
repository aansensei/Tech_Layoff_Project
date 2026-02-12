import pandas as pd
from fredapi import Fred
import os


fred = Fred(api_key='555f8c5c9fac92d3c858d9a9926e02f8')

# FEDFUNDS: Lãi suất quỹ liên bang (Interest Rate)
# CPIAUCSL: Chỉ số giá tiêu dùng (Lạm phát - Inflation)
# UNRATE: Tỷ lệ thất nghiệp (Unemployment Rate)
# GDP: Tổng sản phẩm quốc nội
indicators = {
    'FEDFUNDS': 'Interest_Rate',
    'CPIAUCSL': 'Inflation_CPI',
    'UNRATE': 'Unemployment_Rate',
    'GDP': 'GDP'
}


def fetch_macro_data():
    print(" Đang tải dữ liệu từ FRED...")
    all_data = pd.DataFrame()

    for series_id, name in indicators.items():
        try:
            # Lấy dữ liệu từ năm 2018 đến nay
            data = fred.get_series(series_id, observation_start='2018-01-01')
            df = pd.DataFrame(data, columns=[name])

            # Merge vào bảng chung
            if all_data.empty:
                all_data = df
            else:
                all_data = all_data.join(df, how='outer')
            print(f" Đã tải xong: {name}")
        except Exception as e:
            print(f" Lỗi khi tải {name}: {e}")

    # 3. Xử lý dữ liệu
    # Resample về đầu tháng (MS = Month Start) để đồng bộ
    all_data = all_data.resample('MS').first()

    # Forward fill nếu có dữ liệu bị thiếu (đặc biệt là GDP báo cáo theo quý)
    all_data = all_data.ffill()

    return all_data


if __name__ == "__main__":
    os.makedirs('data/raw', exist_ok=True)

    macro_df = fetch_macro_data()

    # Lưu ra file CSV
    output_path = 'data/raw/macro_economics_data.csv'
    macro_df.to_csv(output_path)

    print(f"\n Thành công! Dữ liệu đã được lưu tại: {output_path}")
    print(macro_df.tail())
