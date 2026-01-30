from apscheduler.schedulers.background import BackgroundScheduler
from app.services.processor import process_market

# ✅ DEFINE SCHEDULER AT MODULE LEVEL
scheduler = BackgroundScheduler()

def run_hourly_job():
    try:
        process_market("AI Infrastructure", "AI infrastructure GPU data centers")
        process_market("Bitcoin", "Bitcoin crypto market")
        process_market("Fintech", "Fintech payments lending")
        print("[scheduler] snapshot saved")
    except Exception as e:
        print("[scheduler] error:", e)

def start_scheduler():
    # ✅ prevent duplicate jobs
    if not scheduler.running:
        scheduler.add_job(run_hourly_job, "interval", minutes=1)
        scheduler.start()
