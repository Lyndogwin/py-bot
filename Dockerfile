FROM python:3
WORKDIR /usr/src/app
RUN python3 -m pip install -U discord.py[voice]
COPY . .
CMD ["python","__main__.py"]