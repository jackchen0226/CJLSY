#TODO Convert numpy to math library
import math
#import numpy as np
import pickle

# These should be equal
LENGTH_FOREARM = 9
LENGTH_BICEP = 9

def cosines_law_(A, B, C):
    #return np.degrees(np.arccos(((C**2 - A**2 - B**2)/(2 * A * B))))
    n = float(C**2) - (A**2) - (B**2)
    d = float(2 * A * B)
    print(n, d)
    return math.acos(n / d)

def sines_law_(C, c, length):
    #return np.degrees(np.arcsin(length * c_))
    return math.asin(length * (math.sin(c)/C))

def isoceles_angle(arm_length, base):
    height = math.sqrt((arm_length**2) - ((base/2.0)**2))
    return math.atan(2*height/base)
import click

@click.command()
@click.option('--x', prompt='X value?', help='The x value of a cartesian point')
@click.option('--y', prompt='Y value?', help='The y value of a cartesian point')

def cart_to_angles(x, y, l1=LENGTH_FOREARM, l2=LENGTH_BICEP):
    # Remember to convert radians = degrees, np.degrees
    x = int(x)
    y = int(y)
    r = math.sqrt((x ** 2) + (y ** 2))
    # theta1 is the angle bound by origin
    # theta2 is angle found near the cartesian point
    theta1 = math.degrees(math.asin(y/r))
    theta2 = math.asin(x/r)
    print(theta1)
    # Law of Cosines: C ** 2 = A ** 2 + B ** 2 - 2ABcos(c)
    # Rewritten: arccos((C ** 2 - A ** 2 - B ** 2)/(2 * A * B))
    
    elbow_angle = math.degrees(cosines_law_(l1, l2, r))
    # Law of Sines: sin(a)/A = sin(b)/B = sin(c)/C
    # sin(c)/C = c_, Rewritten: b = arcsin(Bc_), a = arcsin(Ac_)
    #TODO: check if below works with ALL cartesian points => theta1
    shoulder_angle = math.degrees(isoceles_angle(l1, r))
    elbow_angle = 180. - 2*shoulder_angle
    if x < 0 and y > 0:
        print('thr')
        # Quadrant 2
        theta1 += 90.
    elif x < 0 and y < 0:
        # Quadrant 3
        theta1 = -theta1
        theta1 += 180.
        print(theta1)
    elif x > 0 and y < 0:
        # Quadrant 4
        theta1 = -theta1
        theta1 += 270.

    shoulder_angle += theta1
    if shoulder_angle > 360.:
        shoulder_angle -= 360.

    print("Shoulder angle: {}, Elbow angle: {}".format(str(shoulder_angle), str(elbow_angle)))
    

if __name__ == '__main__':
    cart_to_angles()

