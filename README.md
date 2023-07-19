# OpenGL-RotatingDog
Focuses on exploring transformations and poly-line drawings using OpenGL. We will read data from a file containing vertex positions that form the poly-line representation of a dog's image. The dog's image will be drawn at eight different points along a circle, and each dog will appear to spin in place.

## How to Run

1. Install the required libraries using the following command (if you haven't already):

```bash
pip install glfw PyOpenGL
```

2. Run the script:

```bash
python dog_spin.py
```

## Specifications

- Viewing Volume: (left, right, bottom, top) = (0, 60, 0, 60)
- Background Color: White
- Poly-Line Color: Black
- Circle Center: (30, 30)
- Circle Radius: 25

## Poly-Line Drawing

The `dog.txt` file contains space-separated floating-point numbers representing the (x, y) positions of the vertices forming the poly-line representation of a dog's image. The program will draw this poly-line image at eight different points along a circle with a radius of 25, centered at (30, 30). Each dog will be rotated counterclockwise by 1° in each frame, making them appear to spin in place.

