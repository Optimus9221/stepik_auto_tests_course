#!/usr/bin/env bash
# Настройка venv для курса Selenium
set -euo pipefail

cd "$(dirname "$0")"

echo "=== 1. Пакеты для venv (нужен sudo) ==="
sudo apt-get update
sudo apt-get install -y python3-venv python3-pip python-is-python3

echo ""
echo "=== 2. Удалить сломанный .venv (если был) ==="
rm -rf .venv

echo ""
echo "=== 3. Создать venv ==="
python3 -m venv .venv

echo ""
echo "=== 4. Установить selenium в venv ==="
source .venv/bin/activate
python --version
pip install -U pip selenium pytest

echo ""
echo "=== Готово ==="
echo "Каждый раз перед работой:"
echo "  cd ~/courses/selenium-course"
echo "  source .venv/bin/activate"
echo "  python main.py"
