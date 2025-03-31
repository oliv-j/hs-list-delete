import requests
import time
import datetime

# Hard-coded bearer token (replace with your actual token)
BEARER_TOKEN = "XXX"

# Rate limiting: 50 calls per 10 seconds = 0.2 seconds per call
RATE_LIMIT_SLEEP = 0.2

def log_result(message):
    """Append a log entry with a date-time stamp to log.txt."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("log.txt", "a") as log_file:
        log_file.write(f"{timestamp} - {message}\n")

def delete_list(list_id):
    """Delete a list using the HubSpot API and log the result."""
    url = f"https://api.hubapi.com/crm/v3/lists/{list_id}"
    headers = {
        "Authorization": f"Bearer {BEARER_TOKEN}",
        "Content-Type": "application/json"
    }
    try:
        response = requests.delete(url, headers=headers)
        code = response.status_code
        try:
            result = response.json()
            status = result.get("status", "No status")
            message = result.get("message", "No message")
        except Exception:
            status = "unknown"
            message = response.text
        log_line = f"List ID: {list_id} - Response Code: {code} - Status: {status} - Message: {message}"
        log_result(log_line)
    except Exception as e:
        log_line = f"List ID: {list_id} - Error: {str(e)}"
        log_result(log_line)

def main():
    try:
        with open("lists.txt", "r") as file:
            list_ids = [line.strip() for line in file if line.strip()]
    except Exception as e:
        log_result(f"Error reading lists.txt: {str(e)}")
        return

    for list_id in list_ids:
        delete_list(list_id)
        time.sleep(RATE_LIMIT_SLEEP)

if __name__ == "__main__":
    main()
