from typing_extensions import runtime
from manim import *


class Euklid(Scene):
    def construct(self):
        skalering = .5
        bredde, hoyde = 19*skalering, 12*skalering
        rektangel = Rectangle(height=hoyde, width=bredde)
        bredde_tekst, hoyde_tekst = MathTex(int(
            bredde/skalering)).move_to(DOWN*3.5), MathTex(int(hoyde/skalering)).move_to(LEFT * 5.5)

        self.play(Write(rektangel))
        self.play(Write(bredde_tekst), Write(hoyde_tekst))
        senter = rektangel.get_center() + DOWN * hoyde/2 + LEFT * bredde/2
        arc1 = Arc(start_angle=PI/2, angle=-PI/2,
                   radius=hoyde, arc_center=senter)

        self.play(Write(arc1), run_time=3)

        dot = Dot(point=senter + RIGHT*hoyde).set_color(RED)
        self.play(Write(dot))
        self.play(FadeOut(arc1))

        bredde, hoyde = 7*skalering, 12*skalering
        rektangel = Rectangle(height=hoyde, width=bredde).move_to(RIGHT*3)
        self.bring_to_back(rektangel)
        self.play(Write(rektangel))
        self.play(FadeOut(dot))
        self.play(ApplyMethod(bredde_tekst.set_opacity, .5),
                  ApplyMethod(hoyde_tekst.set_opacity, .5))
        self.wait(.3)
        bredde_tekst, hoyde_tekst = MathTex(int(7)).move_to(
            DOWN*3.5+RIGHT*3), MathTex(int(12)).move_to(RIGHT*.5)
        self.play(Write(bredde_tekst), Write(hoyde_tekst))

        senter = rektangel.get_center() + DOWN * hoyde/2 + RIGHT * bredde/2
        arc1 = Arc(start_angle=PI, angle=-PI/2,
                   radius=bredde, arc_center=senter)
        self.play(Write(arc1), run_time=3)

        dot = Dot(point=senter + UP * bredde).set_color(RED)
        self.play(Write(dot))
        self.play(FadeOut(arc1))

        bredde, hoyde = 7*skalering, 5*skalering
        rektangel = Rectangle(height=hoyde, width=bredde).move_to(
            rektangel.get_center() + UP * bredde/2)
        self.bring_to_back(rektangel) 
        self.play(Write(rektangel))
        self.play(FadeOut(dot))

        self.play(ApplyMethod(bredde_tekst.shift, UP*3.7),
                  Transform(hoyde_tekst, MathTex("5").move_to(hoyde_tekst.get_center() + UP*1.5 + RIGHT*.3) ))
        self.wait(.3)


        senter = rektangel.get_center() + DOWN * hoyde/2 + LEFT * bredde/2
        arc1 = Arc(start_angle=PI/2, angle=-PI/2,
                   radius=hoyde, arc_center=senter)
        self.play(Write(arc1), run_time=3)

        dot = Dot(point=senter + RIGHT * hoyde).set_color(RED)
        self.play(Write(dot))
        self.play(FadeOut(arc1))

        bredde, hoyde = 2*skalering, 5*skalering

        rektangel = Rectangle(height=hoyde, width=bredde).move_to(
            rektangel.get_center() + RIGHT * hoyde/2)
        self.bring_to_back(rektangel)
        self.play(Write(rektangel))
        self.play(FadeOut(dot))
        self.play(ApplyMethod(hoyde_tekst.shift, RIGHT*2.7),
                  Transform(bredde_tekst, MathTex("2").move_to(bredde_tekst.get_center() + RIGHT*1.2) ))
        self.wait(.3)

        senter = rektangel.get_center() + DOWN * hoyde/2 + RIGHT * bredde/2
        arc1 = Arc(start_angle=PI, angle=-PI/2,
                   radius=bredde, arc_center=senter)
        self.play(Write(arc1), run_time=3)

        dot = Dot(point=senter + UP * bredde).set_color(RED)
        self.play(Write(dot))
        self.play(FadeOut(arc1))

        linje = Line(senter + UP * bredde, senter + UP * bredde + LEFT * 1)
        self.play(Write(linje))
        self.play(FadeOut(dot))
        arc1 = Arc(start_angle=PI, angle=-PI/2,
                   radius=bredde, arc_center=senter+UP*1)
        self.play(Write(arc1), run_time=3)
        dot = Dot(point=senter + UP * (bredde+1)).set_color(RED)
        self.play(Write(dot))
        self.play(FadeOut(arc1))

        bredde, hoyde = 2*skalering, 1*skalering

        rektangel = Rectangle(height=hoyde, width=bredde).move_to(
            rektangel.get_center() + UP * bredde/2 + UP*0.5)
        self.bring_to_back(rektangel)
        self.play(Write(rektangel))
        self.play(FadeOut(dot))
        self.play(ApplyMethod(bredde_tekst.shift, UP*2),
                  Transform(hoyde_tekst, MathTex("1").move_to(hoyde_tekst.get_center() + UP*1.2) ))

        self.wait(.3)
        arc1 = Arc(start_angle=PI/2, angle=-PI/2,
                   radius=hoyde, arc_center= rektangel.get_center() + DOWN * hoyde/2 + LEFT * bredde/2 )
        self.play(Write(arc1), run_time=3)
        dot = Dot(point=rektangel.get_center() + DOWN * hoyde/2 + LEFT * bredde/2 + RIGHT * hoyde).set_color(RED)
        self.play(Write(dot))
        self.play(FadeOut(arc1))

        linje = Line(rektangel.get_center() + DOWN * 0.25, rektangel.get_center() + UP * 0.25 )
        self.play(Write(linje))
        self.play(FadeOut(dot))
        self.play(FadeOut(bredde_tekst))

        self.wait(3)
