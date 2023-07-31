import requests
from bs4 import BeautifulSoup
from app.models import Sighting, db
from datetime import datetime

def update_sightings():
    # Get the page content
    res = requests.get('http://www.nuforc.org/webreports.html')
    soup = BeautifulSoup(res.text, 'html.parser')

    # Assume that each sighting is in a table row
    for row in soup.find_all('tr'):
        columns = row.find_all('td')

        if len(columns) > 3:  # assuming we have at least 4 columns in the table
            # Extract fields from the table row
            date_string = columns[0].text.strip()
            location = columns[1].text.strip()
            details = columns[3].text.strip()

            # Parse date
            try:
                date = datetime.strptime(date_string, '%m/%d/%Y %H:%M')  # change to match the date format on the website
            except ValueError:
                print(f"Couldn't parse date {date_string}. Skipping this row.")
                continue

            # Create a new sighting object
            sighting = Sighting(location=location, date=date, details=details)

            # Add it to the session and commit
            db.session.add(sighting)
    
    db.session.commit()