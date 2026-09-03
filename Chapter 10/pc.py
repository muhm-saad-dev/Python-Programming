prices = {
    'CPU (i5-10400F, Used/Tray)': 25000,
    'Motherboard (H410M, Used)': 15000,
    'RAM (16GB DDR4 2x8GB, Used/New)': 12000,
    'GPU (GTX 1650 Super 4GB, Used)': 35000,
    'SSD (SanDisk 500GB SATA, New)': 11000,
    'PSU (550W 80+ Bronze, New)': 11500,
    'PC Case (Micro-ATX Office, New)': 5000,
    'UPS (Crown 850VA, New)': 18000
}
total = sum(prices.values())
print(f"Total: {total}")
for k, v in prices.items():
    print(f"{k}: Rs. {v:,}")
