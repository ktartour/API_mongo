FROM python:3.12-alpine
ENV PYTHONUNBUFFERED=1

ENV APPDIR="/usr/src"
WORKDIR $APPDIR

# Install the app dependencies
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY . $APPDIR

# Run server in production mode
EXPOSE 8000
CMD ["fastapi", "run", "main.py", "--port", "8000"]