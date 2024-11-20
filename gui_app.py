import tkinter as tk
from tkinter import filedialog, messagebox
import os
from ai import generate_answer
from obfuscation import obfuscate_text, extract_dictionary
import pyperclip

class ObfuscatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Enterprise Obfuscator")
        self.root.geometry("800x600")

        self.obfuscation_dict = {}

        # Input Text Field
        self.input_label = tk.Label(root, text="Input Text:")
        self.input_label.pack()
        self.input_text = tk.Text(root, height=15)
        self.input_text.pack(fill=tk.BOTH, expand=True)

        # Output Text Field
        self.output_label = tk.Label(root, text="Obfuscated Text:")
        self.output_label.pack()
        self.output_text = tk.Text(root, height=15)
        self.output_text.pack(fill=tk.BOTH, expand=True)

        # Buttons Frame
        self.buttons_frame = tk.Frame(root)
        self.buttons_frame.pack()

        self.load_file_button = tk.Button(self.buttons_frame, text="Load File", command=self.load_file)
        self.load_file_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.obfuscate_button = tk.Button(self.buttons_frame, text="Obfuscate", command=self.obfuscate_text_action)
        self.obfuscate_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.copy_button = tk.Button(self.buttons_frame, text="Copy Obfuscated Text", command=self.copy_to_clipboard)
        self.copy_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.show_dict_button = tk.Button(self.buttons_frame, text="Dictionary", command=self.show_dictionary)
        self.show_dict_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.loaded_file_path = None

    def load_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.loaded_file_path = file_path
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    self.input_text.delete(1.0, tk.END)
                    self.input_text.insert(tk.END, content)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load file: {e}")

    def obfuscate_text_action(self):
        input_text_content = self.input_text.get(1.0, tk.END).strip()
        if not input_text_content:
            messagebox.showwarning("Input Required", "Please enter or load text to obfuscate.")
            return

        # Generate the obfuscation dictionary using the LLM
        generated_dictionary_text = generate_answer(input_text_content)
        if generated_dictionary_text.strip() == "{}":
            messagebox.showinfo("No Sensitive Data", "No sensitive data found to obfuscate.")
            return

        # Extract the dictionary from the LLM's response
        self.obfuscation_dict = extract_dictionary(generated_dictionary_text)
        if not self.obfuscation_dict:
            messagebox.showerror("Error", "Failed to extract obfuscation dictionary.")
            return

        # Obfuscate the text
        obfuscated_text = obfuscate_text(input_text_content, self.obfuscation_dict)
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, obfuscated_text)

        # If a file was loaded, save the obfuscated text to a new file
        if self.loaded_file_path:
            base, ext = os.path.splitext(self.loaded_file_path)
            obfuscated_file_path = f"{base}_OBFUSCATED{ext}"
            try:
                with open(obfuscated_file_path, 'w', encoding='utf-8') as file:
                    file.write(obfuscated_text)
                messagebox.showinfo("File Saved", f"Obfuscated file saved as:\n{obfuscated_file_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save obfuscated file: {e}")

    def copy_to_clipboard(self):
        obfuscated_text_content = self.output_text.get(1.0, tk.END).strip()
        if obfuscated_text_content:
            pyperclip.copy(obfuscated_text_content)
            messagebox.showinfo("Copied", "Obfuscated text copied to clipboard.")
        else:
            messagebox.showwarning("No Text", "There is no obfuscated text to copy.")

    def show_dictionary(self):
        if not self.obfuscation_dict:
            messagebox.showwarning("No Dictionary", "No obfuscation dictionary available.")
            return

        dict_window = tk.Toplevel(self.root)
        dict_window.title("Obfuscation Dictionary")
        dict_window.geometry("400x300")

        dict_text = tk.Text(dict_window)
        dict_text.pack(fill=tk.BOTH, expand=True)
        dict_text.insert(tk.END, str(self.obfuscation_dict))
        dict_text.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = ObfuscatorApp(root)
    root.mainloop()
