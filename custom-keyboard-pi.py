import tkinter as tk
from pynput.keyboard import Controller, Key

# --- CONFIGURATION ---
# List of keys to show. Use strings for letters or 'Key.space' for special keys.
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
        self.root.attributes("-topmost", True)  # Always on top
        self.root.overrideredirect(True)       # Remove window borders/title bar
        self.root.geometry("+100+500")         # Initial position (x+y)
        
        self.create_widgets()

    def press_key(self, key_val):
        """Simulates the key press into the active window."""
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
        """Builds the UI grid based on the KEYS config."""
        for r, row in enumerate(KEYS):
            for c, key in enumerate(row):
                btn = tk.Button(self.root, text=key, width=6, height=2,
                                command=lambda k=key: self.press_key(k),
                                bg="#333", fg="white", activebackground="#555")
                btn.grid(row=r, column=c, padx=2, pady=2)
        
        # Add a small 'drag' handle or close button
        close_btn = tk.Button(self.root, text="X", command=self.root.destroy, bg="red", fg="white")
        close_btn.grid(row=0, column=len(KEYS[0]), sticky='ne')

if __name__ == "__main__":
    root = tk.Tk()
    app = VirtualKeyboard(root)
    root.mainloop()
