allowed_ips = [
    "192.168.10.10",
    "192.168.10.15",
    "192.168.10.20",
    "10.10.10.15",
    "185.44.21.90"
]

remove_ips = [
    "10.10.10.15",
    "185.44.21.90"
]

print("Access List Update")
print("==================")

print()
print("Original Allow List")
print("-------------------")

for ip in allowed_ips:
    print(ip)

for ip in remove_ips:
    if ip in allowed_ips:
        allowed_ips.remove(ip)

print()
print("Removed IP Addresses")
print("--------------------")

for ip in remove_ips:
    print(ip)

print()
print("Updated Allow List")
print("------------------")

for ip in allowed_ips:
    print(ip)
