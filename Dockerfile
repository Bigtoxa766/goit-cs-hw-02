# Вказуємо базовий образ, який буде використаний для створення контейнера
FROM python:3.10-slim

# Встановлюємо робочу директорію всередині контейнера
WORKDIR /app

# Копіюємо файл requirements.txt в контейнер
COPY requirements.txt .

# Встановлюємо залежності з requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Копіюємо весь вміст проєкту в контейнер
COPY . /app

# Оскільки застосунок працює на порту 8000, відкриваємо його
EXPOSE 8000

# Вказуємо команду для запуску FastAPI через Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
