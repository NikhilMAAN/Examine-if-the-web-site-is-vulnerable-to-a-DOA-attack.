import requests
import psutil
import time

def check_dos_vulnerability(url, request_interval=1, num_requests=10):
    try:
        print(f"Testing {url} for DoS vulnerability...")

        # Send the specified number of requests with the specified interval
        for _ in range(num_requests):
            response = requests.get(url)
            # You can add more checks based on the response status code, headers, etc.
            
            time.sleep(request_interval)  # Pause for the specified interval

        print(f"The website {url} might be vulnerable to a DoS attack.")
        return True
    except Exception as e:
        print(f"Error: {e}")
        print(f"The website {url} seems stable.")
        return False

def display_network_connections():
    """
    Display formatted information about network connections associated with the current script.
    """
    connections = psutil.net_connections()
    
    print("\nCurrent network connections:")
    print("{:<10} {:<40} {:<40} {:<10} {:<10} {:<10}".format("FD", "LADDR", "RADDR", "STATUS", "PID", "TYPE"))
    
    for conn in connections:
        print("{:<10} {:<40} {:<40} {:<10} {:<10} {:<10}".format(
            conn.fd, 
            f"{conn.laddr.ip}:{conn.laddr.port}", 
            f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else "",
            conn.status,
            conn.pid if conn.pid else "",
            conn.type
        ))

def main():
    # Take input from the user
    website_url = input("Enter the website URL to check for DoS vulnerability: ")
    interval = float(input("Enter the request interval in seconds (default is 1): ") or 1)
    num_requests = int(input("Enter the number of requests to send (default is 10): ") or 10)
    
    # Example usage
    dos_vulnerability = check_dos_vulnerability(website_url, request_interval=interval, num_requests=num_requests)

    if dos_vulnerability:
        print(f"{website_url} might be vulnerable to DoS attacks.")
    else:
        print(f"{website_url} is not prone to DoS attacks, or the check could not be completed.")

    # Display network connections associated with the script
    display_network_connections()

if __name__ == "__main__":
    main()

