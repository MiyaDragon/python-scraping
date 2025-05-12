FROM python:3.10-slim

# 必要なパッケージのインストール（cron含む）
RUN apt-get update && apt-get install -y \
    cron \
    procps \
    vim \
    wget \
    sudo \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# 作業ディレクトリ
WORKDIR /work

# Pythonパッケージのインストール
COPY requirements.txt ./
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# 実行スクリプトをコピー
COPY docker/start.sh /start.sh
RUN chmod +x /start.sh

# CMD: start.sh で cron + tail を起動
CMD ["/start.sh"]
