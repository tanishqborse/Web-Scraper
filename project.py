import socket 
import re
import ssl
import sys

# Get the host from the input URL
url = sys.argv[1]
conn_type = url.split("://")[0]
host = url.split("//")[1].split("/")[0]
print(host)
# Construct the GET request
req = "GET / HTTP/1.1\r\n"
req += "Accept-Encoding: identity\r\n"
req += "Host: " + host + "\r\n"
req += "User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0\r\n"
req += "Connection: close\r\n\r\n"

# Send the request and receive the response
resp = ""
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if conn_type == "http":
    conn.connect((host, 80))
    conn.send(req.encode())
    resp = conn.recv(8192).decode('UTF-8')
    conn.close()
elif conn_type == "https":
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    s_conn = context.wrap_socket(conn, server_hostname=host)
    s_conn.connect((host, 443))
    s_conn.send(req.encode())
    data=s_conn.recv(8192).decode()
    while data !="":
        resp += data
        data = s_conn.recv(8192).decode('UTF-8')
    conn.close()

# Use regex to find all external links in the response
urlregex = r"(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})"
external_links = [url for url in re.findall(urlregex, resp) if host not in url]

# Print the external links and the count
print("External links:")
for url in external_links:
    print(url)
print("Number of external links: ", len(external_links))
