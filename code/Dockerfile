FROM python:3.9
ADD requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt
WORKDIR /app
COPY . /app
EXPOSE 8501
ENTRYPOINT ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
