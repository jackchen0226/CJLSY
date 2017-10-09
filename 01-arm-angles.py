import numpy as np
import pickle

LENGTH_FOREARM = 9
LENGTH_BICEP = 12

def cosines_law_(A, B, C):
    return np.arccos((C**2 - A**2 - B**2)/(-2 * A * B))

def sines_law_(c_, length):
    return np.degrees(np.arcsin(length * c_))

import click

@click.command()
@click.option('--x', prompt='X value?', help='The x value of a cartesian point')
@click.option('--y', prompt='Y value?', help='The y value of a cartesian point')

def cart_to_angles(x, y, l1=LENGTH_FOREARM, l2=LENGTH_BICEP):
    # Remember to convert radians = degrees, np.degrees
    x = int(x)
    y = int(y)
    r = np.sqrt(x ** 2 + y ** 2)
    # theta1 is the angle bound by origin
    # theta2 is angle found near the cartesian point
    theta1 = np.arcsin(y/r)
    theta2 = np.arcsin(x/r)

    # Law of Cosines: C ** 2 = A ** 2 + B ** 2 - 2ABcos(c)
    # Rewritten: arccos((C ** 2 - A ** 2 - B ** 2)/(-2 * A * B))
    print(l1, l2, r)
    elbow_angle = cosines_law_(l1, l2, r)

    # Law of Sines: sin(a)/A = sin(b)/B = sin(c)/C
    # sin(c)/C = c_, Rewritten: b = arcsin(Bc_), a = arcsin(Ac_)
    #TODO: check if below works with ALL cartesian points => theta1
    shoulder_angle = sines_law_(elbow_angle, l1) + theta1

    return elbow_angle, shoulder_angle

if __name__ == '__main__':
    cart_to_angles()
