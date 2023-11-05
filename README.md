# CN-C3-Django-Python

# Day 1: Cấu hình môi trường và khởi tạo dự án với Django & Python

- Cài đặt Python
- Cài đặt Django
- Start project

-- command:

- django server: `django-admin startproject mysite`
- create application: `python manage.py startapp challenges`
- run server: `python manage.py runserver` // mặc định chạy trên port 8000
  Note: Để chạy trên port khác: `python manage.py runserver :port`

# Day 2: URLs and Views

URL: https://github.com/duong2604/Teky_CN_C3_Django_HP9

- Giao thức protocol: http, https, FTP
- Domain: github.com
- Path(đường dẫn): /duong2604/CNC2-Django-Python
  path đĩnh nghĩa nơi để lấy dữ liệu

View:

- Class( cover sau tại kì 10)
- Function : function view là một hàm để xử lý các yêu cầu khi có một request đến server và gửi trả về response
  Note: Dữ liệu sẽ đi từ path --> view. Mỗi view(function) sẽ xử lí request cho từng path riềng

ví dụ:
http://shopping.com -> Trang chủ shopping.com

http://shopping.com/products -> Đi vào trang sản phẩm, hiển thị tất cả sản phẩm

http://shopping.com/products/idProduct -> Trang chi tiết sản phẩm

# Day 3: URls and Views - Phần 2

- Dynamic segment:
