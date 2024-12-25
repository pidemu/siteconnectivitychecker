from function import check_site, display_dashboard, log_status_to_file, alert_user

print("Welcome to the Site Connectivity Checker!")

#User inputs URLs separated by commas
urls = input("Please enter website URLs separated by commas: ").split(',')

processed_urls = []

#Checks URLS to starts with https and removes extra spaces
for url in urls:
    url = url.strip()  #Remove extra spaces
    if not url.startswith("https://"): #Checks if input starts with 'https://' if it doesn't it adds it for the user
        print("The URL ",url," does not start with 'https://'. We corrected it for you!")
        url = "https://" + url
    processed_urls.append(url)

#Loop through each URL to check its status & calls on def functions for results
for url in processed_urls:
    status, response_time, timestamp = check_site(url)
    display_dashboard(url, status, response_time, timestamp)  #Display status
    log_status_to_file(url, status, response_time, timestamp)  #Log the result to the site_connectivity_log.txt file
    alert_user(url, status)  #Show alert if necessary

#https://google.com (Sever 200 - Good)
#https://httpbin.org/status/500 (Server 505 - the server does not recognize or cannot fulfill the request)
#https://httpbin.org/status/404 (Server 404 - a server could not find a client-requested webpage)