import platform
import subprocess

def power():
    system = platform.system()
    if system == "Windows":
        _shutdown_windows()
    elif system == "Linux":
        _shutdown_linux()
    elif system == "Darwin":
       _shutdown_mac()
    else:
        print(f"Unsupported OS: {system}")

def _shutdown_windows():
    import os
    try:
        os.system("shutdown /s /t 1")
    except Exception as e:
        print(f"Failed to shutdown on Windows: {e}")

def _shutdown_linux():
    try:
        subprocess.run(["shutdown", "-h", "now"], check=True)
    except Exception as e:
        print(f"Failed to shutdown on Linux: {e}")

def _shutdown_mac():
    try:
        subprocess.run(["shutdown", "-h", "now"], check=True)
    except Exception as e:
        print(f"Failed to shutdown on macOS: {e}")