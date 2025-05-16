#!/bin/bash

# cronログファイルが存在しない場合は作成
touch /var/log/cron.log

# cron起動 ＋ ログ出力
service cron start

# Flaskサーバーをバックグラウンドで起動
python /work/app.py &

# URLを更新するスクリプトをバックグラウンドで起動
python /work/update_ngrok.py

# コンテナを維持するために無限ループ
tail -f /dev/null
