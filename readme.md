# YaCut

Учебны сервис сокращения ссылок с веб-интерфейсом на русском, JSON REST API и загрузкой
файлов на Яндекс Диск — с автоматическим сокращением ссылок на скачивание.

```
POST /api/id/               {"url": "https://example.com/"}
→ 201  {"url": "...", "short_link": "http://127.0.0.1:5000/aB3xY9"}

GET /api/id/aB3xY9/
→ 200  {"url": "https://example.com/"}
```

---

## Установка


git clone https://github.com/mraksdev/async-yacut.git
cd async-yacut

python3 -m venv venv
source venv/bin/activate                    # Linux / macOS
source venv/scripts/activate                # Windows, Git Bash
.\venv\Scripts\Activate.ps1                 # Windows, PowerShell

python3 -m pip install --upgrade pip
pip install -r requirements.txt

Файл переменной окружения создается по образцу env.example

### Создание базы данных

Таблицы созадются с помощью команд


flask shell

>>> from yacut import db
>>> db.create_all()
>>> exit()

## Запуск

flask run

