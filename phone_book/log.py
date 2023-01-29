import datetime

def log_cash(result):
    with open('log.txt', 'a', encoding='utf-8') as file:
        file.write(f'{result}. Время запроса: {datetime.datetime.now()} \n')