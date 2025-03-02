import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

def decode_message():
    file_path = r"C:\Users\manve\Desktop\project\nature.png"
    if not file_path:
        return

    try:
        img = Image.open(file_path)
        pixels = img.load()

        binary_msg = ""
        for y in range(img.height):
            for x in range(img.width):
                r, g, b, a = pixels[x, y]
                binary_msg += str(r & 1)

        message = ""
        for i in range(0, len(binary_msg), 8):
            byte = binary_msg[i:i+8]
            if byte == "00000000":  # End marker
                break
            message += chr(int(byte, 2))

        if message:
            messagebox.showinfo("Hidden Message", message)
        else:
            messagebox.showerror("Error", "No hidden message found.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI
root = tk.Tk()
root.title("Image Steganography - Decrypt")

tk.Button(root, text="Select Image to Decrypt", command=decode_message).pack()

root.mainloop()
