# Read and Calculate IP Address with Python
from ipaddress import IPv4Address
from ipaddress import IPv4Network
from math import log2

# Creating an IPv4 Address
ip = IPv4Address("192.168.12.10")
print(ip)

# Comparing IPv4 Addresses
ip1 = IPv4Address("192.168.12.10")
ip2 = IPv4Address("220.168.13.134")
print(ip1 < ip2)
print(ip1 > ip2)

# Sorting IPv4 Addresses
addresses = (IPv4Address("92.168.100.25"), IPv4Address("196.200.64.221"),
             IPv4Address("176.255.153.159"), IPv4Address("203.166.189.66"),
             IPv4Address("210.172.195.17"), IPv4Address("180.15.76.0"),
             IPv4Address("142.31.100.44"), IPv4Address("172.16.10.5"),
             IPv4Address("172.31.10.33"), IPv4Address("175.64.10.17"))

for i in sorted(addresses):
    print(i)

# CIDR Notation and Binary Subnet Masks
for cidr in range(24, 33):
    mask = ("1" * cidr).ljust(32, "0")
    binary_mask = ".".join(mask[i:i + 8]
                           for i in range(0, 32, 8))
    print(f"/{cidr} -> {binary_mask}")

network = IPv4Network("192.4.2.0/24")
print(network)
print("Address:", network.network_address)
print("CIDR:", network.prefixlen)
print("Number of addresses:", network.num_addresses)

# Number of Addresses for Different CIDR Values
for cidr in range(24, 33):
    network = IPv4Network(f"192.168.1.0/{cidr}", strict=False)
    print(f"/{cidr}\t {network.num_addresses} addresses")


# IP Address Classes
def get_ip_class(ip):
    first_octet = int(str(ip).split(".")[0])

    if 1 <= first_octet <= 126:
        return "Class A"
    elif 128 <= first_octet <= 191:
        return "Class B"
    elif 192 <= first_octet <= 223:
        return "Class C"
    elif 224 <= first_octet <= 239:
        return "Class D"
    else:
        return "Class E"


addresses = [IPv4Address("10.20.30.40"),
             IPv4Address("172.16.5.10"),
             IPv4Address("192.168.1.100"),
             IPv4Address("230.10.20.30")]

for ip in addresses:
    print(ip, "->", get_ip_class(ip))


# Public and Private IP Addresses
addresses = [IPv4Address("192.168.1.10"),
             IPv4Address("10.20.30.40"),
             IPv4Address("172.20.10.5"),
             IPv4Address("8.8.8.8"),
             IPv4Address("1.1.1.1")]

for ip in addresses:
    print(f"{ip} -> Private" if ip.is_private else f"{ip} -> Public")

# Network of IP Addresses - Subnet Mask
network = IPv4Network("192.4.2.0/24")
print("CIDR:", network.prefixlen)
print("Subnet Mask:", network.netmask)
print("Host Mask:", network.hostmask)

# Network of IP Addresses - Usable Hosts
network1 = IPv4Network("192.168.10.0/24")
print(network1)
print("Host Bits:", 32 - network1.prefixlen)
print("Total Hosts:", network1.num_addresses)
print("Usable Hosts:", network1.num_addresses - 2)
network2 = IPv4Network("172.16.0.0/20")
print(network2)
print("Host Bits:", 32 - network2.prefixlen)
print("Total Hosts:", network2.num_addresses)
print("Usable Hosts:", network2.num_addresses - 2)

# Network of IP Addresses - Host Addresses
number_per_Line = 10
count = 0
network1 = IPv4Network("192.168.10.0/24")
for i in network1:
    print(i, end="\t")
    count += 1
    # When the count reaches 10
    if (count % number_per_Line) == 0:
        print()


def get_required_hosts(hosts):
    # Minimum Hosts required: [2^2, 2^3, 2^4, ...]
    available_hosts = [4, 8, 16, 32, 64, 128, 256, 512, 1024]
    required_hosts = []
    # Get the required hosts
    for host in hosts.values():
        for available in available_hosts:
            # Break the loop if the available_hosts greater than
            # the hosts is found
            if available > host:
                required_hosts.append(available)
                break
    return required_hosts


def get_cidr(required_hosts):
    return [32 - int(log2(hosts)) for hosts in required_hosts]


def subnetting(network, hosts):
    # Optional: Sort the subnets in descending order
    # Prioritize the one with the largest required hosts
    required_hosts = get_required_hosts(hosts)
    cidr = get_cidr(required_hosts)
    current_address = network.network_address
    for c, h in zip(cidr, hosts):
        # Set network address
        subnet = IPv4Network(f"{current_address}/{c}", strict=False)
        # get broadcast subnet
        network_addr = subnet.network_address
        broadcast_addr = subnet.network_address + (2 ** (32 - c) - 1)
        # usable Ips
        first_addr, last_addr = network_addr + 1, broadcast_addr - 1
        print(f"{h}: {first_addr} - {last_addr}")
        # Update the next address, 'last_addr + 2 to exclude the broadcast_addr
        # of the previous network, and the network_addr of the current network
        current_address = last_addr + 2


print("+ Example 1")
network = IPv4Network("192.168.10.0/24")
hosts = {"Network A": 60, "Network B": 30,
         "Network C": 14, "Network D": 6}
subnetting(network, hosts)

print("+ Example 2")
network = IPv4Network("172.16.0.0/20")
hosts = {"Network A": 400, "Network B": 200,
         "Network C": 100, "Network D": 50,
         "Network E": 25}
subnetting(network, hosts)
