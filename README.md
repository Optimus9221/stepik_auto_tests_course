# stepik_auto_tests_course

Учебный репозиторий с решениями заданий курса по автоматизации тестирования (Selenium WebDriver + Python).

Репозиторий на GitHub: [Optimus9221/stepik_auto_tests_course](https://github.com/Optimus9221/stepik_auto_tests_course)

## О проекте

Здесь хранятся скрипты, которые я пишу на уроках: поиск элементов, формы, dropdown, explicit wait, alert, checkbox/radio и другие темы курса.

Практические страницы курса: [suninjuly.github.io](http://suninjuly.github.io/)

## Структура

```
stepik_auto_tests_course/
├── lessons/                 # Решения по урокам (ls1.x, ls2.x и т.д.)
├── setup-course-venv.sh     # Скрипт настройки виртуального окружения
├── .gitignore
└── README.md
```

Примеры файлов в `lessons/`:

- `ls1.6.*` — базовые задания (локаторы, формы)
- `ls2.*` — продвинутые темы (select, wait, alert и др.)
- `Recention.py`, `Recention_2.py` — повторение/закрепление
- `ls2.1 cheat sheat.py` — шпаргалка по локаторам

## Требования

- Python 3
- Google Chrome
- ChromeDriver (обычно подтягивается через Selenium Manager)

## Быстрый старт

### 1. Клонировать репозиторий

```bash
git clone https://github.com/Optimus9221/stepik_auto_tests_course.git
cd stepik_auto_tests_course
```

### 2. Настроить окружение

Автоматически (Linux):

```bash
chmod +x setup-course-venv.sh
./setup-course-venv.sh
```

Или вручную:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip selenium pytest
```

### 3. Запустить урок

```bash
source .venv/bin/activate
python lessons/ls2.3.py
```

В PyCharm: откройте проект, выберите интерпретатор `.venv`, запустите нужный файл из `lessons/`.

## Что используется в коде

- [Selenium WebDriver](https://www.selenium.dev/documentation/) — автоматизация браузера
- `By` — локаторы (`ID`, `CSS_SELECTOR`, `TAG_NAME`, `LINK_TEXT`, …)
- `Select` — работа с `<select>`
- `WebDriverWait` + `expected_conditions` — явные ожидания
- `pytest` — при необходимости для тестов

Типичная структура скрипта:

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = None
try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/...")
    # действия на странице
finally:
  if browser:
      browser.quit()
```

## Ветки на GitHub

Основная рабочая ветка с домашними заданиями — **`master`**.

При просмотре репозитория на GitHub убедитесь, что выбрана ветка `master` (а не только `main` с начальным README).

## Заметки

- Папка `.venv` и кэши не попадают в Git (см. `.gitignore`).
- Скрипты учебные: часть решений привязана к конкретным страницам курса и может меняться вместе с уроками.

## Автор

[Optimus9221](https://github.com/Optimus9221)
