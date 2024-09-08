from manim import *
class resu1(Scene):
    def construct(self):
        integral= MathTex(r"\int \frac{3ax^2-2bx}{\sqrt{ax^3-bx^2}}dx")
        integral1= MathTex(r"\int \frac{3ax^2-2bx}{\sqrt{ax^3-bx^2}} dx",font_size=50)
        integral1.to_corner(UL)
        self.play(Write(integral) ,run_play=5)
        self.wait(2)   
        self.play(Transform(integral, integral1),run_time=2)
        self.wait(2)
        
        u= MathTex("u = ax^3 - bx^2","du = (3ax^2 -2bx)dx",font_size=50)
        deriva= Text("derivamos", font_size=30)
        u[0].move_to(3*UP)
        u[1].move_to(2*UP) 
        deriva.move_to(2.5*UP + 3.5*RIGHT) 
        self.play(Write(u[0]),run_play=8)
        self.play(Write(deriva),run_play=2)
        self.play(Write(u[1]),run_play=8)

        inteu= MathTex(r"\int \frac{du}{\sqrt{u}}",font_size=50)
        inteu.move_to(LEFT)
        inteu1= MathTex(r"\int \frac{du}{\sqrt{u}}",
                        r"= \int u^{-\frac{1}{2}} du",
                        r"=\frac{u^\frac{1}{2}}{\frac{1}{2}} + C",
                        r"=2u^{\frac{1}{2}}+C",font_size=50)
        inteu1[0].move_to(5.5*LEFT)
        inteu1[1].move_to(3*LEFT)
        inteu1[2].move_to(IN)
        inteu1[3].move_to(3*RIGHT)
        self.play(Transform(deriva,inteu))
        self.remove(deriva)
        self.play(Transform(inteu,inteu1[0]))
        self.play(Write(inteu1[1]),run_play=3)
        self.wait()

        recordar= MathTex("Recordar:",
                          r"\int u^{n} du",
                          r"=\frac{u^{n+1}}{n+1}")
        recordar[0].move_to(2*DOWN + 4*LEFT)
        recordar[1].move_to(2*DOWN + 2*LEFT)
        recordar[2].move_to(2*DOWN)
        self.play(Write(recordar[0]),run_play=5)
        self.wait()
        self.play(Write(recordar[1]),run_play=5)
        self.play(Write(recordar[2]),run_play=8)
        self.wait()
        self.play(Transform(recordar,inteu1[2]),run_play=5)
        self.play(Write(inteu1[3]),run_play=8)
        self.wait()

        rempla = MathTex("Remplazamos:",r"2u^{\frac{1}{2}}+C",r"=2\sqrt{ax^3-bx^2}+C")
        rempla[0].move_to(2*DOWN + 4*LEFT)
        rempla[1].move_to(2*DOWN + LEFT)
        rempla[2].move_to(2*DOWN + 2.5*RIGHT)
        self.play(Write(rempla[0]),run_play=8)
        self.wait()
        self.play(Write(rempla[1]),run_play=8)
        self.play(Write(rempla[2]),run_play=8)
        self.wait(2)

        resu=MathTex(r"\int \frac{3ax^2-2bx}{\sqrt{ax^3-bx^2}}dx",r"=2\sqrt{ax^3-bx^2}+C")
        self.play(Transform(rempla,resu),Transform(inteu1,resu),Transform(u,resu),Transform(integral,resu),Transform(deriva,resu),Transform(recordar,resu),Transform(inteu,resu))
        self.wait(8)