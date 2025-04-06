# LEGO_MINDSTORM
This repository contains various Java-based programs and experiments for the LEGO Mindstorms NXT robot using the LeJOS NXJ firmware.

lego_mindstorms/
│
├── src/                # Java source files
│   ├── HelloWorld.java
│   └── ...
│
├── bin/                # Compiled class files
│
├── lib/                # LeJOS libraries
│
└── README.md           # Project overview


**LEGO Robot + Python Bluetooth Setup Guide (macOS)**

This guide describes how to set up your macOS system to communicate with the LEGO Mindstorms Robot Inventor (51515) using Python and Bluetooth. 

---

### 1. Check Your Python Installation

Open the terminal and run:

```bash
python3 --version
```
or
```bash
pip3 --version
```

If Python is not installed or the version is outdated, install it using Homebrew:

```bash
brew install python
```

This will install the latest stable version of Python 3 and the `pip` package manager.

---

### 2. Install Required Python Packages

Once Python is available, install the necessary packages for Bluetooth communication with LEGO 51515:

```bash
pip3 install pybricksdev bleak
```

These packages include:
- `pybricksdev`: for working with LEGO firmware and communication
- `bleak`: for BLE (Bluetooth Low Energy) communication on macOS

---

### 3. Test Your Python Environment

Create a simple Python file to verify everything is working:

1. Create a file named `hello.py` with the following content:

```python
print("Hello World!")
```

2. Run the file in terminal:

```bash
python3 hello.py
```

Expected output:

```
admins-MBP:LEGO_MINDSTORM admin$ python3 hello.py
Hello World!
```

---

### Next Steps

After verifying Python works:
- Try to connect to your LEGO Hub using the `bleak` library
- Optionally flash Pybricks firmware for full Python support
- Build a Bluetooth bridge to control your robot via REST/MQTT

If you encounter connection issues, try unpairing the Hub from macOS Bluetooth settings and restarting the connection process.

---

Happy coding with LEGO and Python! 🤖
