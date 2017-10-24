
import math
import pickle

pkl = open('armlengths.pkl', 'rb')
LENGTH_ARM = pickle.load(pkl)
pkl.close() 

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
# Click allows for input in the shell

@click.command()
@click.option('--x', prompt='X value?', help='The x value of a cartesian point')
@click.option('--y', prompt='Y value?', help='The y value of a cartesian point')

def cart_to_angles(x, y, l1=LENGTH_ARM):
    # Remember to convert radians = degrees, np.degrees
    x = int(x)
    y = int(y)
    r = math.sqrt((x ** 2) + (y ** 2))
    # theta1 is the angle bound by origin

    theta1 = math.degrees(math.asin(y/r))
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

