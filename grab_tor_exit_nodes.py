import datetime
import requests

# Get the current time
now = datetime.datetime.now()
# Format the time as a timestamp
timestamp = now.strftime("%Y%m%d%H%M%S")

# Send a request to the Tor exit node list API
response = requests.get("https://check.torproject.org/exit-addresses")

# Extract the list of exit nodes from the response
exit_nodes = response.text.splitlines()

# Save the exit nodes to a file with the timestamp and "tor_exit_nodes" as part of the name
with open(f"{timestamp}_tor_exit_nodes.txt", "w") as f:
    f.write("\n".join(exit_nodes))