import qrcode
from PIL import Image, ImageTk
import tkinter as tk

def generate_qr_code():
    link = link_entry.get()  
    img = qrcode.make(link)  
    qr_image = ImageTk.PhotoImage(img)  
    qr_label.config(image=qr_image)
    qr_label.image = qr_image  

window = tk.Tk()
window.title("QR Code Generator")
tk.Label(window, text="Enter the LINK of the website:").pack(pady=10)
link_entry = tk.Entry(window, width=50)
link_entry.pack()
generate_button = tk.Button(window, text="Generate QR Code", command=generate_qr_code)
generate_button.pack(pady=10)
qr_label = tk.Label(window)
qr_label.pack()
window.mainloop()
