from flask import Flask, render_template, jsonify, request
import subprocess
import shutil
import time

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/scan")
def scan():
    scan_type = request.args.get("type", "hcitool")

    try:
        if scan_type == "hcitool":
            # Run continuous scan for 5 seconds then terminate
            proc = subprocess.Popen(
                ["hcitool", "-i", "hci0", "lescan", "--duplicates"],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT
            )
            time.sleep(5)
            proc.terminate()
            output, _ = proc.communicate()

        elif scan_type == "ubertooth":
            if shutil.which("ubertooth-scan"):
                output = subprocess.check_output(
                    ["ubertooth-scan", "-t", "10"],
                    stderr=subprocess.STDOUT,
                    timeout=10
                )
            else:
                return jsonify({"error": "Ubertooth not found. Try: sudo apt install ubertooth"})

        elif scan_type == "mesh":
            output = subprocess.check_output(
                ["python3", "mesh_broadcast.py"],
                stderr=subprocess.STDOUT,
                timeout=10
            )

        else:
            return jsonify({"error": "Invalid scan type."})

        return jsonify({"output": output.decode()})

    except subprocess.CalledProcessError as e:
        return jsonify({"error": e.output.decode()})
    except FileNotFoundError as e:
        return jsonify({"error": f"Tool not found: {e}"})
    except subprocess.TimeoutExpired:
        return jsonify({"error": "Scan timed out. Try again or check your adapter."})

if __name__ == "__main__":
    app.run(debug=True)
