from manim import *
class resu3(Scene):
    def construct(self):
        integral= MathTex(r"\int \frac{dx}{\sqrt{(1+x^2)(ln(x+\sqrt{1+x^2}))}}")
        integral1= MathTex(r"\int \frac{dx}{\sqrt{(1+x^2)(ln(x+\sqrt{1+x^2}))}}",font_size=35)
        integral1.to_corner(UL)
        self.play(Write(integral) ,run_play=5)
        self.wait(2)   
        self.play(Transform(integral, integral1),run_time=2)
        self.wait(2)

        u= MathTex(r"u = x+\sqrt{1+x^2}",
                   r"du = (1+\frac{2x}{2\sqrt{1+x^2}})dx",
                   r"du= (1+\frac{x}{\sqrt{1+x^2}})dx",
                   r"= (\frac{\sqrt{1+x^2}+x}{\sqrt{1+x^2}})dx",
                   r"=(\frac{u}{\sqrt{1+x^2}})dx",
                   r"\frac{du}{u}=\frac{dx}{\sqrt{1+x^2}}",
                   font_size=35)
        deriva= Text("derivamos", font_size=20)
        u[0].move_to(3*UP+ RIGHT)
        u[1].move_to(2*UP+ RIGHT)
        u[2].move_to(2*UP+ RIGHT)
        u[3].move_to(2*UP + 4.5*RIGHT)
        u[4].move_to(2*UP + 4.5*RIGHT)
        u[5].move_to(2*UP+ RIGHT)
        deriva.move_to(3*UP + 3.5*RIGHT) 
        self.play(Write(u[0]),run_play=8)
        self.play(Write(deriva),run_play=2)
        self.play(Write(u[1]),run_play=8)
        self.wait()
        self.play(Transform(u[1],u[2]),run_play=8)
        self.wait(2)
        self.play(Write(u[3]),run_play=8)
        self.wait()
        self.play(Transform(u[3],u[4]))
        self.wait(2)
        self.play(Transform(u[4],u[5]),Transform(u[3],u[5]),Transform(u[1],u[5]))
        self.wait(2)

        inteu= MathTex(r"\int \frac{du}{u\sqrt{ln(u)}}",
                       r"\int \frac{dv}{\sqrt{v}}",
                       r"=\int v^{-\frac{1}{2}}dv",
                       r"=\frac{v^\frac{1}{2}}{\frac{1}{2}}+C",
                       r"=2v^\frac{1}{2}+C",
                       font_size=35)
        inteu[0].move_to(5*LEFT)
        inteu[1].move_to(5*LEFT)
        inteu[2].move_to(3.5*LEFT)
        inteu[3].move_to(1.5*LEFT)
        inteu[4].move_to(1.5*LEFT)
        self.play(Transform(deriva,inteu[0]),run_play=3)
        self.wait(2)

        v= MathTex(r"v= ln(u)",
                   r"dv= \frac{du}{u}",
                   font_size=35)
        v[0].move_to(RIGHT)
        v[1].move_to(DOWN + RIGHT)
        self.play(Write(v[0]))
        self.play(Write(v[1]))
        self.wait(2)
        self.remove(deriva)
        self.play(Transform(inteu[0],inteu[1]))
        self.wait()
        self.play(Write(inteu[2]))

        recordar= MathTex("Recordar:",
                          r"\int u^{n} du",
                          r"=\frac{u^{n+1}}{n+1}",font_size=45)
        recordar[0].move_to(2*DOWN + 4*LEFT)
        recordar[1].move_to(2*DOWN + 2*LEFT)
        recordar[2].move_to(2*DOWN)
        self.wait()
        self.play(Write(recordar[0]),run_play=5)
        self.wait()
        self.play(Write(recordar[1]),run_play=5)
        self.play(Write(recordar[2]),run_play=8)
        self.wait()
        self.play(Transform(recordar,inteu[3]),run_play=5)
        self.wait(2)
        self.remove(recordar)
        self.play(Transform(inteu[3],inteu[4]))
        self.wait(2)

        rempla = MathTex("Remplazamos:",
                         r"2v^\frac{1}{2}+C",
                         r"=2(ln(u))^\frac{1}{2}+C",
                         r"2(ln(u))^\frac{1}{2}+C",
                         r"=2\sqrt{(ln(x+\sqrt{1+x^2}))}+C",font_size=40)
        rempla[0].move_to(2*DOWN + 4*LEFT)
        rempla[1].move_to(2*DOWN + 1.3*LEFT)
        rempla[2].move_to(2*DOWN + RIGHT)
        rempla[3].move_to(2*DOWN + LEFT)
        rempla[4].move_to(2*DOWN + 3.3*RIGHT)
        self.play(Write(rempla[0]),run_play=8)
        self.wait()
        self.play(Write(rempla[1]),run_play=8)
        self.play(Write(rempla[2]),run_play=8)
        self.wait(2)
        self.play(Transform(rempla[1],rempla[3]),Transform(rempla[2],rempla[3]))
        self.play(Write(rempla[4]),run_play=8)
        self.wait(3)

        resu=MathTex(r"\int \frac{dx}{\sqrt{(1+x^2)(ln(x+\sqrt{1+x^2}))}}",r"=2\sqrt{(ln(x+\sqrt{1+x^2}))}+C",font_size=46)
        self.play(Transform(rempla,resu),Transform(inteu,resu),Transform(u,resu),Transform(integral,resu),Transform(v,resu),Transform(recordar,resu))
        self.wait(8)