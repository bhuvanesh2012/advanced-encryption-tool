# 🔐 AES-256 File Encryption Tool
This is a Python-based GUI application that lets you encrypt and decrypt files using AES-256 encryption with a clean and simple interface.

---
## 💡 Features
✅ AES-256 file encryption and decryption

✅ Simple GUI using Tkinter

✅ Progress bar for both encryption and decryption

✅ Toggle option to delete original file after operation

✅ Auto-restore original file extension after decryption

⚠️ Supports all file types (including .pdf, .jpg, .txt, etc.)

---
## 🛠️ Requirements
Make sure the following Python libraries are installed using the terminal:

```bash
pip install cryptography
```

---
## 🚀 How to Run
#### 1. **Download or clone this repository.**

#### 2. ***Run the script*** --> aes_gui_tool.py

#### 3. Use the GUI to:

‎ ‎ ‎ ‎ ‎ ‎  • Choose a file to encrypt or decrypt

‎ ‎ ‎ ‎ ‎ ‎  • Optionally toggle whether to delete the original file

‎ ‎ ‎  ‎ ‎ ‎ • Monitor progress through the progress bar

‎ ‎ ‎ ‎ ‎ ‎  • Get the output file in the same directory

#### 4. Output:

![Image](https://github.com/user-attachments/assets/dcbf78dc-7dc2-4c98-a856-9ad800e8d3fc)

---
## 🧪 Testing
### To test encryption:

Select any file and click Encrypt File

It will create a .enc version of the file.

**📝Note:**
If the "Delete original file after operation" is toggled ON then the original file will be automatically deleted after Encryption.

### To test decryption:

Select a .enc file created by this tool and click Decrypt File

It will restore the original content and extension as filename_decrypted.ext

**📝Note:**
If the "Delete original file after operation" is toggled ON then the Encrypted file will be automatically deleted after Decryption

---
## 📂 Example
This is how the files will be saved upon the operation selected:

Original File: report.pdf  
Encrypted File: report.pdf.enc  
Decrypted File: report_decrypted.pdf

---
## ⚠️ Disclaimer
This tool is for educational and personal security use only. Do not use it on sensitive or legally protected files without permission.

---

### 👤 Author
**COMPANY:** CODTECH IT SOLUTIONS

**NAME:** Bhuvanesh D

**INTERN ID:** CT04DN710

**DOMAIN:** CYBER SECURITY AND ETHICAL HACKING

**DURATION:** 4 WEEKS

**MENTOR:** NEELA SANTHOSH KUMAR

