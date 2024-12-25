# Site Connectivity Checker

The **Site Connectivity Checker** my **CIS 3260 Project** is a Python program designed to check the availability of websites by sending HTTP requests. It provides real-time status, response time, and logs the results for later reference. Alerts are also shown if a site is unreachable or experiencing issues.

## Built With
![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![PyCharm](https://img.shields.io/badge/IDE-PyCharm-green.svg)

## Features
- Checks the status of multiple websites.
- Displays status, response time, and timestamp in the console.
- Logs results to a file for reference.
- Alerts users if a website is down or unreachable.

## How It Works
1. Users input a list of website URLs (comma-separated).
2. The program:
   - Sends HTTP requests to the provided URLs.
   - Retrieves the HTTP status, response time, and timestamp.
   - Displays the results in the console.
   - Logs the results to a file named `site_connectivity_log.txt`.
   - Alerts the user if the site is not accessible.

## Prerequisites
- Python 3.6 or later.
- `requests` library.

Install the `requests` library using pip:
```bash
pip install requests
```

## Code Organization 
- **site_checker_main.py** (Main script that runs the program and handles user interactions.)
- **function.py** (Contains all the core functions used for the project)
- **site_connectivity_log.txt** (A log file that stores the history of connectivity checks)

## Site Connectivity Checker Sample:
![unnamed](https://github.com/user-attachments/assets/652afd57-3b69-4d88-b490-c86665ad04dc)

