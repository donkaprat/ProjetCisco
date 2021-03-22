import meraki

# Defining your API key as a variable in source code is not recommended
API_KEY = 'eca68c2bc709c33ea3cc7e90830d64ed358f9d73'
# Instead, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

dashboard = meraki.DashboardAPI(API_KEY)

serial = 'Q2FV-Q8RR-2AGL'

response = dashboard.devices.getDevice(
    serial
)

print(response)