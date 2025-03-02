import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

def encode_message():
    file_path = r"C:\Users\manve\Documents\free-nature-images.jpg"
    if not file_path:
        return

    message = message_entry.get("1.0", tk.END).strip()
    if not message:
        messagebox.showerror("Error", "Please enter a message to hide")
        return

    try:
        img = Image.open(file_path)
        img = img.convert("RGBA")
        pixels = img.load()

        binary_msg = ''.join(format(ord(char), '08b') for char in message) + '00000000'  # End marker

        msg_index = 0
        for y in range(img.height):
            for x in range(img.width):
                r, g, b, a = pixels[x, y]

                if msg_index < len(binary_msg):
                    new_r = (r & ~1) | int(binary_msg[msg_index])  # Modify LSB
                    pixels[x, y] = (new_r, g, b, a)
                    msg_index += 1
                else:
                    break
            if msg_index >= len(binary_msg):
                break

        save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png")])
        if save_path:
            img.save(save_path)
            messagebox.showinfo("Success", "Message hidden successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI
root = tk.Tk()
root.title("Image Steganography - Encrypt")

tk.Label(root, text="Enter Message to Hide:").pack()
message_entry = tk.Text(root, height=5, width=40)
message_entry.pack()

tk.Button(root, text="Select Image & Encrypt", command=encode_message).pack()

root.mainloop()
