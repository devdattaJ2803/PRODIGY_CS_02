import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import numpy as np

def caesar_cipher_image(pixels, key, encrypt=True):
    if encrypt:
        return (pixels + key) % 256
    else:
        return (pixels - key) % 256

def load_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        global img
        img = Image.open(file_path)
        img.thumbnail((250, 250))
        img_tk = ImageTk.PhotoImage(img)
        panel.config(image=img_tk)
        panel.image = img_tk
        input_image_path.set(file_path)

def encrypt_image():
    key = int(key_entry.get())
    pixels = np.array(img)
    encrypted_pixels = caesar_cipher_image(pixels, key, encrypt=True)
    encrypted_img = Image.fromarray(encrypted_pixels.astype('uint8'))
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png"), ("JPEG Files", "*.jpg")])
    if file_path:
        encrypted_img.save(file_path)
        messagebox.showinfo("Success", f"Encrypted image saved as {file_path}")

def decrypt_image():
    key = int(key_entry.get())
    pixels = np.array(img)
    decrypted_pixels = caesar_cipher_image(pixels, key, encrypt=False)
    decrypted_img = Image.fromarray(decrypted_pixels.astype('uint8'))
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png"), ("JPEG Files", "*.jpg")])
    if file_path:
        decrypted_img.save(file_path)
        messagebox.showinfo("Success", f"Decrypted image saved as {file_path}")

# Create the main window
root = tk.Tk()
root.title("Image Encryption Tool")

# Create and place the widgets
input_image_path = tk.StringVar()

tk.Label(root, text="Image Encryption Tool", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=2, pady=10)

panel = tk.Label(root)
panel.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

tk.Button(root, text="Load Image", command=load_image).grid(row=2, column=0, padx=10, pady=10)
tk.Label(root, text="Encryption/Decryption Key:").grid(row=3, column=0, padx=10, pady=10)
key_entry = tk.Entry(root)
key_entry.grid(row=3, column=1, padx=10, pady=10)

tk.Button(root, text="Encrypt Image", command=encrypt_image).grid(row=4, column=0, padx=10, pady=10)
tk.Button(root, text="Decrypt Image", command=decrypt_image).grid(row=4, column=1, padx=10, pady=10)

# Run the main event loop
root.mainloop()
