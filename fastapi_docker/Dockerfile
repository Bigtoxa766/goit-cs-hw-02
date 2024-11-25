# Використовуємо офіційний Python 3.10 образ
FROM python:3.10-slim

# Встановлюємо системні залежності, необхідні для роботи PostgreSQL
RUN apt-get update && apt-get install -y gcc libpq-dev && rm -rf /var/lib/apt/lists/*

# Встановлюємо змінну середовища
ENV APP_HOME /app

# Налаштовуємо робочу директорію всередині контейнера
WORKDIR $APP_HOME

# Копіюємо всі файли проекту в робочу директорію контейнера
COPY . .

# Встановлюємо Python-залежності з файлу requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Вказуємо порт, на якому працюватиме застосунок
EXPOSE 5000

# Вказуємо команду для запуску FastAPI-застосунку через uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]


