import requests

# The API endpoint
url = "https://developers.zoomifier.com/analytics/export/contact"

# Data to be sent
data = {
     "APIKey":"eyJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE3Mjc3NjQ1NDYsInRlbmFudGlkIjoiNTEyIiwidXNlcmlkIjoiMjM0MCIsInJvbGVpZCI6IjgiLCJleHAiOjE3MzU1NDA1NDZ9.KpxkD0do-oaSt1IFSFaUeqAFwKJ6nTsC4Lbnd2Q5Ufw",
     "opcode": "EXPORT_CONTACT_ANALYTICS",
    "start_date": "2024-09-01",
    "end_date": "2024-10-01",
    "scope_of_analytics": "me",
    "response_format": "JSON",
    "content_count[gt]": "0",
    "engagement_time[gt]": "00"
   
}

# A POST request to the API
response = requests.get(url, params=data)

# Print the response
print(response.json())