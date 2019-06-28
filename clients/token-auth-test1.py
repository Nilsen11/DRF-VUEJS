import requests


def client():
    # credentials = {"username": 'test', "password": 'dsfdsfdfs'}
    #
    # response = requests.post("http://127.0.0.1:8000/api/rest-auth/login/", data=credentials)
    #
    # print("Status code:", response.status_code)
    # response_data = response.json()
    # print(response_data)

    url = 'http://127.0.0.1:8000/api/status/3/'
    tokek_h = "Token 00c7cc5fa41faaf79b724787b38a14f1c2679f09"

    headers = {"Authorization": tokek_h}
    # response = requests.get('http://127.0.0.1:8000/api/profiles/', headers=headers)

    response = requests.delete(url, headers=headers)
    print(response.status_code)


if __name__ == "__main__":
    client()
