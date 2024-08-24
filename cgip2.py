import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageEnhance, ImageOps, ImageTk

# Initialize the root window
root = tk.Tk()
root.title("Photo Customizer")
root.geometry("1200x600")
root.configure(bg="#f0f0f0")

# Global variables to hold the original and processed images
original_image = None
processed_image = None

# Function to load an image
def load_image():
    global original_image, processed_image
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
    if file_path:
        original_image = Image.open(file_path)
        processed_image = original_image.copy()
        display_image(original_image, original_label)
        display_image(processed_image, processed_label)
        enable_buttons()

# Function to display an image in a label
def display_image(image, label):
    image = image.resize((500, 500), Image.LANCZOS)
    tk_image = ImageTk.PhotoImage(image)
    label.config(image=tk_image)
    label.image = tk_image

# Function to apply compression
def compress_image():
    global processed_image
    processed_image = original_image.copy()
    processed_image = processed_image.resize((processed_image.width // 2, processed_image.height // 2), Image.LANCZOS)
    processed_image = processed_image.resize((processed_image.width * 2, processed_image.height * 2), Image.LANCZOS)
    display_image(processed_image, processed_label)

# Function to convert to black and white
def convert_to_black_and_white():
    global processed_image
    processed_image = original_image.copy()
    processed_image = ImageOps.grayscale(processed_image).convert("RGBA")
    display_image(processed_image, processed_label)

# Function to apply negative effect
def apply_negative():
    global processed_image
    processed_image = original_image.copy()
    processed_image = ImageOps.invert(processed_image.convert("RGB")).convert("RGBA")
    display_image(processed_image, processed_label)

# Function to adjust brightness
def adjust_brightness():
    global processed_image
    processed_image = original_image.copy()
    enhancer = ImageEnhance.Brightness(processed_image)
    processed_image = enhancer.enhance(1.2)
    display_image(processed_image, processed_label)

# Function to adjust contrast
def adjust_contrast():
    global processed_image
    processed_image = original_image.copy()
    enhancer = ImageEnhance.Contrast(processed_image)
    processed_image = enhancer.enhance(1.2)
    display_image(processed_image, processed_label)

# Function to save the processed image
def save_image():
    if processed_image:
        save_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG files", "*.jpg"), ("PNG files", "*.png")])
        if save_path:
            processed_image.save(save_path)
            messagebox.showinfo("Success", "Image saved successfully!")
    else:
        messagebox.showerror("Error", "No image to save!")

# Function to enable buttons after image is loaded
def enable_buttons():
    compress_button.config(state=tk.NORMAL)
    bw_button.config(state=tk.NORMAL)
    negative_button.config(state=tk.NORMAL)
    brightness_button.config(state=tk.NORMAL)
    contrast_button.config(state=tk.NORMAL)
    download_button.config(state=tk.NORMAL)

# Create and place widgets
upload_button = tk.Button(root, text="Upload Image", command=load_image, bg="#4CAF50", fg="white")
upload_button.pack(side=tk.TOP, padx=10, pady=10)

button_frame = tk.Frame(root)
button_frame.pack(side=tk.TOP, pady=10)

compress_button = tk.Button(button_frame, text="Compress Image", command=compress_image, bg="#007BFF", fg="white", state=tk.DISABLED)
compress_button.pack(side=tk.LEFT, padx=5)

bw_button = tk.Button(button_frame, text="Black & White", command=convert_to_black_and_white, bg="#007BFF", fg="white", state=tk.DISABLED)
bw_button.pack(side=tk.LEFT, padx=5)

negative_button = tk.Button(button_frame, text="Negative", command=apply_negative, bg="#007BFF", fg="white", state=tk.DISABLED)
negative_button.pack(side=tk.LEFT, padx=5)  # Added comma

brightness_button = tk.Button(button_frame, text="Brightness", command=adjust_brightness, bg="#007BFF", fg="white", state=tk.DISABLED)
brightness_button.pack(side=tk.LEFT, padx=5)

contrast_button = tk.Button(button_frame, text="Contrast", command=adjust_contrast, bg="#007BFF", fg="white", state=tk.DISABLED)
contrast_button.pack(side=tk.LEFT, padx=5)

download_button = tk.Button(root, text="Download Image", command=save_image, bg="#007BFF", fg="white", state=tk.DISABLED)
download_button.pack(side=tk.TOP, pady=10)

image_frame = tk.Frame(root)
image_frame.pack(side=tk.TOP, pady=10)

original_label = tk.Label(image_frame)
original_label.pack(side=tk.LEFT, padx=10, pady=10)

processed_label = tk.Label(image_frame)
processed_label.pack(side=tk.RIGHT, padx=10, pady=10)

root.mainloop()
