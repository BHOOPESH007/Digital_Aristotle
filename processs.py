import numpy as np
from mathematics import get_ten
from qadrilateral import Diagram
diagram = Diagram()

def calculate_points(A,B,C):
    D=360-(A+B+C)
    Ax=25
    Ay=25
    Bx=50
    By=25
    Cy=50
    Cx=(Bx*get_ten(B)+By-Cy)/get_ten(B)

    if B+C<180:
        angel_C_with_A = 180-(A+B)

    elif B+C>180:
        angel_C_with_A = 360-(A+B)

    elif B+C==180:
        angel_C_with_A = 0
    Dx = np.array([[get_ten(angel_C_with_A), -1],[get_ten(A), -1]])
    Dy = np.array([Cx*get_ten(angel_C_with_A)-Cy, Ax*get_ten(A)-Ay])

    Dx,Dy= np.linalg.solve(Dx,Dy)
    return (Ax,Ay),(Bx,By),(Cx,Cy), (Dx,Dy)