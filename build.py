import subprocess

subprocess.run("pip freeze > requirements.txt", shell=True)
subprocess.run("pyside6-uic ui/main.ui -o ui_main.py", shell=True)
subprocess.run("pyside6-rcc rc.qrc -o rc_rc.py", shell=True)