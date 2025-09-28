import requests
import sys

def check_application_status(url):
    """
    Checks the status of an application by making an HTTP GET request to the given URL.

    Args:
        url (str): The URL of the application to check.

    Returns:
        None. Prints the status directly to the console.
    """
    try:
        response = requests.get(url, timeout=10)
        if 200 <= response.status_code < 300:
            print(f"SUCCESS: Application at '{url}' is UP.")
            print(f"Status Code: {response.status_code}")
        else:
            print(f"FAILURE: Application at '{url}' is DOWN.")
            print(f"Status Code: {response.status_code} ({response.reason})")

    except requests.exceptions.Timeout:
        print(f"FAILURE: The request to '{url}' timed out. The application may be down or slow.")
    except requests.exceptions.ConnectionError:
        print(f"FAILURE: Could not connect to '{url}'. The application is likely DOWN.")
    except requests.exceptions.RequestException as e:
        print(f"FAILURE: An unexpected error occurred for URL '{url}'.")
        print(f"Error: {e}")

def main():
    """
    Main function to get URL from command-line arguments and run the check.
    """
    if len(sys.argv) > 1:
        target_url = sys.argv[1]
    else:
        target_url = "https://www.google.com"
        print("Usage: python app_health_checker.py <your_url>")
        print(f"No URL provided. Running check on example: {target_url}\n")

    if not target_url.startswith(('http://', 'https://')):
        print(f"Warning: URL '{target_url}' does not have a scheme. Prepending 'https://'.")
        target_url = 'https://' + target_url

    check_application_status(target_url)

if __name__ == "__main__":
    main()

