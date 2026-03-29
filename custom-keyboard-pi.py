import tkinter as tk
from pynput.keyboard import Controller, Key

# --- CONFIGURATION ---
KEYS = [
    ['Q', 'W', 'E', 'R', 'T'],
    ['A', 'S', 'D', 'F', 'G'],
    ['Z', 'X', 'C', 'V', 'B'],
    ['Space', 'Enter', 'Esc']
]

class VirtualKeyboard:
    def __init__(self, root):
        self.root = root
        self.keyboard = Controller()
        
        # Window setup
        self.root.title("Custom ARM Keyboard")
        self.root.attributes("-topmost", True)
        self.root.overrideredirect(True)
        self.root.geometry("+100+500")
        
        # Variables to track drag position
        self._offset_x = 0
        self._offset_y = 0

        self.create_widgets()

    def start_drag(self, event):
        """Capture initial mouse position relative to window."""
        self._offset_x = event.x
        self._offset_y = event.y

    def do_drag(self, event):
        """Update window position based on mouse movement."""
        x = self.root.winfo_x() + (event.x - self._offset_x)
        y = self.root.winfo_y() + (event.y - self._offset_y)
        self.root.geometry(f"+{x}+{y}")

    def press_key(self, key_val):
        try:
            if key_val == "Space":
                self.keyboard.press(Key.space)
                self.keyboard.release(Key.space)
            elif key_val == "Enter":
                self.keyboard.press(Key.enter)
                self.keyboard.release(Key.enter)
            elif key_val == "Esc":
                self.keyboard.press(Key.esc)
                self.keyboard.release(Key.esc)
            else:
                self.keyboard.type(key_val)
        except Exception as e:
            print(f"Error pressing {key_val}: {e}")

    def create_widgets(self):
        # 1. DRAG HANDLE (Full-width bar at the top)
        drag_handle = tk.Label(self.root, text="⁝⁝ DRAG HERE ⁝⁝", bg="#222", fg="gray", cursor="fleur")
        drag_handle.grid(row=0, column=0, columnspan=len(KEYS[0]), sticky='ew', pady=(0, 5))
        
        # Bind drag events to the handle
        drag_handle.bind("<Button-1>", self.start_drag)
        drag_handle.bind("<B1-Motion>", self.do_drag)

        # 2. KEYBOARD KEYS
        for r, row in enumerate(KEYS):
            for c, key in enumerate(row):
                btn = tk.Button(self.root, text=key, width=6, height=2,
                                command=lambda k=key: self.press_key(k),
                                bg="#333", fg="white", activebackground="#555")
                # r+1 because row 0 is the drag handle
                btn.grid(row=r+1, column=c, padx=2, pady=2)
        
        # 3. CLOSE BUTTON
        close_btn = tk.Button(self.root, text="X", command=self.root.destroy, 
                              bg="#800", fg="white", font=("Arial", 8, "bold"))
        close_btn.grid(row=0, column=len(KEYS[0])-1, sticky='ne')

if __name__ == "__main__":
    root = tk.Tk()
    app = VirtualKeyboard(root)
    root.mainloop()
