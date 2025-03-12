import subprocess

subprocess.run("pip freeze > requirements.txt", shell=True)
subprocess.run("pyside6-uic ui/main.ui -o ui_main.py", shell=True)
subprocess.run("pyside6-rcc rc.qrc -o rc_rc.py", shell=True)
subprocess.run("pyinstaller --name 'Smart Sleep Timer' --windowed --onefile --specpath . main.py", shell=True)