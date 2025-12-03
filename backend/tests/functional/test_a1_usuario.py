from httpx import Client


URL = "api/v1/usuario"

def test_insert_usuario(client: Client, token: str):

    data: dict = {
        "usuario": "giovanilima",
        "email": "giovani.lima@example.com",
        "senha": "senha123"}
    
    response = client.post(f"{URL}/", 
                           headers={'Content-Type': 'application/json',
                                    "Authorization": f"Bearer {token}"},
                           json=data)

    assert response.status_code == 202