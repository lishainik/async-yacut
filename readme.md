# YaCut

Учебны сервис сокращения ссылок с веб-интерфейсом на русском, JSON REST API и загрузкой
файлов на Яндекс Диск — с автоматическим сокращением ссылок на скачивание.


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

```
>>> from yacut import db
>>> db.create_all()
>>> exit()
```

## Запуск

flask run

