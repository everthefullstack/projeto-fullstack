from httpx import Client


URL = "api/v1/auth"

def test_login(client: Client):

    data: dict = {
        "login": "giovanilima",
        "senha": "senha123"
    }
    
    response = client.post(f"{URL}/login", 
                           headers={'Content-Type': 'application/json'},
                           json=data)

    print(response.text)
    assert response.status_code == 200