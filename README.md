# newsCrawler

Step 1: cài python 3 và pip

Step 2: cài django ("pip install django")

Step 3: cài các module cần thiết:
  - pip install djangorestframework-datatables
  - pip install django_ace
  - pip install psycopg2-binary
  - pip install django-login-required-middleware
  - pip install beautifulsoup4
  - pip install validators
  - pip install -U Celery
  - pip install -U django-celery-beat
  - pip install lxml
  - pip install pyyaml
  
Step 4: cài postgres (port 5432), link tham khảo:
- https://stackjava.com/postgresql/huong-dan-cai-dat-va-cau-hinh-postgresql-tren-windows.html
- https://openplanning.net/10713/cai-dat-co-so-du-lieu-postgresql-tren-windows

Có thể pgAdmin4.exe không chạy nhưng chỉ cần postgres đang chạy trên port 5432 là được (check bằng windown button, gõ service, check postgres status, running là được)

Note: khi cài đặt thì nhớ username và password. thay các mục USER và PASSWORD trong file newsCrawler/newsCrawler/setting.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'doimatkhaupostgres',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}


Step 5:
  - mở cmd và cd và thư mục newCrawler
  - chạy python manage.py runserver 8080
  - tao user bằng (chưa tạo trang add user): echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('test', 'admin@myproject.com', 'test')" 
| python manage.py shell
  - mở localhost:8080 để vào dashboard

Test module crawler:
 -cd vào thư mục newsCrawler/newsCrawler
 - trong đó có file doCrawler.py
 -chạy python .\DoCrawler.py trong thư mục crawler_result sẽ có file list_href.txt và các file kết quả crawler nội dung (.txt) (chạy test cho trang vnexpress.net/thoi-su)
