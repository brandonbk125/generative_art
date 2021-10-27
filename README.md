# generative_art

# What is this program?
This program is exploring how different hash functions can be visualised using a unique type of art generation, by drawing lines based on the hash that each function will create given the same string input.

# How does it work?
This program uses the hashlib library to implement the different hash functions 
```python 
import hashlib
```

and uses PIL in order to create the image, draw the lines and save the image. 
 
```python
from PIL import Image
```

Each character of the hash is converted into a co-ordinate that will be used by the program to draw the lines.
It uses the normalise() function to make sure the range of numbers from the hash will make an even distribution across the canvas. Then, when the lines are plotted the program will draw a line between each nearest neighbour and another line between the nearest neighbours nearest neighbour.
I used the spatial import from the scipy library
```python
from scipy import spatial
```
 to calculate the nearest neighbours by putting the co-ordinates into a [KDTree](https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.KDTree.html).

# Thoughts so far + possible future updates

The results from this program are very interesting in my opinion and a slight change in the normalise() function calculation can change the outcome so drastically. In the current state of the program it only deals with a black background and white lines. I am still considering how to compute this information for each hash. Potentially having a different colour for each line wouldn't look very good so I need to think about this some more. Maybe computing a start colour and an end colour and having a gradient for the background. Not sure how to deal with the line colours yet, although I quite like the black and white for now it has a lot of room for creativity with different colours. I will update the code when I have come up with a good idea. Need to research colour spectrum calculations more because RGB would probably make for some boring/silly outcomes.
