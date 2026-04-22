#setup
R = "\033[31m"
G = "\033[32m"
BL = "\033[34m"
BO = "\033[1m"
RT = "\033[0m"
import math 
while True: 
    adrs = input(f"{BO} {G} Enter Network Address in A.B.C.D/E Format: {RT}")
    parts = adrs.split("/")
    strt_mask = int(parts[1])
    stcl = ((0xFFFFFFFF << (32-strt_mask)) & 0xFFFFFFFF) 
    ip = parts[0]
    octet = "".join(f"{int(x):08b}" for x in ip.split(".")) 
    def to_ip(n):
       return f"{(n>>24)&255}.{(n>>16)&255}.{(n>>8)&255}.{n&255}"
    current = int(octet, 2) & stcl
    total_ips = 2**(32-strt_mask) 
    rawhost = input(f"{BO} {G} Enter all your subnets hostcounts like this: x y z: {RT}")
    host_list = [int(h.strip()) for h in rawhost.split()]
    host_list.sort(reverse=True)
    subnum = 1

    print(f"{BO}\n  Sorting largest to smallest...{RT} \n")
    for curhost in host_list:
     print(f"{BO}Subnet # {subnum}{RT}")
     hostbits = math.ceil(math.log2(curhost + 2))
     new_mask = 32 - hostbits 
     walking = 2**hostbits 
     next = current + walking
     gateway = next - 2
     if walking > total_ips: 
          print(f"{R}{BO}!!! ERROR: Only {total_ips} IPs left. This request needs {walking}. {RT}")
          break  # Out of space!
     total_ips -= walking 
     bitmask = ((0xFFFFFFFF << (32-new_mask)) & 0xFFFFFFFF)
     print(f"{BL}Subnet Mask: {RT} {to_ip(bitmask)} || /{new_mask}")
     print(f"{G}Network Address: {RT} {to_ip(current)}")
     print(f"{G}Gateway Address:{RT} {to_ip(gateway)}")
     print(f"{G}Broadcast Address: {RT} {to_ip(next - 1)} \n")
     current+=walking 
     subnum += 1
     if total_ips > 0:
        usable_power = 2**math.floor(math.log2(total_ips))
     else:
        usable_power = 0

     print(f"              Remaining Addresses: {total_ips}")
     print(f"              Largest Usable Block: {usable_power-2} /{32 - int(math.log2(usable_power)) if usable_power > 0 else 32}")
     
    input(f"\nPress ENTER to Restart:\n")


  
        



    

