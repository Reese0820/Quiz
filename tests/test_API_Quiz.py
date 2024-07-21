import pytest
from API_Quiz import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_success(client):
    response = client.post('/api/orders', json={
        'id': 'A0000001',
        'name': 'Melody Holiday Inn',
        'address': {
            'city': 'taipei-city',
            'district': 'da-an-district',
            'street': 'fuxing-south-road'
        },
        'price': '1500',
        'currency': 'TWD'
    })
    assert response.status_code == 200
    assert response.json['id'] == 'A0000001'
    assert response.json['name'] == 'Melody Holiday Inn'
    assert response.json['price'] == 1500.0
    assert response.json['currency'] == 'TWD'

def test_name_not_in_english_failure(client):
    response = client.post('/api/orders', json={
        'id': 'A0000002',
        'name': 'melody holiday inn@',
        'address': {
            'city': 'taipei-city',
            'district': 'da-an-district',
            'street': 'fuxing-south-road'
        },
        'price': '1500',
        'currency': 'TWD'
    })
    assert response.status_code == 400
    assert 'Name contains non-English characters' in response.json['error']

def test_name_not_capitalized_failure(client):
    response = client.post('/api/orders', json={
        'id': 'A0000002',
        'name': 'melody holiday inn',
        'address': {
            'city': 'taipei-city',
            'district': 'da-an-district',
            'street': 'fuxing-south-road'
        },
        'price': '1500',
        'currency': 'TWD'
    })
    assert response.status_code == 400
    assert 'Name is not capitalized' in response.json['error']

def test_price_validation_failure(client):
    response = client.post('/api/orders', json={
        'id': 'A0000003',
        'name': 'Melody Holiday Inn',
        'address': {
            'city': 'taipei-city',
            'district': 'da-an-district',
            'street': 'fuxing-south-road'
        },
        'price': '2500',
        'currency': 'TWD'
    })
    assert response.status_code == 400
    assert 'Price is over 2000' in response.json['error']

def test_currency_validation_failure(client):
    response = client.post('/api/orders', json={
        'id': 'A0000004',
        'name': 'Melody Holiday Inn',
        'address': {
            'city': 'taipei-city',
            'district': 'da-an-district',
            'street': 'fuxing-south-road'
        },
        'price': '1500',
        'currency': 'EUR'
    })
    assert response.status_code == 400
    assert 'Currency format is wrong' in response.json['error']

def test_price_transformation_in_float_success(client):
    response = client.post('/api/orders', json={
        'id': 'A0000005',
        'name': 'Melody Holiday Inn',
        'address': {
            'city': 'taipei-city',
            'district': 'da-an-district',
            'street': 'fuxing-south-road'
        },
        'price': '60.54',
        'currency': 'USD'
    })
    assert response.status_code == 200
    assert response.json['price'] == 1876.74
    assert response.json['currency'] == 'TWD'

def test_price_transformation_in_int_success(client):
    response = client.post('/api/orders', json={
        'id': 'A0000005',
        'name': 'Melody Holiday Inn',
        'address': {
            'city': 'taipei-city',
            'district': 'da-an-district',
            'street': 'fuxing-south-road'
        },
        'price': '60',
        'currency': 'USD'
    })
    assert response.status_code == 200
    assert response.json['price'] == 1860.0
    assert response.json['currency'] == 'TWD'

def test_usd_price_exchange_to_validation_failure(client):
    response = client.post('/api/orders', json={
        'id': 'A0000005',
        'name': 'Melody Holiday Inn',
        'address': {
            'city': 'taipei-city',
            'district': 'da-an-district',
            'street': 'fuxing-south-road'
        },
        'price': '100',
        'currency': 'USD'
    })
    assert response.status_code == 400
    assert 'Price is over 2000' in response.json['error']
