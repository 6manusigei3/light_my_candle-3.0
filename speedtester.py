import speedtest
import csv
from datetime import datetime

# Run a speed test
def run():
    st = speedtest.Speedtest()
    st.get_best_server()
    download = st.download() / 1_000_000  # Convert to Mbps
    upload = st.upload() / 1_000_000
    ping = st.results.ping

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"[{timestamp}] Ping: {ping:.2f} ms | Download: {download:.2f} Mbps | Upload: {upload:.2f} Mbps")

    # Save to CSV
    with open("speed_log.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, ping, download, upload])

# Add header if file is new
try:
    with open("speed_log.csv", "x", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Timestamp", "Ping (ms)", "Download (Mbps)", "Upload (Mbps)"])
except FileExistsError:
    pass

run()


