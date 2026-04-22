# VLSM-Calc

A simple Python script for calculating Variable Length Subnet Masks via the terminal. I built this to speed up subnetting tasks without needing to jump back and forth to a web-based calculator or having to do the math manually.

## Logic
The script takes a base network (CIDR notation) and a list of host requirements. It sorts the requirements from largest to smallest to ensure the most efficient use of the address space and calculates:
- Network Address
- Broadcast Address
- Usable IP Range
- New Subnet Mask

## How to run it
You just need Python installed.

1. Clone the repo:
   `git clone https://github.com/boogiedude243261-beep/VLSM-Calculator-Python.git`

2. Run the script:
   `python VLSM.py`

## Example
Input:
- Network: `10.0.0.0/24`
- Hosts: `100 20 10`

The script will output the boundaries for each block and show the remaining available space in the original scope.

---
*Note: This was written for IPv4. IPv6 support isn't planned yet but might be added later.*
