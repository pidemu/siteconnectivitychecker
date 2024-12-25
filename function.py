import requests
from datetime import datetime

#Function to check the status of a site using python request & pip install requests
def check_site(url):
    response = requests.get(url, timeout = 5) #Gets request of a given URL with 5 seconds timeout to wait for a response from the server
    if response.status_code == 200:
        status = response.status_code #Request HTTPS status of URL
        response_time = response.elapsed.total_seconds() #Time it took for the HTTP request using import requests
    else:
        status = response.status_code
        response_time = "N/A"

    timestamp = datetime.now().strftime("%m-%d-%Y %I:%M%p")
    return status, response_time, timestamp

#Function to display results
def display_dashboard(url, status, response_time, timestamp):
    print("---------------Checking Website Connectivity---------------")
    if status == 200:
        print("| Status Message: The site is UP.")
    else:
        print("| Status Message: The site is DOWN.")
    print("-----------------------------------------------------------")
    print("| URL:", url)
    print("| Status:", str(status))
    print("| Response Time:", str(response_time), "s")
    print("| Last Checked:", timestamp)
    print("-----------------------------------------------------------")

#Function to log results to site_connectivity_log.txt
def log_status_to_file(url, status, response_time, timestamp):
    with open("site_connectivity_log.txt", "a") as log_file:
        log_entry = (timestamp + ": " + url + " - Status: " + str(status) + ", "
            + "Response Time: " + str(response_time) + "s\n")

        log_file.write(log_entry)

#Function to alert user if there's a connectivity issue
def alert_user(url, status):
    if status != 200:
        print("ALERT! The site", url, "has an issue. Status:", str(status), ".")