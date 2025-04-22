from flask import Flask, render_template, jsonify
import subprocess

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/scan")
def scan():
    try:
        output = subprocess.check_output(["ubertooth-scan", "-t", "10"], stderr=subprocess.STDOUT)
        return jsonify({"output": output.decode()})
    except subprocess.CalledProcessError as e:
        return jsonify({"error": e.output.decode()})

if __name__ == "__main__":
    app.run(debug=True)
