import pytest
from datetime import datetime
from app.models import Sighting, db
from main import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # setup a clean database before each test
        yield client

def test_get_sightings(client):
    # Arrange
    sighting = Sighting(location='New York', date=datetime.now(), details='Amazing!')
    db.session.add(sighting)
    db.session.commit()

    # Act
    response = client.get('/api/sightings?location=New York')

    # Assert
    assert response.status_code == 200
    json_response = response.get_json()
    assert len(json_response) == 1
    assert json_response[0]['location'] == 'New York'
    assert json_response[0]['details'] == 'Amazing!'