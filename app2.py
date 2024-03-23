import requests
import concurrent.futures
import time

# The URL of your API endpoint
url = 'http://localhost:3000/test/hello'

# Number of requests to send
num_requests = 200

def send_request(url):
    """Send a single request and return the status code and response text."""
    response = requests.get(url)
    return response.status_code, response.text

# Use ThreadPoolExecutor to send requests in parallel
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    # Prepare to send multiple requests in parallel
    future_to_request = {executor.submit(send_request, url): i for i in range(num_requests)}
    
    for future in concurrent.futures.as_completed(future_to_request):
        request_id = future_to_request[future]
        try:
            status_code, response_text = future.result()
            print(f'Request #{request_id + 1}: Status Code = {status_code}, Response = {response_text}')
        except Exception as exc:
            print(f'Request #{request_id + 1} generated an exception: {exc}')

# Optional: pause to see the overall effect
time.sleep(1)
