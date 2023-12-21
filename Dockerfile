# 使用官方 Python 基础镜像
FROM python:3.9.6

# 设置工作目录
WORKDIR /app

# 将当前目录内容复制到位于 /app 的容器中
COPY . /app

# 安装依赖
RUN pip install -r requirements.txt

# 使得 8501 端口在容器外部可用
EXPOSE 8501


# 运行 Streamlit 应用
CMD ["streamlit", "run", "app.py"]

