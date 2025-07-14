import tkinter as tk
from tkinter import messagebox
from spellchecker import SpellChecker

class SpellCheckerApp:
    def __init__(self, root):
        self.spell = SpellChecker()

        root.title("Spell Checker")
        root.geometry("500x300")
        root.config(bg="#f0f0f0")

        self.label = tk.Label(root, text="Enter Text Below:", font=("Arial", 12), bg="#f0f0f0")
        self.label.pack(pady=10)

        self.text_entry = tk.Text(root, height=5, width=50, font=("Arial", 12))
        self.text_entry.pack(pady=10)

        self.check_button = tk.Button(root, text="Check Spelling", command=self.check_spelling, font=("Arial", 12), bg="#4CAF50", fg="white")
        self.check_button.pack(pady=5)

        self.result_label = tk.Label(root, text="", font=("Arial", 12), bg="#f0f0f0", wraplength=450, justify="left")
        self.result_label.pack(pady=10)

    def check_spelling(self):
        text = self.text_entry.get("1.0", tk.END).strip()
        words = text.split()
        corrected_words = []

        changes = []

        for word in words:
            corrected = self.spell.correction(word)
            corrected_words.append(corrected)
            if corrected != word:
                changes.append(f'"{word}" → "{corrected}"')

        corrected_text = ' '.join(corrected_words)

        if changes:
            result = f"Corrected Text:\n{corrected_text}\n\nChanges:\n" + "\n".join(changes)
        else:
            result = "No spelling mistakes found."

        self.result_label.config(text=result)


if __name__ == "__main__":
    root = tk.Tk()
    app = SpellCheckerApp(root)
    root.mainloop()
