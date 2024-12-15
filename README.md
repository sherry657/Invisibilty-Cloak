
# 🕊️ Invisibility Cloak with Real-Time GUI

A dynamic invisibility cloak implementation using webcam feed and real-time background subtraction with customizable HSV (Hue, Saturation, Value) range adjustments.

---

## 📜 Overview

This project creates an **invisibility cloak effect** using OpenCV and a graphical user interface with `customtkinter`. The GUI allows users to dynamically select the range of Hue, Saturation, and Value to adjust the invisibility cloak effect in real time.

---

## 🛠️ Features

- **Dynamic HSV Adjustments**: Allows users to select a range for Hue, Saturation, and Value to make the cloak effect more adaptable.
- **Real-Time Processing**: Processes webcam feed in real time.
- **User-friendly GUI**: Customizable with sliders for interactive experience.
- **Background Subtraction**: Seamlessly integrates real-time webcam input with pre-captured background.

---

## 💻 Installation Instructions

### Requirements
Make sure you have Python 3.x installed on your system.

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/<sherry657>/Invisibilty.git
   cd Invisibilty.git
   ```

2. **Install Required Libraries**:
   Ensure you have the following dependencies:
   ```bash
   pip install opencv-python-headless numpy customtkinter pillow
   ```

---

## 🚀 Usage

1. **Launch the Program**:
   Run the Python script:
   ```bash
   python main.py
   ```

2. **Configure HSV Ranges Dynamically**:
   - Use sliders in the GUI to adjust the hue, saturation, and value ranges dynamically.
   - Observe changes in real time as they affect the invisibility cloak effect.

---

## 🎨 GUI Controls

- **Hue Range Sliders**:
  Adjust the minimum and maximum Hue values to refine which color is treated as "cloak" color.
  
- **Saturation & Value Sliders**:
  Dynamically change these values to alter the invisibility effect intensity and the cloak's color masking.

---

## 📸 Screenshot Preview

Media\gui.png

---

## 🛠️ Built With

- [OpenCV](https://opencv.org/) - Real-time computer vision library.
- [customtkinter](https://pypi.org/project/customtkinter/) - For creating intuitive GUI controls.
- [NumPy](https://numpy.org/) - Numerical computing for array manipulation.

---

## 🖇️ Dependencies

- OpenCV
- NumPy
- customtkinter
- Pillow (PIL)

---

## ⚠️ Troubleshooting

1. **Webcam Not Found**:
   - Ensure the webcam is connected.
   - Restart the application.

2. **Sliders Not Working**:
   - Ensure all required dependencies are installed.

3. **Error with `customtkinter`**:
   - Ensure you have the latest version installed:
     ```bash
     pip install --upgrade customtkinter
     ```

---


## 🤝 Contributions

Contributions are welcome! If you find a bug or have an idea for an enhancement, feel free to open an issue or submit a pull request.

---

