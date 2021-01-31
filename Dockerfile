FROM python:3.8

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP=tlchallenge/app.py
ENV FLASK_ENV=development

EXPOSE 5000
CMD [ "flask", "run", "--host", "0.0.0.0"]
