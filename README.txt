
🔍 Web-Based TCP Port Scanner
=============================

A simple, threaded TCP port scanner with a web-based GUI, built using Python and Flask. Easily scan a single host or a /24 subnet for open TCP ports from your browser.

🌐 Features
-----------
- ✅ Web interface for input and results
- ✅ Supports single IP and subnet scanning (e.g., 192.168.1.0/24)
- ✅ Multithreaded for fast scanning
- ✅ Validates port ranges
- ✅ Displays open ports in real-time

🛠️ Installation
----------------
1. Clone the Repo:
   git clone https://github.com/yourusername/web-port-scanner.git
   cd web-port-scanner

2. Install Dependencies:
   Make sure you have Python 3 installed.
   pip install flask

🚀 Usage
--------
Run the App:
   python app.py

Then open your browser and visit:
   http://127.0.0.1:5000

📥 Input Parameters
-------------------
Target       : IP address or subnet prefix (e.g., 192.168.1)
Start Port   : Starting port number (e.g., 20)
End Port     : Ending port number (e.g., 100)
Threads      : Number of threads (e.g., 50)
Subnet Scan  : Check to scan the entire /24 range

✅ Safe Targets for Testing
---------------------------
127.0.0.1        : Your own machine (localhost)
192.168.x.x      : Local network devices
scanme.nmap.org  : Public scan target by Nmap (use respectfully)

📁 Project Structure
--------------------
port_scanner_web/
├── app.py               # Flask app with port scanning logic
├── templates/
│   └── index.html       # Frontend UI template
└── README.txt           # Documentation

⚠️ Legal Disclaimer
-------------------
This tool is intended for educational and authorized use only.
Do NOT scan IP addresses you do not own or have permission to scan.

🧠 Future Features (Ideas)
--------------------------
- Export results to CSV or PDF
- Add banner grabbing / service detection
- Deploy to public server (e.g., Render, Replit)
- Real-time scan progress with WebSocket

📧 Contact
----------
Made by: Bedangshu Raj Mudiar
GitHub : https://github.com/itsbedangshu

