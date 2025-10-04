from datetime import datetime, timedelta
import uuid

def generate_time_slots(start_time, end_time, interval_minutes, court_id, date):
    slots = []
    current = start_time
    while current < end_time:
        slot = {
            "slot_id": str(uuid.uuid4()),  
            "court_id": court_id,
            "date": date,
            "start": current.strftime("%H:%M"),
            "end": (current + timedelta(minutes=interval_minutes)).strftime("%H:%M"),
            "status": "available"
        }
        slots.append(slot)
        current += timedelta(minutes=interval_minutes)
    return slots


