from flask import Flask, render_template, jsonify
import subprocess

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/scan")
def scan():
    try:
        output = subprocess.check_output(
            ["hcitool", "lescan", "--duplicates"],
            stderr=subprocess.STDOUT,
            timeout=10
        )
        return jsonify({"output": output.decode()})
    except subprocess.CalledProcessError as e:
        return jsonify({"error": e.output.decode()})
    except FileNotFoundError:
        return jsonify({"error": "hcitool not found. Install it with: sudo apt install bluez"})
    except subprocess.TimeoutExpired:
        return jsonify({"error": "Scan timed out. Try again or check your Bluetooth adapter."})

if __name__ == "__main__":
    app.run(debug=True)
