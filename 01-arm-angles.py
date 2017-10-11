#TODO Convert numpy to math library
import math
#import numpy as np
import pickle

# These should be equal
LENGTH_FOREARM = 9
LENGTH_BICEP = 9

def cosines_law_(A, B, C):
    #return np.degrees(np.arccos(((C**2 - A**2 - B**2)/(-2 * A * B))))
    return math.degrees(math.acos((C**2 - A**2 - B**2)/(-2 * A * B)))

def sines_law_(c_, length):
    #return np.degrees(np.arcsin(length * c_))
    return math.degrees(math.asin(length * c_))

import click

@click.command()
@click.option('--x', prompt='X value?', help='The x value of a cartesian point')
@click.option('--y', prompt='Y value?', help='The y value of a cartesian point')

def cart_to_angles(x, y, l1=LENGTH_FOREARM, l2=LENGTH_BICEP):
    # Remember to convert radians = degrees, np.degrees
    x = int(x)
    y = int(y)
    r = math.sqrt(x ** 2 + y ** 2)
    # theta1 is the angle bound by origin
    # theta2 is angle found near the cartesian point
    theta1 = math.asin(y/r)
    theta2 = math.asin(x/r)

    # Law of Cosines: C ** 2 = A ** 2 + B ** 2 - 2ABcos(c)
    # Rewritten: arccos((C ** 2 - A ** 2 - B ** 2)/(-2 * A * B))
    
    elbow_angle = cosines_law_(l1, l2, r)

    # Law of Sines: sin(a)/A = sin(b)/B = sin(c)/C
    # sin(c)/C = c_, Rewritten: b = arcsin(Bc_), a = arcsin(Ac_)
    #TODO: check if below works with ALL cartesian points => theta1
    shoulder_angle = sines_law_(math.sin(math.radians(elbow_angle))/r, l1) + theta1
    print(elbow_angle)
    print(shoulder_angle)
    return elbow_angle, shoulder_angle

if __name__ == '__main__':
    print(cart_to_angles())
