import platform
import subprocess

def lock_screen():
    system = platform.system()
    if system == "Windows":
        _lock_screen_windows()
    elif system == "Linux":
        _lock_screen_linux()
    elif system == "Darwin":
        _lock_screen_mac()
    else:
        print(f"Unsupported OS: {system}")

def _lock_screen_windows():
    import ctypes
    try:
        ctypes.windll.user32.LockWorkStation()
    except Exception as e:
        print(f"Failed to lock screen on Windows: {e}")

def _lock_screen_linux():
    try:
        subprocess.run(["xdg-screensaver", "lock"], check=True)
    except Exception as e:
        print(f"Failed to lock screen on Linux: {e}")

def _lock_screen_mac():
    try:
        subprocess.run(["pmset", "displaysleepnow"], check=True)
    except Exception as e:
        print(f"Failed to lock screen on macOS: {e}")