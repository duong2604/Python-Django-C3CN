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

  Thường sử dụng để truyền động dữ liệu trên URL. Đây là một tính năng rất quan trọng trong Django
  Trong file `challenges/urls.py`
  urlpatterns = [
  path('', views.index),
  path('<int:month>', views.monthly_challenges_by_number),
  path('<str:month>', views.monthly_challenges_by_string)
  ]

- Redirects:

  HttpResponseRedirect('')
  Dùng để điều hướng đến một path đã tồn tại. Tham số truyền vào là một đườn dẫn(path) muốn điều hướng đến

## Day 4: Templates and Static files

### Templates

- Truy cập challenges folder, khởi tạo "templates" folder
- Trong "templates" folder, khởi tạo "index.html"
- Trong views.py:

```py
def index(request):
   return render(request, "index.html")

```

- urls.py

```py
path('', views.index)
```

- Truy cập vào mysite/setting.py
  Note: Khai báo app , django sẽ tự động tìm kiếm template file trong các aplication con, điều này giúp chúng ta render được các file html.

````py
# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "challenges"

]```

````
