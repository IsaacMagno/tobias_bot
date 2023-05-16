FROM python:3.10
WORKDIR /bot
COPY requirements.txt /bot/
RUN pip install -r requirements.txt
RUN  apt-get -y update && apt-get install -y ffmpeg 
COPY . /bot
CMD python tobias_bot.py