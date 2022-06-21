# Request Data from web Hacker News
## Sau khi clone project về:
- Bước 1: Vào folder lib
- Bước 2: Chạy file main.py

*Nếu thiếu thư viện nào thì pip install <tên thư viện>

## Cài đặt nhanh toàn bộ thư viện có trong project
- Anh có thể chạy dòng lệnh này
```
pip install requests beautifulsoup4 tk
```
- Hoặc ở nơi chứa tệp requirements.txt
```
pip install -r requirements.txt
```

## Crawl next page của trang
- Với vấn đề crawl next page em chưa thực hiện trong code. Chương trình hiện tại chỉ có thể thay đổi url để crawl dữ liệu ở các page khác.
- Ý tưởng của em chính là trang đầu tiên của web có url là "https://news.ycombinator.com/news?p=1", trang kế tiếp có url là "https://news.ycombinator.com/news?p=2" nên thực hiện việc ghép chuỗi: string = "https://news.ycombinator.com/news?p" + str(i). Với i là biến số trang (luôn lớn hoặc bằng 1 và có thể tăng hoặc giảm) và sau đó thực hiện requests tiếp dữ liệu tương ứng với url mới.
- Em sẽ thực hiện chức năng crawl next page.
