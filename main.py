import tkinter as tk
import psutil
import time
import pygetwindow as gw
import threading

class VSCodeTimeCounter:
    def __init__(self, root):
        self.root = root
        self.root.title("VS Code Time Counter")

        self.counter = 0
        self.running = False

        self.label = tk.Label(root, text="Time spent in VS Code: 0 seconds", font=("Helvetica", 16))
        self.label.pack(pady=20)

        self.stop_button = tk.Button(root, text="Stop", command=self.stop_counter)
        self.stop_button.pack(pady=5)

        self.exit_button = tk.Button(root, text="Exit", command=self.exit_app)
        self.exit_button.pack(pady=5)

        # Check if VS Code is already running
        self.check_vscode_running()

        # Start monitoring VS Code
        threading.Thread(target=self.monitor_vscode).start()

    def get_vscode_window(self):
        vscode_windows = gw.getWindowsWithTitle("Visual Studio Code")
        if vscode_windows:
            return vscode_windows[0]
        else:
            return None

    def stop_counter(self):
        self.running = False

    def exit_app(self):
        self.running = False
        self.root.destroy()

    def measure_vscode_time(self):
        start_time = time.time()
        while self.running:
            time.sleep(1)
            self.counter += 1
            self.label.config(text="Time spent in VS Code: {} seconds".format(self.counter))
            self.root.update()
        end_time = time.time()
        duration = end_time - start_time
        self.show_popup("Time spent in VS Code: {:.2f} seconds".format(duration))

    def check_vscode_running(self):
        for proc in psutil.process_iter(['pid', 'name']):
            if "Code.exe" in proc.info['name']:  # Check the process name
                self.start_counter()
                break

    def start_counter(self):  # يجب تحريك هذه الدالة إلى هنا
        self.running = True
        threading.Thread(target=self.measure_vscode_time).start()

    def monitor_vscode(self):
        while True:
            vscode_running = False
            for proc in psutil.process_iter(['pid', 'name']):
                if "Code.exe" in proc.info['name']:
                    vscode_running = True
                    break
            if not vscode_running and self.running:
                self.stop_counter()
            elif vscode_running and not self.running:
                self.start_counter()
            time.sleep(5)

    def show_popup(self, message):
        popup = tk.Toplevel()
        popup.title("Time Info")
        popup.geometry("300x100")
        popup.resizable(False, False)
        popup_label = tk.Label(popup, text=message, font=("Helvetica", 14))
        popup_label.pack(pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    app = VSCodeTimeCounter(root)
    root.mainloop()
