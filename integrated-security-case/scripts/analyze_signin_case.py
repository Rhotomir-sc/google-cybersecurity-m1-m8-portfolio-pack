import csv
from collections import defaultdict
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "sample-data" / "signin-events.csv"

failed_attempts = defaultdict(int)
successful_events = []

with open(DATA_FILE, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        key = (row["user"], row["source_ip"])

        if row["status"] == "failed":
            failed_attempts[key] += 1

        elif row["status"] == "success":
            successful_events.append(row)

print("Integrated Security Case - Authentication Analysis")
print("=" * 52)

for (user, source_ip), failed_count in failed_attempts.items():

    if failed_count >= 3:
        print()
        print("Suspicious Authentication Pattern")
        print("-" * 35)
        print(f"User: {user}")
        print(f"Source IP: {source_ip}")
        print(f"Failed attempts: {failed_count}")

        matching_successes = [
            event
            for event in successful_events
            if event["user"] == user
            and event["source_ip"] == source_ip
        ]

        if matching_successes:
            print("Successful sign-ins from same source: YES")
            print("Applications accessed:")

            for event in matching_successes:
                print(
                    f"- {event['application']} "
                    f"at {event['timestamp']}"
                )

            print("Assessment: REVIEW FOR POSSIBLE ACCOUNT COMPROMISE")

        else:
            print("Successful sign-ins from same source: NO")
            print("Assessment: REPEATED AUTHENTICATION FAILURES")
