# Используем официальный образ Python
FROM python:3.12

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем зависимости
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальной код проекта
COPY . .

# Выполняем миграции (опционально — можно вызывать через docker-compose отдельно)
# RUN python manage.py migrate

# Открываем порт (по умолчанию Django использует 8000)
EXPOSE 8000

# Команда запуска приложения
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]