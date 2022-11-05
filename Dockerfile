FROM python:3
COPY . /pythonMessenger
WORKDIR /pythonMessenger

EXPOSE 8001

RUN pip install selenium

CMD [ "python", "/pythonMessenger/test.py" ]