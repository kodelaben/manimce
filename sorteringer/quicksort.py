from manim import *


class Insertions(Scene):
    def construct(self):
        def sortering(array):
            if len(array) <= 1:
                if len(array) == 1:
                    self.bring_to_front(gruppe[array[0]][0])
                    self.play(ApplyMethod(gruppe[array[0]][0][1].set_color, GREEN))
                return
            pivot = array[-1]
            self.play(ApplyMethod(gruppe[pivot][0].shift, DOWN * 2.5))
            getposi = gruppe[pivot][0].get_center()-DOWN*1.5
            self.play(ApplyMethod(gruppe[pivot][0].shift, -(getposi)))
            self.bring_to_front(gruppe[pivot][0])
            self.play(ApplyMethod(gruppe[pivot][0][1].set_color, GREEN))
            venstre = []
            hoyre = []
            for j in array[0:-1]:
                self.play(ApplyMethod(gruppe[j][0].shift, DOWN * 1.5))
                if gruppe[j][1] < gruppe[pivot][1]:
                    skalar = 1
                    venstre.insert(0, j)
                    forskyvning = len(venstre)
                else:
                    skalar = -1
                    hoyre.append(j)
                    forskyvning = len(hoyre)

                posisjon = (
                    gruppe[pivot][0][0].get_center()
                    + UP
                    + skalar * LEFT * forskyvning * skalering
                )

                self.play(ApplyMethod(gruppe[j][0].move_to, posisjon))
                self.play(ApplyMethod(gruppe[j][0].shift, DOWN))
            self.wait(0.3)
            lengdehoyre = len(hoyre)
            self.play(*[ApplyMethod(gruppe[j][0].shift, LEFT *skalering*lengdehoyre+(getposi)) for j in array])
            self.play(*[ApplyMethod(gruppe[j][0].shift, UP * 2.5) for j in array])
            self.wait(.3)
            sortering(venstre)
            sortering(hoyre)

        tall = [4, 1, 13, 9, 17, 11, 6, 3, 14, 2, 5, 8, 16, 12, 0, 15, 10, 7]
        antall = len(tall)
        skalering = 0.7
        buffer = 0.00

        tallobj = [*[MathTex(tall[i]).move_to(
                    (antall / 2 - 0.5) * LEFT * skalering
                    + RIGHT * i * (skalering + buffer)
                    + UP) for i in range(antall)]]

        bokser, gruppe = [], []
        for i in range(antall):
            bokser.append(
                Square(side_length=1 * skalering).move_to(tallobj[i].get_center()))
            gruppe.append([VGroup(tallobj[i], bokser[i]), tall[i]])

        self.add(*[gruppe[i][0] for i in range(antall)])
        self.wait(0.3)
        
        sortering(range(len(tall)))
        self.wait(3)
