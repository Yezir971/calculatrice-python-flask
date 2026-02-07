# from app.api import add
import pytest
import requests
from app.database import Database

from app import create_app
@pytest.fixture
def client():
    # On crée l'app avec une config de test
    app = create_app()
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:" # Si tu utilises SQLAlchemy
    })
    
    with app.test_client() as client:
        # Ici, tu peux ajouter un appel pour créer tes tables SQL
        yield client
URL_BASE = "http://127.0.0.1:5000/api"

# test success 
def test_route_test():
    response = requests.get(URL_BASE + '/test')
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert "status" in data
    assert data['status'] == "API fonctionne correctement"
def test_add():
    response = requests.get( URL_BASE + "/add/2/3") 
    assert response.status_code == 200
    data = response.json()  
    assert isinstance(data, dict)
    assert "result" in data
    assert data['result'] == 5.0
    
def test_soustract():
    response = requests.get( URL_BASE + "/subtract/2/3") 
    assert response.status_code == 200
    data = response.json()  
    assert isinstance(data, dict)
    assert "result" in data
    assert data['result'] == -1 

def test_multipli():
    response = requests.get( URL_BASE + "/multiply/2/3") 
    assert response.status_code == 200
    data = response.json()  
    assert isinstance(data, dict)
    assert "result" in data
    assert data['result'] == 6
    
def test_divid():
    response = requests.get( URL_BASE + "/divide/6/3") 
    assert response.status_code == 200
    data = response.json()  
    assert isinstance(data, dict)
    assert "result" in data
    assert data['result'] == 2
# test success 
    
    
# test error  
     
def test_add_error():
    response = requests.get( URL_BASE + "/add/a/3") 
    assert response.status_code == 400
    data = response.json()  
    assert isinstance(data, dict)
    assert "error" in data
    assert data['error'] == "Les paramètres doivent être des nombres"
    
def test_soustract_error():
    response = requests.get( URL_BASE + "/subtract/a/3") 
    assert response.status_code == 400
    data = response.json()  
    assert isinstance(data, dict)
    assert "error" in data
    assert data['error'] == "Les paramètres doivent être des nombres"
    
def test_soustract_error():
    response = requests.get( URL_BASE + "/subtract/a/3") 
    assert response.status_code == 400
    data = response.json()  
    assert isinstance(data, dict)
    assert "error" in data
    assert data['error'] == "Les paramètres doivent être des nombres"
    
def test_multipli_error():
    response = requests.get( URL_BASE + "/multiply/a/3") 
    assert response.status_code == 400
    data = response.json()  
    assert isinstance(data, dict)
    assert "error" in data
    assert data['error'] == "Les paramètres doivent être des nombres"
    
def test_divide_error():
    response = requests.get( URL_BASE + "/divide/a/3") 
    assert response.status_code == 400
    data = response.json()  
    assert isinstance(data, dict)
    assert "error" in data
    assert data['error'] == "Les paramètres doivent être des nombres"
    
def test_divide_by_zero_error():
    response = requests.get( URL_BASE + "/divide/1/0") 
    assert response.status_code == 400
    data = response.json()  
    assert isinstance(data, dict)
    assert "error" in data
    assert data['error'] == "Division par zéro impossible"
    

# partie test user 
def test_add_user_empty_email(client):
    user_data = {
        "username": "ds"
        
    }
    response = client.post( URL_BASE + "/user", json=user_data) 
    assert response.status_code == 400
    assert response.json["error"] == "Les champs username et email sont requis"

    

def test_add_user(client):
    user_data = {
        "username": "test_user6", 
        "email": "user@example.com"
    }
    response = client.post( URL_BASE + "/user", json=user_data) 
    assert response.status_code == 201



def test_add_same_user(client):
    user_data = {
        "username": "test_user6",
        "email":"user@exemple.com"
    }
    response = client.post(URL_BASE + "/user",  json=user_data)
    assert response.status_code == 409
    assert response.json["error"] == "Cet utilisateur existe déjà"

def test_get_user(client):
    response = client.get(URL_BASE + '/user/test_user6')
    assert response.status_code == 200
    
# partie mock 
def test_get_user_mock(client, mocker):
    fake_user = { 'username': 'test_user6', 'email': 'test@example.com'}
    mock_db = mocker.patch('app.api.db.get_user')
    mock_db.return_value = fake_user
    response = client.get(URL_BASE + '/user/test_user6')
    assert response.status_code == 200
    assert response.get_json() == fake_user
    
def test_get_user_john_doe(client):
    response = client.get(URL_BASE + '/user/charly-le-boss')
    assert response.status_code == 404
    assert response.json["error"] == 'Utilisateur non trouvé'
    
def test_delete_user(client):
    response = client.delete(URL_BASE + '/user/test_user6')
    assert response.status_code == 200
    assert response.json["message"] == "Utilisateur supprimé avec succès" 
    
def test_delete_user_john_doe(client):
    response = client.delete(URL_BASE + '/user/test_user6')
    assert response.status_code == 404
    assert response.json["error"] == "Utilisateur non trouvé" 