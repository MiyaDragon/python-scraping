#!/bin/bash

# cronログファイルが存在しない場合は作成
touch /var/log/cron.log

# cron起動 ＋ ログ出力
service cron start

# 永続的にログを監視（コンテナ維持のため）
tail -f /var/log/cron.log
