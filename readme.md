# I. 🎤 Giới thiệu

## 1.1. Giới thiệu chung

  Vnstock là thư viện Python được thiết kế để tải dữ liệu chứng khoán Việt Nam. 
  Vnstock sử dụng các nguồn cấp dữ liệu đáng tin cậy, bao gồm nhưng không giới hạn 
  từ công ty chứng khoán và công ty phân tích thị trường tại Việt Nam. 

pip install vnstock

link github : https://github.com/thinh-vu/vnstock

from vnstock import * #import all functions

# I. Các nhóm hàm tính toán
## 2.1. Liệt kê cổ phiếu niêm yết
listing_companies()
## 2.2. 💴 Phân tích cơ bản
* Thông tin công ty niêm yết  : company_overview('{ ten cong ty (TCB) }')
* Thông tin công ty           : company_profile('TCB')
* Danh sách cổ đông           : company_large_shareholders(symbol='TCB')
* Các chỉ số tài chính cơ bản : company_fundamental_ratio(symbol='TCB', mode='simplify', missing_pct=0.8)
* Mức biến động giá cổ phiếu  : ticker_price_volatility(symbol='TCB')
* Thông tin giao dịch nội bộ  : company_insider_deals(symbol='TCB', page_size=20, page=0)
* Danh sách cty con, cty liên kết : company_subsidiaries_listing(symbol='TCB', page_size=100, page=0)
* Ban lãnh đạo công ty        : company_officers(symbol='TCB', page_size=20, page=0)
* Thông tin sự kiện quyền     : company_events(symbol='TPB', page_size=15, page=0)
* Tin tức công ty             : company_news(symbol='TCB', page_size=15, page=0)
* Lịch sử chi trả cổ tức      : dividend_history("VNM")
* Chỉ số tài chính (TCBS)     : financial_ratio("TCB", 'quarterly', True)

### Báo cáo tài chính
* Income Statement: Báo cáo doanh thu
* Balance Sheet: Bảng cân đối kế toán
* Cashflow: Báo cáo lưu chuyển tiền tệ

**Bổ sung param `get_all` để lấy tất cả báo cáo hoặc 5 năm gần nhất hoặc 10 quý gần nhất**
* financial_flow(symbol="TCB", report_type='incomestatement', report_range='quarterly', get_all=False)
* financial_flow(symbol="TCB", report_type='balancesheet', report_range='quarterly', get_all=False)
* financial_flow(symbol="TCB", report_type='cashflow', report_range='quarterly', get_all=False)

## Định giá
* stock_evaluation (symbol='TCB', period=1, time_window='D')

## 2.3. Phân tích kỹ thuật
### Historical Price : 
* stock_historical_data("GMD", "2021-01-01", "2022-02-25", "1D")
* stock_historical_data("VNINDEX", "2023-06-01", "2023-06-29", "1D", "index")
* stock_historical_data (symbol='VN30F1M', start_date='2023-06-01', end_date='2023-06-17', resolution='1D', type='derivative')

## 2.4. 👓 Stock screening
## Comparison
📊 Price Table
* price_depth('TCB,SSI,VND')
* price_board('TCB,SSI,VND')

🏭 Industry Analysis
* industry_analysis("VNM")

🔬 Stocks List Analysis
* stock_ls_analysis("TCB, BID, CEO, GMD")

## Rating & Evaluation
⭐General Rating
* general_rating("VNM")

🌱 Business Model Rating
* biz_model_rating("VNM")

📑 Financial Health Rating
* financial_health_rating("VNM")

💲 Valuation Rating

* valuation_rating("VNM")

🔎 Stock Filter

* params = {
            "exchangeName": "HOSE,HNX,UPCOM",
            "marketCap": (100, 1000),
            "dividendYield": (5, 10)
        }

# Áp dụng bộ lọc với hàm để lấy kết quả

df = stock_screening_insights (params, size=1700, drop_lang='vi')


2.5. 🧰 Trading Center
🔥 Intraday Trading Data
stock_intraday_data(symbol='GMD', page_size=1000)
