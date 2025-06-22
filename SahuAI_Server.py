import subprocess
import webbrowser
import time
import platform
import os
import sys
import socket

def is_port_in_use(port=5000):
    """Check if port is already in use (e.g. server already running)"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(("127.0.0.1", port)) == 0

def run_flask():
    print("🚀 Launching Flask development server...")

    if is_port_in_use():
        print("⚠️ Port 5000 is already in use. Trying to open the running server in browser...")
        webbrowser.open("http://127.0.0.1:5000")
        return

    try:
        command = [sys.executable, "app.py"]  # Safest way to launch current Python interpreter
        env = os.environ.copy()
        env.update({
            "FLASK_ENV": "development",
            "FLASK_DEBUG": "1"
        })

        flask_process = subprocess.Popen(command, env=env)

        print("⏳ Waiting for server to initialize...")
        time.sleep(1.5)
        webbrowser.open("http://127.0.0.1:5000")

        print("✅ Flask server running at http://127.0.0.1:5000")
        print("📌 Press Ctrl+C in terminal to stop the server.")
        flask_process.wait()

    except Exception as e:
        print(f"❌ Failed to start Flask server: {e}")

    finally:
        print("🧹 Server process cleaned up.")

if __name__ == "__main__":
    run_flask()
