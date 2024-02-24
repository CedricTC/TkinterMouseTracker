import tkinter as tk
import pyautogui

class MousePositionApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Mouse Konumu")

        self.label = tk.Label(self, text="Mouse Konumu:")
        self.label.pack(pady=10)

        self.custom_font = ("Helvetica", 12)

        self.position_label = tk.Label(self, text="", font=self.custom_font)
        self.position_label.pack()

        self.update_position()

    def update_position(self):        
        x, y = pyautogui.position()        
        self.position_label.config(text=f"X: {x}, Y: {y}")    
        self.after(100, self.update_position)

if __name__ == "__main__":
    app = MousePositionApp()
    app.mainloop()
