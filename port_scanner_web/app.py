<<<<<<< HEAD
from flask import Flask, render_template, request
import socket
import threading
from queue import Queue

app = Flask(__name__)
socket.setdefaulttimeout(0.5)
print_lock = threading.Lock()


def tcp_scan(ip, port, result):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result_code = s.connect_ex((ip, port))
        if result_code == 0:
            with print_lock:
                result.append(f"{ip}:{port}/TCP Open")
        s.close()
    except:
        pass


def worker(scan_queue, result):
    while not scan_queue.empty():
        ip, port = scan_queue.get()
        tcp_scan(ip, port, result)
        scan_queue.task_done()


def scan(ip_list, start_port, end_port, threads):
    scan_queue = Queue()
    result = []

    for ip in ip_list:
        for port in range(start_port, end_port + 1):
            scan_queue.put((ip, port))

    for _ in range(threads):
        t = threading.Thread(target=worker, args=(scan_queue, result))
        t.daemon = True
        t.start()

    scan_queue.join()
    return sorted(result)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        target = request.form["target"]
        start_port = int(request.form["start_port"])
        end_port = int(request.form["end_port"])
        threads = int(request.form["threads"])
        is_network = "network" in request.form

        ip_list = []
        if is_network:
            try:
                base = ".".join(target.strip().split(".")[:3])
                ip_list = [f"{base}.{i}" for i in range(1, 255)]
            except:
                return render_template("index.html", error="Invalid network prefix.")
        else:
            ip_list = [target]

        results = scan(ip_list, start_port, end_port, threads)
        return render_template("index.html", results=results)

    return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True)
=======
from flask import Flask, render_template, request
import socket
import threading
from queue import Queue

app = Flask(__name__)
socket.setdefaulttimeout(0.5)
print_lock = threading.Lock()


def tcp_scan(ip, port, result):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result_code = s.connect_ex((ip, port))
        if result_code == 0:
            with print_lock:
                result.append(f"{ip}:{port}/TCP Open")
        s.close()
    except:
        pass


def worker(scan_queue, result):
    while not scan_queue.empty():
        ip, port = scan_queue.get()
        tcp_scan(ip, port, result)
        scan_queue.task_done()


def scan(ip_list, start_port, end_port, threads):
    scan_queue = Queue()
    result = []

    for ip in ip_list:
        for port in range(start_port, end_port + 1):
            scan_queue.put((ip, port))

    for _ in range(threads):
        t = threading.Thread(target=worker, args=(scan_queue, result))
        t.daemon = True
        t.start()

    scan_queue.join()
    return sorted(result)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        target = request.form["target"]
        start_port = int(request.form["start_port"])
        end_port = int(request.form["end_port"])
        threads = int(request.form["threads"])
        is_network = "network" in request.form

        ip_list = []
        if is_network:
            try:
                base = ".".join(target.strip().split(".")[:3])
                ip_list = [f"{base}.{i}" for i in range(1, 255)]
            except:
                return render_template("index.html", error="Invalid network prefix.")
        else:
            ip_list = [target]

        results = scan(ip_list, start_port, end_port, threads)
        return render_template("index.html", results=results)

    return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True)
>>>>>>> 2eb96a5 (Initial commit of port scanner project)
