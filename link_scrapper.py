import socket
import re
import ssl
import sys
from urllib.parse import urlparse

def fetch_page_content(url):
    """Fetches the HTML content of a webpage."""
    try:
        parsed_url = urlparse(url)
        conn_type = parsed_url.scheme
        host = parsed_url.netloc

        print(f"\n[+] Extracted Host: {host}")

        req = f"GET / HTTP/1.1\r\nHost: {host}\r\n"
        req += "User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0\r\n"
        req += "Accept-Encoding: identity\r\nConnection: close\r\n\r\n"

        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if conn_type == "http":
            port = 80
        elif conn_type == "https":
            port = 443
            context = ssl.create_default_context()
            conn = context.wrap_socket(conn, server_hostname=host)
        else:
            print("[!] Unsupported URL scheme. Use http or https.")
            return None

        conn.connect((host, port))
        conn.send(req.encode())

        response = ""
        while True:
            chunk = conn.recv(8192).decode("utf-8", errors="ignore")
            if not chunk:
                break
            response += chunk

        conn.close()
        return response

    except Exception as e:
        print(f"[!] Error: {e}")
        return None

def extract_external_links(html_content, host):
    """Extracts and returns external links from the given HTML content."""
    url_regex = r"https?://(?:www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/\S*)?"
    all_links = re.findall(url_regex, html_content)

    external_links = [link for link in all_links if host not in link]
    return external_links

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    html_content = fetch_page_content(url)
    
    if html_content:
        parsed_url = urlparse(url)
        host = parsed_url.netloc
        external_links = extract_external_links(html_content, host)

        print("\n[+] External Links Found:\n")
        for link in external_links:
            print(f"  - {link}")

        print(f"\n[+] Total External Links: {len(external_links)}")

if __name__ == "__main__":
    main()
