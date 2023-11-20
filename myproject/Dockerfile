# 基于 Python 官方镜像
FROM python:3.12-alpine
# FROM python:3.11-alpine

# 在 Alpine 中安装 GCC 和其他构建依赖
RUN apk add --no-cache gcc musl-dev linux-headers 
# nodejs npm

# 安装 Node.js
# RUN apk add --update nodejs npm

# 设置环境变量
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 设置工作目录
WORKDIR /code

# 安装依赖
COPY requirements.prod.txt /code/
RUN pip install --no-cache-dir -r requirements.prod.txt

COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# 复制项目
COPY . /code/

# 收集静态文件
RUN python manage.py collectstatic --noinput

# 启动 Gunicorn
# CMD ["gunicorn", "-b", "0.0.0.0:8000", "mysite.wsgi:application"]

# 启动 uwsgi
CMD ["uwsgi", "--http", "0.0.0.0:8000", "--module", "mysite.wsgi", "--workers", "4", "--threads", "2"]

# 启动开发服务器
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
