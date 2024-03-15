import cv2
import tkinter as tk
from tkinter import filedialog, messagebox, Label, Entry, Button, Scale, IntVar, Checkbutton

def resize_image(image, new_width):
    ratio = new_width / image.shape[1]
    new_height = int(image.shape[0] * ratio)
    resized_image = cv2.resize(image, (new_width, new_height))
    return resized_image

def apply_threshold(image, threshold_value):
    _, thresholded_image = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)
    return thresholded_image

def process_image():
    image_path = image_entry.get()
    if not image_path:
        messagebox.showerror("Error", "Please select an image.")
        return

    image = cv2.imread(image_path)

    if image is None:
        messagebox.showerror("Error", "Could not read the image.")
        return

    new_width = int(resize_scale.get())
    threshold_value = threshold_scale.get()

    if apply_threshold_var.get() == 1:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image = apply_threshold(image, threshold_value)
    else:
        image = resize_image(image, new_width)

    cv2.imshow("Processed Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

root = tk.Tk()
root.title("Image Processing Tool")

image_label = Label(root, text="Image Path:")
image_label.grid(row=0, column=0, padx=5, pady=5)

image_entry = Entry(root, width=50)
image_entry.grid(row=0, column=1, padx=5, pady=5)

browse_button = Button(root, text="Browse", command=lambda: image_entry.insert(tk.END, filedialog.askopenfilename()))
browse_button.grid(row=0, column=2, padx=5, pady=5)

resize_label = Label(root, text="Resize Value:")
resize_label.grid(row=1, column=0, padx=5, pady=5)

resize_scale = Scale(root, from_=100, to=1000, orient=tk.HORIZONTAL, length=200)
resize_scale.set(500)
resize_scale.grid(row=1, column=1, padx=5, pady=5)

apply_threshold_var = IntVar()
apply_threshold_checkbox = Checkbutton(root, text="Apply Thresholding", variable=apply_threshold_var)
apply_threshold_checkbox.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

threshold_label = Label(root, text="Threshold Value:")
threshold_label.grid(row=3, column=0, padx=5, pady=5)

threshold_scale = Scale(root, from_=0, to=255, orient=tk.HORIZONTAL, length=200)
threshold_scale.set(127)
threshold_scale.grid(row=3, column=1, padx=5, pady=5)

process_button = Button(root, text="Process Image", command=process_image)
process_button.grid(row=4, column=0, columnspan=3, padx=5, pady=5)

root.mainloop()
