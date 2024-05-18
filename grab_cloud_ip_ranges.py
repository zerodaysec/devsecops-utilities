import datetime
import requests

# Get the current time
now = datetime.datetime.now()

# Format the time as a timestamp
timestamp = now.strftime("%Y%m%d%H%M%S")


# Set the URLs for the IP range files
aws_url = "https://ip-ranges.amazonaws.com/ip-ranges.json"
azure_url = "https://download.microsoft.com/download/7/1/D/71D86715-5596-4529-9B13-DA13A5DE5B63/ServiceTags_Public_20221226.json"  # "https://www.microsoft.com/en-us/download/confirmation.aspx?id=56519"
gcp_url = "https://www.gstatic.com/ipranges/cloud.json"
oracle_url = "https://docs.oracle.com/iaas/tools/public_ip_ranges.json"

# Download the AWS IP ranges
response = requests.get(aws_url)
aws_ranges = response.json()

# Save the AWS IP ranges to a file
with open(f"{timestamp}-aws-ip-ranges.json", "w") as f:
    f.write(str(aws_ranges))

# Download the Azure IP ranges
response = requests.get(azure_url)
azure_ranges = response.text

# Save the Azure IP ranges to a file
with open(f"{timestamp}-azure-ip-ranges.json", "w") as f:
    f.write(str(azure_ranges))

# Download the GCP IP ranges
response = requests.get(gcp_url)
gcp_ranges = response.json()

# Save the GCP IP ranges to a file
with open(f"{timestamp}-gcp-ip-ranges.json", "w") as f:
    f.write(str(gcp_ranges))


# Download the Oracle IP ranges
response = requests.get(oracle_url)
oracle_ranges = response.json()

# Save the AWS IP ranges to a file
with open(f"{timestamp}-oracle-ip-ranges.json", "w") as f:
    f.write(str(oracle_ranges))