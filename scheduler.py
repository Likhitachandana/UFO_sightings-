from apscheduler.schedulers.background import BackgroundScheduler
from app.services.scraper import update_sightings

def run_scheduler():
    sched = BackgroundScheduler(daemon=True)
    sched.add_job(update_sightings,'interval',hours=24)
    sched.start()
