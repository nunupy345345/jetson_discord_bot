# NVIDIA Jetson用の軽量Pythonベースイメージ
FROM nvcr.io/nvidia/l4t-base:r36.2.0

WORKDIR /app

RUN apt-get update && \
  apt-get install -y python3 python3-pip && \
  pip3 install --no-cache-dir Jetson.GPIO discord.py && \
  apt-get clean && rm -rf /var/lib/apt/lists/*

COPY ./app/bot.py .

CMD ["python3", "bot.py"]
