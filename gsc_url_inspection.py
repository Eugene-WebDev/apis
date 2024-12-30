from google.oauth2 import service_account
from googleapiclient.discovery import build

# Step 1: Set up credentials
# Replace with the path to your credentials.json file
CREDENTIALS_FILE = "credentials.json"

# Scope for Search Console API
SCOPES = ["https://www.googleapis.com/auth/webmasters"]

# Authenticate and build the service
credentials = service_account.Credentials.from_service_account_file(
    CREDENTIALS_FILE, scopes=SCOPES
)
service = build("searchconsole", "v1", credentials=credentials)

# Step 2: Define the URL to inspect
url_to_inspect = "https://www.techwithtim.net/"

# Step 3: Perform URL Inspection
try:
    request = {
        "inspectionUrl": url_to_inspect,
        "languageCode": "en",
    }
    response = service.urlInspection().index().inspect(body=request).execute()

    # Process the response
    inspection_result = response.get("inspectionResult", {})
    print("URL Inspection Result:")
    print(f"URL: {url_to_inspect}")
    print(f"Indexing Status: {inspection_result.get('indexStatusResult', {}).get('status', 'Unknown')}")
    print(f"Last Crawl Date: {inspection_result.get('indexStatusResult', {}).get('lastCrawlDate')}")
    print(f"Coverage State: {inspection_result.get('indexStatusResult', {}).get('coverageState')}")
    print(f"Mobile Usability: {inspection_result.get('mobileUsabilityResult', {}).get('status', 'Unknown')}")
except Exception as e:
    print("An error occurred:", str(e))

