FROM python:3.13 AS init 

WORKDIR /app
COPY . .


ENV VIRTUAL_ENV=/app/.venv_docker
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN python -m venv $VIRTUAL_ENV


RUN pip install --upgrade pip
RUN $uv pip install --no-cache-dir -r requirements.txt


CMD ["reflex", "run", "--venv", "prod", "--backend-only"]
