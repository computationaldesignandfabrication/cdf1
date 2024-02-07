from compas.geometry import Point, Vector, Frame, Line, Circle
from compas_viewer import Viewer
from compas.colors import Color

from random import random


viewer = Viewer(width=1000, height=1000, viewmode="top", show_grid=False)

w=h=15

face = Circle(radius=w/2, frame=Frame(Point(0, 0, 0), Vector(1, 0, 0), Vector(0, 1, 0)))
eye_left = Line(Point(w/8,0,0), Point(w/3,0,0))
eye_right = Line(Point(-w/8,0,0), Point(-w/3,0,0))
mouth = Line(Point(-w/6,-h/6,0), Point(w/6,-h/6,0))


viewer.add(face, linescolor=Color.black())
viewer.add(eye_left, linescolor=Color.black())
viewer.add(eye_right, linescolor=Color.black())
viewer.add(mouth, linescolor=Color.black())


viewer.show()