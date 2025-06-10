import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Random import get_random_bytes

def pad_key(key):
    return SHA256.new(key.encode('utf-8')).digest()

def encrypt_file(file_path, key, progress):
    try:
        key = pad_key(key)
        output_file = file_path + ".enc"

        with open(file_path, 'rb') as f:
            data = f.read()

        original_ext = os.path.splitext(file_path)[1]
        ext_bytes = original_ext.encode().ljust(10, b'#')  # fixed 10 bytes

        data = ext_bytes + data
        iv = get_random_bytes(16)
        cipher = AES.new(key, AES.MODE_CFB, iv)
        encrypted = iv + cipher.encrypt(data)

        with open(output_file, 'wb') as f:
            f.write(encrypted)

        progress["value"] = 100
        messagebox.showinfo("Success", f"Encrypted:\n{output_file}")
    except Exception as e:
        messagebox.showerror("Error", f"Encryption failed:\n{str(e)}")

def decrypt_file(file_path, key, progress):
    try:
        key = pad_key(key)

        with open(file_path, 'rb') as f:
            encrypted = f.read()

        iv = encrypted[:16]
        cipher = AES.new(key, AES.MODE_CFB, iv)
        decrypted = cipher.decrypt(encrypted[16:])

        ext = decrypted[:10].rstrip(b'#').decode()
        original_data = decrypted[10:]
        output_file = os.path.splitext(file_path)[0] + "_decrypted" + ext

        with open(output_file, 'wb') as f:
            f.write(original_data)

        progress["value"] = 100
        messagebox.showinfo("Success", f"Decrypted:\n{output_file}")
    except Exception as e:
        messagebox.showerror("Error", f"Decryption failed:\n{str(e)}")

def browse_file(entry):
    path = filedialog.askopenfilename()
    if path:
        entry.delete(0, tk.END)
        entry.insert(0, path)

def start_encrypt():
    file_path = file_entry.get()
    key = key_entry.get()
    if file_path and key:
        progress["value"] = 0
        root.after(100, lambda: encrypt_file(file_path, key, progress))
    else:
        messagebox.showwarning("Input Error", "Please select a file and enter a password.")

def start_decrypt():
    file_path = file_entry.get()
    key = key_entry.get()
    if file_path and key:
        progress["value"] = 0
        root.after(100, lambda: decrypt_file(file_path, key, progress))
    else:
        messagebox.showwarning("Input Error", "Please select a file and enter a password.")

# GUI setup
root = tk.Tk()
root.title("AES-256 File Encryptor/Decryptor")
root.geometry("500x300")
root.resizable(False, False)

tk.Label(root, text="File Path:").pack(pady=5)
file_entry = tk.Entry(root, width=50)
file_entry.pack(pady=5)
tk.Button(root, text="Browse", command=lambda: browse_file(file_entry)).pack(pady=5)

tk.Label(root, text="Password:").pack(pady=5)
key_entry = tk.Entry(root, show="*", width=50)
key_entry.pack(pady=5)

progress = ttk.Progressbar(root, length=400, mode='determinate')
progress.pack(pady=15)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)
tk.Button(btn_frame, text="Encrypt", command=start_encrypt, width=15).pack(side="left", padx=10)
tk.Button(btn_frame, text="Decrypt", command=start_decrypt, width=15).pack(side="right", padx=10)

root.mainloop()