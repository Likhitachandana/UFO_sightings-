import pytest
from unittest.mock import patch
from app.models import Sighting, db
from app.services.scraper import update_sightings

@patch('app.services.scraper.requests.get')
def test_update_sightings(mock_get):
    # Arrange
    mock_get.return_value.text = """
    <html>
        <body>
            <tr>
                <td>01/01/2023 00:00</td>
                <td>New York</td>
                <td></td>
                <td>It was amazing!</td>
            </tr>
        </body>
    </html>
    """

    # Act
    update_sightings()

    # Assert
    sighting = Sighting.query.first()
    assert sighting is not None
    assert sighting.location == 'New York'
    assert sighting.details == 'It was amazing!'