import math
import numpy as np


from processs import calculate_points
from diagram import Diagram
from file_folder import Folder

folder = Folder()
diagram = Diagram()

if __name__ == "__main__":
    t=input()

    for i in range(t):
        A,B,C= map(int, raw_input().split(','))
        (Ax,Ay),(Bx,By),(Cx,Cy), (Dx,Dy) = calculate_points(A,B,C)
        quadrilateral_diagram_path = diagram.get_quadrilateral((Ax,Ay),(Bx,By),(Cx,Cy), (Dx,Dy))
        diagram.save(quadrilateral_diagram_path,str(i))
