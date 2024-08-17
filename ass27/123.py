import requests

# The API endpoint
url = "https://api.dev-zoomifier.com/exportanalytics"

# Data to be sent
data = {
     "opcode": "EXPORT_CUSTOMER_ENGAGEMENT_ANALYTICS",
      "userid": "1976",
      "tenantid": "403",
      "durationfrom": "2024-07-13",
      "durationto": "2024-08-12",
      "ScopeOfAnalytics": "Me"
}

# A POST request to the API
response = requests.post(url, json=data)

# Print the response
print(response.json())