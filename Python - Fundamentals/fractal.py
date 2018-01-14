__author__ = "Prikly Grayp"
__license__ = "MIT"
__version__ = "1.0.0"
__email__ = "priklygrayp@gmail.com"
__status__ = "Development"

'''Computing Mandelbrot sets.'''

import math
def mandel(real, imag):
    '''Compute a point in the Mandelbrot.

    The logarithm of number of iterations needed to determine whether a complex point is in the Mandelbrot set.

    Args:
        real: The real coordinate
        imag: The imaginary coorinate

    Returns:
        An integer in the range 1-255.
    '''
    x = 0
    y = 0
    for i in range(1, 257):
        if x * x + y * y > 4.0:
            break
        xt = real + x*x - y * y
        y = imag + 2.0 * x * y
        x = xt
    return  int(math.log(i) * 256 / math.log(256)) -1

def mandelbrot(size_x, size_y):
    '''Make a Mandelbrot set image.

    Args:
        size_x: Image width
        size_y = Image height

    Returns:
        A lsit of lists of integers in the range 0-255.
    '''
    return [[mandel((3.5 * x / size_x) - 2.5,
                    (2.0 * y / size_y) - 1.0)
             for x in range(size_x)]
            for y in range(size_y)]

pixels = mandelbrot(448, 256)
print(pixels)

import bmp
bmp.write_grayscale('mandel.bmp', pixels)
print(bmp.dimentions('mandel.bmp'))