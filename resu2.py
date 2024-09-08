from manim import *
class resu2(Scene):
    def construct(self):
        integral= MathTex(r"\int \frac{xcos(x)}{(xsen(x)+cos(x)-1)^m}dx")
        integral1= MathTex(r"\int \frac{xcos(x)}{(xsen(x)+cos(x)-1)^m}dx",font_size=35)
        integral1.to_corner(UL)
        self.play(Write(integral) ,run_play=5)
        self.wait(2)   
        self.play(Transform(integral, integral1),run_time=2)
        self.wait(2)
        u= MathTex("u = xsen(x)+cos(x)-1",
                   "du = (sen(x)+xcos(x)-sen(x))dx",
                   "= xcos(x)dx",
                   "du = xcos(x)dx",
                   font_size=35)
        deriva= Text("derivamos", font_size=20)
        u[0].move_to(3*UP+ RIGHT)
        u[1].move_to(2*UP)
        u[2].move_to(2*UP + 4*RIGHT)
        u[3].move_to(2*UP)
        deriva.move_to(2.5*UP + 3.5*RIGHT) 
        self.play(Write(u[0]),run_play=8)
        self.play(Write(deriva),run_play=2)
        self.play(Write(u[1]),run_play=8)
        self.play(Write(u[2]),run_play=8)
        self.wait(2)
        self.play(Transform(u[1],u[3]),Transform(u[2],u[3]))
        self.wait(2)

        a = MathTex(r"\int \frac{xcos(x)}{(xsen(x)+cos(x)-1)^m",font_size=50)
        a.to_corner(UL)

        b = MathTex("u=xsen(x)+cos(x)-1",font_size=50)
        b.to_corner(UR)
        
        c = MathTex("du=xcos(x)dx",font_size=50)
        c.move_to(4*UR + 2*DOWN)

        inteu= MathTex(r"\int \frac{du}{u^m}",
                       r"=\int u^{-m} du",
                            r"=\frac{u^{1-m}}{1-m}+ C",
                            font_size=50)
        inteu[0].move_to(5*LEFT)
        inteu[1].move_to(2.7*LEFT)
        inteu[2].move_to(IN + 0.5*RIGHT)

        self.remove(u[1],u[2])
        self.play(Transform(deriva,inteu[0]),Transform(u[0],b),Transform(u[3],c),Transform(integral,a),run_play=3)
        self.wait()
        self.play(Write(inteu[1]))

        recordar= MathTex("Recordar:",
                          r"\int u^{n} du",
                          r"=\frac{u^{n+1}}{n+1}",
                          r";  n \neq -1", font_size=45)
        recordar[0].move_to(2*DOWN + 4*LEFT)
        recordar[1].move_to(2*DOWN + 2*LEFT)
        recordar[2].move_to(2*DOWN)
        recordar[3].move_to(2*DOWN + 2*RIGHT)
        self.wait()
        self.play(Write(recordar[0]),run_play=5)
        self.wait()
        self.play(Write(recordar[1]),run_play=5)
        self.play(Write(recordar[2]),run_play=5)
        self.play(Write(recordar[3]),run_play=3)
        self.wait()
        self.play(Transform(recordar,inteu[2]),run_play=5)
        self.wait(2)

        rempla = MathTex("Remplazamos:",r"\frac{u^{1-m}}{1-m}+ C",r"=\frac{(xsen(x)+cos(x)-1)^{1-m}}{1-m}+ C",font_size=40)
        rempla[0].move_to(2*DOWN + 4*LEFT)
        rempla[1].move_to(2*DOWN + 1.3*LEFT)
        rempla[2].move_to(2*DOWN + 3*RIGHT)
        self.play(Write(rempla[0]),run_play=8)
        self.wait()
        self.play(Write(rempla[1]),run_play=8)
        self.play(Write(rempla[2]),run_play=8)
        self.wait(3)

        resu=MathTex(r"\int \frac{xcos(x)}{(xsen(x)+cos(x)-1)^m}dx",r"=\frac{(xsen(x)+cos(x)-1)^{1-m}}{1-m}+ C",font_size=46)
        self.play(Transform(rempla,resu),Transform(inteu,resu),Transform(u,resu),Transform(integral,resu),Transform(deriva,resu),Transform(recordar,resu),Transform(a,resu),Transform(b,resu),Transform(c,resu))
        self.wait(8)