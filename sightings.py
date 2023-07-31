from flask import request, jsonify
from app.api import bp
from app.models import Sighting
from sqlalchemy import func
from datetime import datetime

@bp.route('/sightings', methods=['GET'])
def get_sightings():
    location = request.args.get('location')
    date = request.args.get('date')

    query = Sighting.query

    if location:
        query = query.filter(func.lower(Sighting.location) == func.lower(location))
    
    if date:
        try:
            date = datetime.strptime(date, "%Y-%m-%d")  # we're assuming the date is in YYYY-MM-DD format
            query = query.filter(func.date(Sighting.date) == date.date())
        except ValueError:
            return jsonify({'error': 'Invalid date format, expected YYYY-MM-DD'}), 400

    results = query.all()
    
    return jsonify([{
        'id': sighting.id,
        'location': sighting.location,
        'date': sighting.date.isoformat(),
        'details': sighting.details
    } for sighting in results])