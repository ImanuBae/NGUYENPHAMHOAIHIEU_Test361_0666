import tkinter as tk
from tkinter import messagebox, scrolledtext

from transposition_cipher import TranspositionCipher


class TranspositionUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Transposition Cipher")
        self.root.geometry("760x560")

        self.cipher = TranspositionCipher()

        tk.Label(root, text="Input Text").grid(row=0, column=0, padx=10, pady=(10, 4), sticky="w")
        self.input_text = scrolledtext.ScrolledText(root, height=9)
        self.input_text.grid(row=1, column=0, columnspan=4, padx=10, sticky="nsew")

        tk.Label(root, text="Key").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.key_entry = tk.Entry(root, width=12)
        self.key_entry.insert(0, "8")
        self.key_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        tk.Button(root, text="Encrypt", command=self.encrypt).grid(row=2, column=2, padx=6, pady=10, sticky="ew")
        tk.Button(root, text="Decrypt", command=self.decrypt).grid(row=2, column=3, padx=10, pady=10, sticky="ew")

        tk.Label(root, text="Output Text").grid(row=3, column=0, padx=10, pady=(6, 4), sticky="w")
        self.output_text = scrolledtext.ScrolledText(root, height=9)
        self.output_text.grid(row=4, column=0, columnspan=4, padx=10, sticky="nsew")

        tk.Button(root, text="Copy Output To Input", command=self.copy_output_to_input).grid(
            row=5, column=0, columnspan=2, padx=10, pady=10, sticky="ew"
        )
        tk.Button(root, text="Clear", command=self.clear).grid(
            row=5, column=2, columnspan=2, padx=10, pady=10, sticky="ew"
        )

        root.columnconfigure(0, weight=1)
        root.columnconfigure(1, weight=0)
        root.columnconfigure(2, weight=1)
        root.columnconfigure(3, weight=1)
        root.rowconfigure(1, weight=1)
        root.rowconfigure(4, weight=1)

    def get_key(self):
        try:
            return int(self.key_entry.get().strip())
        except ValueError:
            raise ValueError("Key phai la so nguyen.")

    def get_input(self):
        return self.input_text.get("1.0", tk.END).rstrip("\n")

    def set_output(self, text):
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, text)

    def encrypt(self):
        try:
            result = self.cipher.encrypt(self.get_input(), self.get_key())
            self.set_output(result)
        except ValueError as exc:
            messagebox.showerror("Invalid input", str(exc))

    def decrypt(self):
        try:
            result = self.cipher.decrypt(self.get_input(), self.get_key())
            self.set_output(result)
        except ValueError as exc:
            messagebox.showerror("Invalid input", str(exc))

    def copy_output_to_input(self):
        output = self.output_text.get("1.0", tk.END).rstrip("\n")
        self.input_text.delete("1.0", tk.END)
        self.input_text.insert(tk.END, output)

    def clear(self):
        self.input_text.delete("1.0", tk.END)
        self.output_text.delete("1.0", tk.END)


if __name__ == "__main__":
    app = tk.Tk()
    TranspositionUI(app)
    app.mainloop()
