FROM python:3.13.3-slim-bullseye

RUN  python -m venv /opt/venv

ENV PATH=/opt/venv/bin:$PATH

RUN pip install --upgrade pip

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


RUN apt-get update && apt-get install -y \
    libpq-dev \
    libjpeg-dev \
    libcairo2 \
    gcc \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /code

WORKDIR /code

COPY requirements.txt /tmp/requirements.txt

COPY ./src /code

RUN pip install -r /tmp/requirements.txt

COPY ./boot/docker-run.sh /opt/run.sh

RUN chmod +x /opt/run.sh

# RUN apt-get remove-purge -y \
#     && apt-get autoremove -y \
#     && apt-get clean \
#     && rm -fr /var/lib/apt/lists/*

CMD ["/opt/run.sh"]