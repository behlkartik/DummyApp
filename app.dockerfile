FROM python:3.10

WORKDIR /app

RUN mkdir -p /app/blog

COPY ./blog ./blog

ENV FLASK_APP=./blog/app.py
ENV FLASK_DEBUG=true
ENV PYTHONPATH=.
ENV VIRTUAL_ENV=/opt/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"


RUN python3 -m venv $VIRTUAL_ENV \
    && pip install -r /app/blog/requirements.txt

EXPOSE 3000

CMD flask run -h 0.0.0.0 -p 3000
