import time
from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color

from file_folder import Folder
folder=Folder()

class Diagram():

    def get_quadrilateral(self, (Ax,Ay),(Bx,By),(Cx,Cy),(Dx,Dy)):
        with Drawing() as draw:
            draw.stroke_width = 2
            draw.stroke_color = Color('black')
            draw.fill_color = Color('white')
            points = [(Ax,Ay),(Bx,By),(Cx,Cy),(Dx,Dy)]
            
    #         points = [(25, 25),(75, 25),(75,75), (25, 75)]
            draw.polygon(points)

            with Image(width=100, height=100, background=Color('lightblue')) as image:
                draw(image)
                file_name = 'Quad.gif'
                image.save(filename=file_name)
        return file_name
    
    def save(self, file_name, position):
        fileName, ext= file_name.split('.')
        source = file_name
        destination = folder.getOrCreate('Diagram')+ '/' +fileName+'_'+ position + ext
        folder.file_rename(source, destination)