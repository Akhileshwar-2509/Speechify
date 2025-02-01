import os

# Path to your service account key file
GOOGLE_APPLICATION_CREDENTIALS = "path_to_your_service_account_file.json"

# Set environment variable for authentication
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = GOOGLE_APPLICATION_CREDENTIALS
