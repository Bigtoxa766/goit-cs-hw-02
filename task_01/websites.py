import requests
from datetime import datetime

websites = [
    "https://www.google.com",
    "https://www.facebook.com",
    "https://www.example.com",
    "https://www.nonexistentwebsite123.com"
]

log_file = "website_check.log"

def log_message(message):
    with open(log_file, 'a') as file:
        file.write(f"{datetime.now()} - {message}\n")

def check_website_availability(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return f"Сайт {url} доступний (HTTP статус-код: {response.status_code})."
        else:
            return f"⚠️ Сайт {url} відповів з кодом {response.status_code}."
    except requests.exceptions.RequestException as e:
        return f"❌ Сайт {url} недоступний. Помилка: {e}"

if __name__ == "__main__":
    for site in websites:
        result = check_website_availability(site)
        log = log_message(result)

        print(result)
        print("-" * 60)
