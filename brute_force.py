import csv
from datetime import datetime, timedelta

tries_threshold = 3
time_threshold = 60

def demo_datetime():
    time = datetime.strptime("14:00:01", "%H:%M:%S")
    print(f"First time: {time}")
    later_time = datetime.strptime("14:00:08", "%H:%M:%S")
    print(f"Later time: {later_time}")
    print(f"later_time - time = {later_time - time}")

def read_events(path):
    events = []
    with open(path, encoding="utf-8", newline="") as csv_file:
        for row in csv.DictReader(csv_file):
            events.append((row["time"], row["ip"]))
    return events
        

# 3 tries within 60 seconds
def find_brute_force(events):
    occurrency_times = {}
    for timestamp, ip in events:
        if ip not in occurrency_times:
            occurrency_times[ip] = []
        occurrency_times[ip].append(datetime.strptime(timestamp, "%H:%M:%S"))
    
    hits = set()
    for ip, timestamps in occurrency_times.items():
        timestamps.sort()
        for i in range(len(timestamps) - (tries_threshold -1)):
            if timestamps[i + (tries_threshold - 1)] - timestamps[i] <= timedelta(seconds=time_threshold):
                hits.add(ip)
    return sorted(hits)


if __name__ == "__main__":
    #demo_datetime()
    events = read_events("events.csv")
    print(events)
    print("---------------------")
    hits = find_brute_force(events)
    print(f"IP addresses with brute force attempts: {hits}")