# Multi-Threaded TCP Port Scanner

A lightweight, highly efficient multi-threaded TCP port scanner written in Python. This tool demonstrates low-level socket programming and concurrent programming execution, utilizing a thread pool and thread-safe queue structures.

## 🚀 Features
- **Concurrent Scanning:** Utilizes Python's `threading` and `queue` libraries to scan up to 100 ports simultaneously.
- **Error Handling:** Automatically handles domain name resolution (DNS lookup) and catches common socket exceptions.
- **Port Ranges:** Allows the user to dynamically define the target IP/domain as well as the custom start and end port ranges.

## 🛠️ How It Works
Rather than scanning ports sequentially, which suffers from massive latency bottlenecks during timeouts, this tool queues specified ports and distributes them among daemon threads. Each thread attempts a TCP three-way handshake using the standard `socket.connect_ex()` method. A return code of `0` indicates a completed handshake (open port).

## 💻 Usage
Run the script using Python 3:

```bash
python3 scanner.py
