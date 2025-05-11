# 📔 Личный дневник

**Личный дневник** — это веб-приложение на Django, которое позволяет пользователям создавать, редактировать и удалять личные заметки. Простой и удобный интерфейс делает его идеальным для повседневного использования, а гибкая архитектура обеспечивает лёгкую масштабируемость.

## 🚀 Функциональность

- Регистрация и авторизация пользователей
- Создание, редактирование и удаление заметок
- Категоризация записей (по дате, тегам и т.д.)
- Поддержка интерфейса удаления с подтверждением
- Адаптивный дизайн (в т.ч. мобильная версия)
- Панель администратора Django
- Защита доступа к заметкам по правам

## 🛠️ Технологии

- **Язык:** Python 3.12+
- **Фреймворк:** Django 4.x
- **Frontend:** Bootstrap 5, HTML/CSS
- **База данных:** SQLite (по умолчанию) / PostgreSQL
- **Docker:** поддержка контейнеризации через Docker Compose

## 🔧 Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/your-username/personal-diary.git
   cd personal-diary
    ```

2. Создайте и активируйте виртуальное окружение:
    ```bash
   python -m venv .venv
   source .venv/bin/activate  # или .venv\Scripts\activate на Windows
    ```
3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
   
4. Проведите миграции и создайте суперпользователя:
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```
5. Запустите сервер:
   ```bash
   python manage.py runserver
   ```
   
## 🐳 Запуск с помощью Docker

Если вы хотите развернуть проект **«Личный дневник»** в контейнере с помощью Docker, выполните следующие шаги:

### ⚙️ Предварительные требования

- Установлен **Docker**
- Установлен **Docker Compose**
- Docker демон запущен (на Windows — убедитесь, что Docker Desktop работает с правами администратора)

### 📦 Сборка и запуск

```bash
docker-compose up --build
```

После сборки приложение будет доступно по адресу:

```
http://localhost:8000
```

### ⚠️ Возможные ошибки и решения

**Ошибка:**
```
the docker client must be run with elevated privileges
```

**Решение:**  
Запустите терминал от имени администратора.

---

**Ошибка:**
```
service "web" depends on undefined service "celery"
```

**Решение:**  
Удалите или закомментируйте строчку `depends_on: - celery` в файле `docker-compose.yml`, если вы не используете Celery.

---

**Ошибка:**
```
error during connect: open //./pipe/docker_engine: The system cannot find the file specified.
```

**Решение:**  
Убедитесь, что Docker Desktop запущен и работает корректно.

### 🛠 Дополнительные команды

Выполнение миграций:
```bash
docker-compose exec web python manage.py migrate
```

Создание суперпользователя:
```bash
docker-compose exec web python manage.py createsuperuser
```

Остановка контейнеров:
```bash
docker-compose down
```
