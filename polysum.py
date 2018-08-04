#A regular polygon has n number of sides. Each side has length s.The area of a regular polygon is: (0.25 * n * s**2)/tan(pi/n)
#The perimeter of a polygon is: length of the boundary of the polygon
#Write a function called polysum that takes 2 arguments, n and s. This function should sum the area and square of the perimeter of the regular polygon. The function returns the sum, rounded to 4 decimal places.

import math
def polysum(n, s):
    a = math.pi/n
    area = (0.25 * n * s**2)/(math.tan(a))
    perimeter = n * s
    total = area + (perimeter ** 2)
    rounded_sum = round(total, 4)
    return rounded_sum
    


