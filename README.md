# Port Scanner 

A professional Python-based TCP port scanner designed for ethical hacking and network auditing. This tool identifies open ports and attempts to retrieve service banners for version enumeration.

##  Features
- **TCP Connect Scan**: Precise identification of open ports using the `socket` library.
- **Banner Grabbing**: Retrieves service information to identify versions and running services.
- **Multithreaded Scanning**: High-performance execution using `threading` and `Queue` for near-instant results.
- **Reporting**: Automatically generates a structured `resultado.txt` file with scan results.
- **Performance Tracking**: Measures and displays the total execution time (Benchmark).
- **Robust Error Handling**: Handles invalid IPs, hostnames, and manual interrupts (Ctrl+C).

## 📊 Performance Comparison

| Version | Method | Time (500 ports) |
| :--- | :--- | :--- |
| v1.0 | Sequential | ~50 seconds |
| **v2.0** | **Multithreaded** | **~1.5 seconds** |

## 🛠️ Installation & Usage

1. **Clone the repository**:
   ```bash
   git clone https://github.com/aronvillarnobo/port-scanner-python.git

2. **Run the tool**:

   **Windows:**
   ```bash
   python port_scanner_v2.py

   **macOS / Linux:**
   ```bash
   python3 port_scanner_v2.py  

## ⚠️ Disclaimer
**This tool is for educational and ethical testing purposes only. Scanning targets without explicit prior authorization is illegal and unethical. The developer is not responsible for any misuse of this tool.**
- **Developed by Aron Villarnobo - April 2026**
