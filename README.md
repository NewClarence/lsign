django + mysql 搭建的注册登录项目
========
首次运行按照如下操作
--------
# 第一步，搭建虚拟开发环境<br>
virtualenv ./env<br>
# 第二步，安装依赖库<br>
source ./env/bin/active<br>
./env/bin/pip install -r requirements.txt<br>
# 第三步，创建数据库<br>
参照如下配置<br>
DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'USER': 'dbuser',
        'PASSWORD': 'a',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}<br>
export LD_LIBRARY_PATH=/opt/mysql/my3306/lib<br>
./manage.py migrate<br>
# 第四步，启动<br>
./manage.py runserver 0.0.0.0:8000<br>
