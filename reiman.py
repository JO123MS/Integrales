from manim import *

class Reimann(Scene):
    def construct(self):
        text1 = Text("Sumas de Reimann")
        self.play(Write(text1),run_time=2)
        self.wait(2)
        fx= MathTex(r" f(x)=x^2 -x + 1","f(x)")
        fx[0].move_to(0.5*DOWN + 4.3*LEFT)
        fx[1].move_to(0.5*DOWN + 3.4*LEFT)
        text2 = Text("Sumas de Reimann",font_size=40)
        text2.move_to(3*UL + LEFT)
        self.play(Transform(text1,text2),run_play=3)

        # Animacion de grafica
        ax = Axes(
            x_range=[-2, 4],
            y_range=[0, 8],
            x_axis_config={"numbers_to_include": [-2,-1,0,1,2,3,4]},
            y_axis_config={"numbers_to_include": [0,1,2,3,4,5,6,7,8]},
            tips=False,
        )

        labels = ax.get_axis_labels()

        curve_1 = ax.plot(lambda x: x ** 2 - x + 1, x_range=[-1, 3], color=BLUE_C)
        curve_2 = ax.plot(lambda x: 0 * x , x_range=[-1, 3],color=WHITE)

        line_1 = ax.get_vertical_line(ax.input_to_graph_point(-1, curve_1), color=YELLOW)
        line_2 = ax.get_vertical_line(ax.input_to_graph_point(3, curve_1), color=YELLOW)
        riemann_area = ax.get_riemann_rectangles(curve_1, x_range=[-1, 3], dx=0.1, color=BLUE, fill_opacity=0.5)
        self.add(ax, labels, curve_1, curve_2, line_1, line_2)
        self.add(riemann_area)

        self.play(Write(fx[0]),run_play=3)
        self.play(Transform(fx[0],fx[1]),run_play=3)

        num=0.1
        veces=8 
        for _ in range(veces):
            num -= 0.01
            riemann_area2 = ax.get_riemann_rectangles(curve_1, x_range=[-1, 3], dx=num, color=BLUE, fill_opacity=0.5)
            self.play(Transform(riemann_area, riemann_area2))
            
        self.wait(2)
        area = ax.get_area(curve_1, [-1, 3], bounded_graph=curve_2, color=BLUE, opacity=0.5)
        
        self.play(Transform (riemann_area2,area),Transform(riemann_area,area))
        self.wait(2)

        self.remove(ax, labels, curve_1, curve_2, line_1, line_2,area,riemann_area,fx[0],fx[1],riemann_area2)
        text3 = Text("Utilizamos la definicion de sumas de Reimann:",font_size=30)
        text3.move_to(2.3*UP + 2*LEFT)
        self.play(Write(text3),run_play=3)
        teoria=MathTex(r"\int_{a}^{b}f(x)dx = \displaystyle \lim_{n \to \infty } \sum_{i=1}^{n}f(x_{i})\Delta x",
                     "Donde: ",r"\Delta x =\frac{b-a}{n}",r"x_{i}=a+i\Delta x")
        teoria[0].move_to(1.3*UP+3*LEFT)
        self.play(Write(teoria[0]))
        teoria[1].move_to(1.5*UP+1.7*RIGHT)
        teoria[2].move_to(0.7*UP + 1.5*RIGHT)
        teoria[3].move_to(0.7*UP +4.5*RIGHT)
        self.play((Write(teoria[1])),(Write(teoria[2])),(Write(teoria[3])))
        self.wait()
        rempla=MathTex("Reemplazamos: ",r"\Delta x =\frac{3-(-1)}{n}",
                       r"\Delta x =\frac{4}{n}",r"x_{i}=-1+i\frac{4}{n}")
        rempla[0].move_to(1.5*UP + 2.5*RIGHT)
        rempla[1].move_to(0.7*UP + 1.5*RIGHT)
        rempla[2].move_to(0.7*UP + 1.5*RIGHT)
        rempla[3].move_to(0.7*UP +4.5*RIGHT)
        self.play(Transform(teoria[1],rempla[0]))
        self.wait()
        self.play(Transform(teoria[2],rempla[1]))
        self.remove(teoria[2])
        self.play(Transform(rempla[1],rempla[2]))
        self.wait()
        self.play(Transform(teoria[3],rempla[3]))
        self.wait()

        resu=MathTex(r" \int_{-1}^{3}(x^{2}-x+1)dx = \displaystyle \lim_{n \to \infty }\sum_{i=1}^{n}f(\frac{4i}{n}-1)\frac{4}{n}",
        r" \int_{-1}^{3}(x^{2}-x+1)dx = \displaystyle \lim_{n \to \infty }\sum_{i=1}^{n}[(\frac{4i}{n}-1)^{2}-(\frac{4i}{n}-1)+1]\frac{4}{n}",
        r"\int_{-1}^{3}(x^{2}-x+1)dx = \displaystyle \lim_{n \to \infty }\sum_{i=1}^{n}[\frac{16i^{2}}{n^{2}}-\frac{12i}{n}+3]\frac{4}{n}",
        r"= \displaystyle \lim_{n \to \infty }[\frac{64}{n^{3}}\sum_{i=1}^{n}i^{2}-\frac{48}{n^{2}}\sum_{i=1}^{n}i+\frac{12}{n}\sum_{i=1}^{n}1]",
        r"= \displaystyle \lim_{n \to \infty }[\frac{64}{n^{3}}(\frac{n(2n+1)(n+1)}{6})-\frac{48}{n^{2}}(\frac{n(n+1)}{2})+\frac{12}{n}(n)]",
        r"= \displaystyle \lim_{n \to \infty }[\frac{32}{3}(2+\frac{1}{n})(1+\frac{1}{n})-24(1+\frac{1}{n})+12]",
        r"=\frac{64}{3}-12",
        r"=\frac{28}{3} u^{2}")
        resu[0].move_to(1.5*UP+2.3*LEFT)
        resu[1].move_to(1.5*UP+0.3*LEFT)
        resu[2].move_to(1.5*UP+LEFT)

        resu[3].move_to(1.5*LEFT)
        resu[4].move_to(0.1*RIGHT)
        resu[5].move_to(1.5*LEFT)

        resu[6].move_to(1.5*DOWN + 3.5*LEFT)
        resu[7].move_to(1.5*DOWN + 1.5*LEFT)

        self.play(Transform(rempla,resu[0]),Transform(teoria,resu[0]),Transform(text3,resu[0]))
        self.wait()
        self.remove(rempla,teoria,text3)
        self.play(Transform(resu[0],resu[1]))
        self.wait()
        self.remove(resu[0])
        self.play(Transform(resu[1],resu[2]))
        self.wait()
        
        self.play(Write(resu[3]))
        self.wait()
        self.play(Transform(resu[3],resu[4]))
        self.wait()
        self.remove(resu[3])
        self.play(Transform(resu[4],resu[5]))
        self.wait()

        self.play(Write(resu[6]))
        self.wait()
        self.play(Write(resu[7]))
        self.wait()