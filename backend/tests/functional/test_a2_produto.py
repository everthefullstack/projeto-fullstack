from httpx import Client


URL = "api/v1/produto"

def test_insert_produto(client: Client, token: str):

    data: dict = {
        "nome": "corsa",
        "marca": "chevrolet",
        "valor": 20000.00
    }
    
    response = client.post(f"{URL}/", 
                           headers={'Content-Type': 'application/json',
                                    "Authorization": f"Bearer {token}"},
                           json=data)

    assert response.status_code == 202

def test_update_produto(client: Client, token: str):

    data: dict = {
        "id": "fcc7cadc-2bf3-4e7f-9d0f-72b370ccfea9",
        "nome": "corsa",
        "marca": "chevrolet",
        "valor": 25000.00
    }
    
    response = client.put(f"{URL}/", 
                          headers={'Content-Type': 'application/json',
                                   "Authorization": f"Bearer {token}"},
                          json=data)

    assert response.status_code == 202

def test_get_produtos(client: Client, token: str):

    response = client.get(f"{URL}/", 
                          headers={'Content-Type': 'application/json',
                                   "Authorization": f"Bearer {token}"})

    assert response.status_code == 200

def test_delete_produto(client: Client, token: str):

    produto_id = "2040ffdd-e86d-485d-a671-991ce6f610d1"
    
    response = client.delete(f"{URL}/{produto_id}", 
                             headers={'Content-Type': 'application/json',
                                      "Authorization": f"Bearer {token}"})
    
    assert response.status_code == 202