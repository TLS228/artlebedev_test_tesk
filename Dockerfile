# Базовый образ
FROM python:3.9

# Установка зависимостей системы
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Рабочая директория
WORKDIR /app

# Копируем файлы
COPY . .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Даём права скрипту запуска
RUN chmod +x entrypoint.sh

# Старт
ENTRYPOINT ["./entrypoint.sh"]