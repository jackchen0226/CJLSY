# CJLSY
Repository for team CJLSY for ECE 101

## 01-arm-angles.py

This is for the first project of ECE 101 where we create a two jointed arm.
A cartesian point is given and one must find angles of the arm's shoulder and elbow in order to have the arm make a mark at the given point.
In order to do this one must use trigonometric equations to do so. Because the triangle produced by the radius
of the given points and the two arms, which have the same length, is an isoceles triangle the program will use trigonometry to find the angles
of the shoulder and elbow.

### Installing Respository

Like most git repositories, this one can also be cloned onto your machine.

`git clone https://github.com/jackchen0226/CJLSY.git`

This code is also needs **Python 3.6** or higher, which can be downloaded [here](https://www.python.org/downloads/release/python-363/).
Make sure that you also select to install pip if on *Windows*, this will be important later.

If on linux, python can be installed with apt with sudo permissions.

`sudo apt-get install python3`

### Dependencies

`01-arm-angles.py` has a single dependency, [click](http://click.pocoo.org/5/), in order for better shell input. Click can be installed through pip

```
sudo apt-get install pip
pip install click
```

### How to use

When this repository is cloned, `01-arm-angles.py` will not initially run. This is because the length of the arm must be set first. This can be done
with `set-arm-length.py`.

```
python3 set-arm-length.py
Set length of arm:
```

This will pickle the length of the arm into a .pkl file, "armlengths.pkl" which `01-arm-angles.py` utilizes.

```
python3 01-arm-angles.py`
X value?:
Y value?:
Shoulder angle: #, Elbow angle: #
```
