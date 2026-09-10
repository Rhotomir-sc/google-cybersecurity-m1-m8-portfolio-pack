import re

security_text = """
Suspicious activity was detected from 185.44.21.90.
The process attempted to contact fshjaifhajfa.click.
Another connection was observed to 193.46.217.4.

File SHA256:
d202ed020ed8e36bd8a0f5b571a19d386c12abecb2a28c989d50bbf92c78f54e
"""

ip_pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
domain_pattern = r"\b[a-zA-Z0-9.-]+\.(?:com|net|org|click|top|io|thm)\b"
sha256_pattern = r"\b[a-fA-F0-9]{64}\b"

ip_addresses = re.findall(ip_pattern, security_text)
domains = re.findall(domain_pattern, security_text)
sha256_hashes = re.findall(sha256_pattern, security_text)

print("IOC Extraction Results")
print("======================")

print()
print("IP Addresses")
print("------------")
for ip in ip_addresses:
    print(ip)

print()
print("Domains")
print("-------")
for domain in domains:
    print(domain)

print()
print("SHA-256 Hashes")
print("--------------")
for sha256 in sha256_hashes:
    print(sha256)
