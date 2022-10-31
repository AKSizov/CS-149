"""Drawing utilities for Pillow Images.

Author: ???
Version: ???
Honor Code and Acknowledgments:
"""

from PIL import Image


def draw_rectangle(img, x_pos, y_pos, width, height, color):
    """Draw a rectangle onto the provided image.

    Args:
        img (Image): The image to modify
        x_pos: The x-position of the  upper-left corner of the rectangle
        y_pos: The y-position of the  upper-left corner of the rectangle
        width: The width of the rectangle in pixels
        height: The height of the rectangle in pixels
        color: A three-entry tuple representing the color of the rectangle
    """
    pass


def draw_triangle(img, x_pos, y_pos, width, color):
    """Draw a right isosceles triangle onto the provided image.

    Args:
        img: The image to modify
        x_pos: The x-position of the  upper-left corner of the triangle
        y_pos: The y-position of the  upper-left corner of the triangle
        width: The width of the triangle in pixels
        color: A three-entry tuple representing the color of the triangle
    """
    pass


def main():
    """Sample application illustrating image modifications.

    You can test your code by downloading the duke dog image and running this
    function.
    """
    import tkinter as tk
    from tkinter import filedialog

    root = tk.Tk()
    root.withdraw()

    file = filedialog.askopenfilename(title="Select An Image",
                                      initialdir="./",
                                      initialfile="dog.jpg",
                                      filetypes=[("Image files",
                                                  ".jpg .JPG .png")])

    im1 = Image.open(file)
    im2 = im1.copy()

    draw_rectangle(im1, 0, 0, 100, 120, (255, 0, 0))
    draw_triangle(im2, 0, 0, 100, (255, 0, 0))
    im1.show()
    im2.show()


if __name__ == "__main__":
    main()
    quit()
