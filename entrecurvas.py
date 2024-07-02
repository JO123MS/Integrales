from manim import *

class Area(Scene):
    def construct(self):
        #Creacion de el plano
        ax = Axes(
            x_range=[-2, 2],
            y_range=[0, 3],
            x_axis_config={"numbers_to_include": [-1,0,1]},
            y_axis_config={"numbers_to_include": [0,1,2,3,]},
            tips=False,
        )
        labels = ax.get_axis_labels()

        #Creacion de las funciones
        funcionfx = ax.plot(
            lambda x:  (1  + (2*x+2)**2 )**0.5, 
            x_range=[-1, 0], 
            color=GREEN_B)
        funciongx = ax.plot(
            lambda x: 0*x,
            x_range=[-1, 0],
            color=WHITE,
        )

        #Objetos extras(lineas)
        linea1 = ax.get_vertical_line(ax.input_to_graph_point(-1, funcionfx), color=YELLOW)
        linea2 = ax.get_vertical_line(ax.i2gp(0, funcionfx), color=YELLOW)

        #Creacion del Area
        area = ax.get_area(funcionfx, [-1, 0], bounded_graph=funciongx, color=BLUE_C, opacity=0.5)
        
        #Nos da la imagen, la imagen luego se guada en la carpeta del video
        self.add(ax, labels, funcionfx, funciongx, linea1, linea2, area)
