import os
import json
import random
from datetime import datetime, timedelta

# Dossier de sortie
OUTPUT_DIR = "../data"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Liste de voitures
CAR_IDS = [f"C{i:04d}" for i in range(1, 6)]  # C0001 → C0005

# Durée de simulation : 24h
START_TIME = datetime(2025, 4, 17, 0, 0)
INTERVAL_MINUTES = 5
TOTAL_EVENTS = int((24 * 60) / INTERVAL_MINUTES)  # toutes les 5 min pendant 24h

def generate_event(car_id, current_time):
    return {
        "car_id": car_id,
        "timestamp": current_time.isoformat(),
        "speed": round(random.uniform(0, 130), 1),
        "location": {
            "lat": round(random.uniform(48.80, 48.90), 6),  # Paris area
            "lon": round(random.uniform(2.25, 2.45), 6)
        },
        "engine_temp": round(random.uniform(70, 110), 2),
        "fuel_level": round(random.uniform(5, 100), 1)
    }

def main():
    print("Génération des fichiers JSON...")

    for car_id in CAR_IDS:
        events = []
        current_time = START_TIME

        for _ in range(TOTAL_EVENTS):
            event = generate_event(car_id, current_time)
            events.append(event)
            current_time += timedelta(minutes=INTERVAL_MINUTES)

        file_path = os.path.join(OUTPUT_DIR, f"{car_id}.json")
        with open(file_path, "w") as f:
            json.dump(events, f, indent=2)

        print(f"✅ Fichier généré : {file_path} ({len(events)} événements)")

if __name__ == "__main__":
    main()
