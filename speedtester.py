import speedtest

def run():
    st = speedtest.Speedtest()
    st.get_best_server()
    download = st.download() / 1_000_000   # Convert to Mbps
    upload = st.upload() / 1_000_000
    ping = st.results.ping
    print(f"Ping: {ping:.2f} ms")
    print(f"Download: {download:.2f} Mbps")
    print(f"Upload: {upload:.2f} Mbps")

if __name__ == "__main__":
    run()

