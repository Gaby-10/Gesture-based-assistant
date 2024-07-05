import tkinter as tk
import threading

def setup_gui(start_command, exit_command):
    root = tk.Tk()
    root.title("Hand Gesture Recognition")
    root.geometry("300x100")

    start_button = tk.Button(root, text="Start Gesture Recognition", command=start_command)
    start_button.pack(pady=10)

    exit_button = tk.Button(root, text="Exit", command=exit_command)
    exit_button.pack(pady=5)

    root.protocol("WM_DELETE_WINDOW", exit_command)  # Ensure window close button works
    root.mainloop()

def close_gui(root):
    root.quit()  # Quit the tkinter application
    root.destroy()  # Destroy the tkinter application
    exit()


if __name__ == "__main__":
    root = tk.Tk()
    gui_thread = threading.Thread(target=setup_gui, args=(hand_gesture_recognition, lambda: close_gui(root)))
    gui_thread.start()
