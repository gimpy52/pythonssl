import ssl
import socket

"""
This is where things will go eventually
"""
hostname = "www.google.com"
#cert = CertInfo(host=hostname, port=443)
#info = cert.cipher()

context = ssl.create_default_context()

conn = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=hostname)
conn.connect(('google.com', 443))

cert = conn.getpeercert()
print(cert)
