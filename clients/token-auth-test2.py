import requests


def client():
    data = {"username": 'adminsss',
            "email": "Test@gmail.com",
            "password1": '111111111a',
            "password2": '111111111a'
            }

    response = requests.post("http://127.0.0.1:8000/api/rest-auth/registration/", data=data)

    print("Status code:", response.status_code)
    response_data = response.json()
    print(response_data)

    # tokek_h = "Token 00c7cc5fa41faaf79b724787b38a14f1c2679f09"
    # headers = {"Authorization": tokek_h}
    # response = requests.get('http://127.0.0.1:8000/api/profiles/', headers=headers)
    #
    # print(response.json())


if __name__ == "__main__":
    client()
