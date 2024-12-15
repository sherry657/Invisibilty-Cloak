import cv2
import numpy as np
import customtkinter as ctk
from PIL import Image, ImageTk


cap = cv2.VideoCapture(0)

# Wait for a few seconds to capture the background
print("Capturing background. Please ensure the cloak is not in the frame.")
for i in range(30):
    ret, background = cap.read()
if not ret:
    print("[ERROR] Failed to capture background.")
    cap.release()
    exit()
background = cv2.flip(background, 1)


ctk.set_appearance_mode("Dark")  # Modes: "System", "Dark", "Light"
ctk.set_default_color_theme("dark-blue")  # Themes: "blue", "dark-blue", "green"

root = ctk.CTk()
root.title("Invisibility Cloak GUI")
root.geometry("1000x700")

# Frame for controls
control_frame = ctk.CTkFrame(root, width=300, height=700, corner_radius=15)
control_frame.pack(side="left", fill="y", padx=10, pady=10)

# Frame for video feed
video_frame = ctk.CTkFrame(root, corner_radius=15)
video_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

# Function to update saturation and value sliders dynamically


def update_saturation_and_value_display():
    mid_hue = (hue_min_slider.get() + hue_max_slider.get()) // 2
    
    # Update saturation gradient
    sat_gradient = np.zeros((20, 300, 3), dtype=np.uint8)
    for i in range(300):
        sat_gradient[:, i, :] = [mid_hue, int(i * 255 / 300), 128]
    sat_gradient_bgr = cv2.cvtColor(sat_gradient, cv2.COLOR_HSV2RGB)
    sat_image = Image.fromarray(sat_gradient_bgr)
    sat_image_tk = ImageTk.PhotoImage(image=sat_image)
    sat_canvas.create_image(0, 0, anchor="nw", image=sat_image_tk)
    sat_canvas.image = sat_image_tk

    # Update value gradient
    val_gradient = np.zeros((20, 300, 3), dtype=np.uint8)
    for i in range(300):
        val_gradient[:, i, :] = [mid_hue, 255, int(i * 255 / 300)]
    val_gradient_bgr = cv2.cvtColor(val_gradient, cv2.COLOR_HSV2RGB)
    val_image = Image.fromarray(val_gradient_bgr)
    val_image_tk = ImageTk.PhotoImage(image=val_image)
    val_canvas.create_image(0, 0, anchor="nw", image=val_image_tk)
    val_canvas.image = val_image_tk

# Hue controls
hue_label = ctk.CTkLabel(control_frame, text="Hue Range", font=("Arial", 14))
hue_label.pack(pady=10)

hue_canvas = ctk.CTkCanvas(control_frame, width=250, height=20, bg="white")
hue_canvas.pack(pady=5)
hue_image = Image.open("hue.png").resize((250, 20))
hue_image_tk = ImageTk.PhotoImage(hue_image)
hue_canvas.create_image(0, 0, anchor="nw", image=hue_image_tk)
hue_canvas.image = hue_image_tk

hue_min_slider = ctk.CTkSlider(control_frame, from_=0, to=179, number_of_steps=179, command=lambda v: update_saturation_and_value_display())
hue_min_slider.pack(pady=5)

hue_max_slider = ctk.CTkSlider(control_frame, from_=0, to=179, number_of_steps=179, command=lambda v: update_saturation_and_value_display())
hue_max_slider.set(179)
hue_max_slider.pack(pady=5)

# Saturation controls
sat_label = ctk.CTkLabel(control_frame, text="Saturation", font=("Arial", 14))
sat_label.pack(pady=10)

sat_canvas = ctk.CTkCanvas(control_frame, width=250, height=20, bg="white")
sat_canvas.pack(pady=5)

sat_min_slider = ctk.CTkSlider(control_frame, from_=0, to=255, number_of_steps=255)
sat_min_slider.pack(pady=5)

# Value controls
val_label = ctk.CTkLabel(control_frame, text="Value", font=("Arial", 14))
val_label.pack(pady=10)

val_canvas = ctk.CTkCanvas(control_frame, width=250, height=20, bg="white")
val_canvas.pack(pady=5)

val_min_slider = ctk.CTkSlider(control_frame, from_=0, to=255, number_of_steps=255)
val_min_slider.pack(pady=5)

# Video display in GUI
video_label = ctk.CTkLabel(video_frame, text="")
video_label.pack(fill="both", expand=True)

# Function to process the video stream
def process_frame():
    global background

    # Read a frame from the webcam
    ret, frame = cap.read()
    if not ret:
        print("[ERROR] Failed to read from webcam.")
        root.quit()
        return

    frame = cv2.flip(frame, 1)
    hsv = cv2.bilateralFilter(frame, d=15, sigmaColor=75, sigmaSpace=75)
    # Convert frame to HSV
    hsv = cv2.cvtColor(hsv, cv2.COLOR_BGR2HSV)

    # Get HSV range from sliders
    lower_bound = np.array([hue_min_slider.get(), sat_min_slider.get(), val_min_slider.get()])
    upper_bound = np.array([hue_max_slider.get(), 255, 255])
    hsv = cv2.GaussianBlur(hsv, (15, 15), 0)
    # Create a mask for the selected color
    
    mask = cv2.inRange(hsv, lower_bound, upper_bound)

    # Morphological operations to remove noise
    kernel = np.ones((3, 3), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=2)
    mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, kernel, iterations=1)
    mask = cv2.dilate(mask, kernel, iterations=1)
    # Invert the mask
    mask_inv = cv2.bitwise_not(mask)

    # Extract the cloak region from the background
    cloak = cv2.bitwise_and(background, background, mask=mask)

    # Extract the non-cloak region from the current frame
    non_cloak = cv2.bitwise_and(frame, frame, mask=mask_inv)

    # Combine the two regions
    result = cv2.addWeighted(cloak, 1, non_cloak, 1, 0)

    # Convert the result to an image format compatible with Tkinter
    result_rgb = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(result_rgb)
    imgtk = ImageTk.PhotoImage(image=img)

    # Display the image in the GUI
    video_label.imgtk = imgtk
    video_label.configure(image=imgtk)

    # Call this function again after 10 ms
    video_label.after(10, process_frame)

# Start processing the video stream
process_frame()

# Run the GUI event loop
root.mainloop()

# Release resources
cap.release()
cv2.destroyAllWindows()
