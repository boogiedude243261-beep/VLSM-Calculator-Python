# VLSM-Calc Networking Project

A simple Python script for calculating Variable Length Subnet Masks via the terminal. I built this to speed up subnetting tasks without needing to jump back and forth to a web-based calculator or having to do the math manually.

## Logic
The script takes a base network (CIDR notation) and a list of host requirements. It sorts the requirements from largest to smallest to ensure the most efficient use of the address space and calculates:
- Network Address
- Broadcast Address
- Usable IP Range
- New Subnet Mask

## How to run it
You just need Python installed.
### Linux & macOS
```bash
cd ~ && git clone https://github.com && cd ~/.local/bin && echo 'cd ~/VLSM-Calculator-Python && python3 VLSM.py' > ./vlsm && chmod +x vlsm && cd ~
```
Run globally: `vlsm`

### Windows
```bash
git clone https://github.com.git
cd VLSM-Calculator-Python
python VLSM.py
```

## Example
Input:
- Network: `192.168.1.0/24`
- Hosts: `50 20 40 30 60`

The script will output the boundaries for each block and show the remaining available space in the original scope.

---
*Note: This was written for IPv4 not IPv6

