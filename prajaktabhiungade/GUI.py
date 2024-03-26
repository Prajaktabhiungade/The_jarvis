import tkinter as tk
from PIL import Image, ImageTk
import pyttsx3

class GUI:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.root = tk.Tk()
        self.root.title("JarvisUI")

        # Load and display image
        image = Image.open("C:\Desktop\The_jarvis\prajaktabhiungade\image.jpg")  # Change the path to your image
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(self.root, image=photo)
        image_label.image = photo
        image_label.pack()

        self.root.mainloop()

if __name__ == "__main__":
    app = GUI()





