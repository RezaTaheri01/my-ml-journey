import subprocess
import ctypes


ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 6)  # minimize
run = subprocess.run("jupyter notebook", capture_output=True)
