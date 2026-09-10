import csv
from collections import Counter
from pathlib import Path

LOG_FILE = Path(__file__).parent.parent / "sample-data" / "login_attempts.csv"
FAILURE_THRESHOLD = 3


def load_failed_logins(file_path):
    failed_events = []

    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["status"].lower() == "failed":
                failed_events.append(row)

    return failed_events


def count_failed_attempts(events, field):
    return Counter(event[field] for event in events)


def print_summary(title, counter):
    print(f"\n{title}")
    print("-" * len(title))

    for value, count in counter.most_common():
        flag = " <-- REVIEW" if count >= FAILURE_THRESHOLD else ""
        print(f"{value}: {count}{flag}")


def main():
    failed_events = load_failed_logins(LOG_FILE)

    print("Failed Login Analysis")
    print("=====================")
    print(f"Total failed attempts: {len(failed_events)}")

    failures_by_user = count_failed_attempts(failed_events, "username")
    failures_by_ip = count_failed_attempts(failed_events, "source_ip")

    print_summary("Failures by User", failures_by_user)
    print_summary("Failures by Source IP", failures_by_ip)


if __name__ == "__main__":
    main()
