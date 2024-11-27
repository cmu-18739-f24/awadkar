FROM ubuntu@sha256:626ffe58f6e7566e00254b638eb7e0f3b11d4da9675088f4781a50ae288f3322 AS base

RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    python3 \
    socat \
    pip

RUN mkdir /challenge

COPY app.py database.py requirements.txt setup_db.py setup-challenge.py /app/

RUN echo '#!/bin/bash\n\
python3 /app/app.py\
' > /app/start.sh && chmod +x /app/start.sh

WORKDIR /app

FROM base AS challenge
ARG FLAG

RUN python3 setup-challenge.py
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000
# PUBLISH 5000 AS port

# Run the database setup script
RUN python3 setup_db.py

CMD ["/bin/bash", "/app/start.sh"]