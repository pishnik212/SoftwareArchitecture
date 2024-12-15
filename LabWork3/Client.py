import requests

BASE_URL = 'http://127.0.0.1:5000'

# Получение всех пользователей пользователей системы
def get_users():
    response = requests.get(f'{BASE_URL}/users')
    return response.json()

# Добавление новой заявки
def add_application(submission_date, status, entrant_id):
    application_data = {
        'submissionDate': submission_date,
        'status': status,
        'entrantId': entrant_id
    }
    response = requests.post(f'{BASE_URL}/applications', json=application_data)
    return response.json()

if __name__ == '__main__':
    print(get_users())
    print(add_application('2023-10-01', 'Pending', 1))
