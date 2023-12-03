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

## Day 4: Templates and Static files (Phần 1)

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

## Day 5: Templates and Static files (Phần 2)

- Truy cập templates/challenges.html

```html
<p>Username: {{username}}</p>
<p>Age:{{age}}</p>
```

- views.py

```py

def index(request):

    user = {
        "name": "danny",
        "age": 25
    }

    return render(request, "challenges.html", {
        "username": user['name'],
        "age": user['age']
    })
```

## Day 6: Templates and Static files (Phần 3)

`challenges/views.py`

```py

def index(request):

    months = list(monthly_challenges.keys())

    return render(request, "index.html", {
        'months': months
    })


def monthly_challenges_by_string(request, month):

    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges.html", {
            "challenge_text": challenge_text
        })
    except:
        return HttpResponseNotFound('404 not found!')

```

`challenges/templates/index.html`

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
  </head>
  <body>
    <ul>
      {% for month in months %}
      <li>
        <a href="{% url 'monthly' month %}">{{month}}</a>
      </li>
      {% endfor %}
    </ul>
  </body>
</html>
```

`challenges/templates/challenges.html`

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>This month</title>
  </head>
  <body>
    <h1>This month challenge</h1>
    <p>{{ challenge_text }}</p>
  </body>
</html>

<!-- Django Template language DTL -->
```

## Day 7: Templates and Static files (Phần 4)

`Xử lý lỗi 404 not found khi request đến 1 path không tồn tại trên hệ thống`
`mypage/templates/  tạo thêm 404.html file`

```html
<!DOCTYPE html>
<html>
  <title>Wrong address</title>
  <body>
    <h1>Ooops!</h1>

    <h2>I cannot find the file you requested!</h2>
  </body>
</html>
```

`challenges/views.py`

```py

def monthly_challenges_by_string(request, month):

    except:
        # return HttpResponseNotFound('404 not found!')
        raise Http404('404.html')

```

`Để Django có thể trả về Page 404 cần cấu hình lại trong file settings.py`

```py
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["127.0.0.1"]
```
