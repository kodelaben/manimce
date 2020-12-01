from manim import *


class Boblesort(Scene):
    def construct(self):
        tall = [4, 1, 9, 11, 6, 3, 10, 2]
        antall = len(tall)

        tallobj = []
        for i in range(antall):
            tallobj.append(
                MathTex(tall[i]).move_to((antall/2-.5)*LEFT + 1*RIGHT*i)
            )

        bokser = []
        for i in range(antall):
            bokser.append(
                Square(side_length=1).move_to(tallobj[i].get_center())
            )

        gruppe = []
        for i in range(antall):
            gruppe.append(
                VGroup(tallobj[i], bokser[i])
            )

        self.add(
            *[gruppe[i] for i in range(antall)]
        )
        self.wait()

        for k in range(antall-1, 0, -1):
            if k == antall - 1:
                tempo = 1
            else:
                tempo = 1/2
            for i in range(k):
                self.play(*[ApplyMethod(gruppe[j].shift, UP*1.5)
                            for j in range(i, i+2)], run_time=tempo)
                self.wait(0.3)
                if tall[i] > tall[i+1]:
                    self.play(Indicate(gruppe[i][0]))
                    dummy = tall[i]
                    tall[i] = tall[i+1]
                    tall[i+1] = dummy
                    self.play(ApplyMethod(gruppe[i].shift, UP), run_time=tempo/3)
                    self.play(ApplyMethod(gruppe[i].shift, RIGHT),
                              ApplyMethod(gruppe[i+1].shift, LEFT), run_time=tempo/3)
                    self.play(ApplyMethod(gruppe[i].shift, DOWN), run_time=tempo/3)
                    self.play(*[ApplyMethod(gruppe[j].shift, DOWN*1.5)
                                for j in range(i, i+2)], run_time=tempo)
                    dummy = gruppe[i+1]
                    gruppe[i+1] = gruppe[i]
                    gruppe[i] = dummy
                else:
                    self.play(Indicate(gruppe[i+1][0]))
                    self.play(*[ApplyMethod(gruppe[j].shift, DOWN*1.5)
                                for j in range(i, i+2)], run_time=tempo)
            self.bring_to_front(gruppe[k])
            self.play(ApplyMethod(gruppe[k][1].set_color, GREEN), run_time=tempo)
        self.play(ApplyMethod(gruppe[0][1].set_color, GREEN), run_time=tempo)
        self.wait(2)