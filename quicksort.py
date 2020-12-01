from manim.manim import *

class Insertions(Scene):
    def construct(self):
        tall = [4, 1, 13, 9, 11, 6, 3, 10, 2, 5, 8, 16, 14, 0, 15, 7]
        antall = len(tall)
        skalering = 0.7
        buffer = .00

        tallobj = []

        for i in range(antall):
            tallobj.append(
                MathTex(tall[i]).move_to((antall/2-.5)*LEFT*skalering + RIGHT*i*(skalering+buffer)+UP)
            )

        bokser = []
        for i in range(antall):
            bokser.append(
                Square(side_length=1*skalering).move_to(tallobj[i].get_center())
            )

        gruppe = []
        for i in range(antall):
            gruppe.append(
                [ VGroup(tallobj[i], bokser[i]), tall[i] ]
            )


        self.add(
            *[gruppe[i][0] for i in range(antall)]
        )
        self.wait(.3)

        self.play(ApplyMethod(gruppe[-1][0].shift, DOWN*2.5))
        self.play(ApplyMethod(gruppe[-1][0].shift, LEFT *np.floor(antall/2)*skalering))

        self.wait(.3)
        self.play(ApplyMethod(gruppe[-1][0][1].set_color, GREEN))

        hoyre = []
        venstre = []
        pivot = -1

        for j in range(antall-1):
            self.play(ApplyMethod(gruppe[j][0].shift, DOWN*1.5))
            if gruppe[j][1] < gruppe[pivot][1]:
                skalar = 1
                venstre.insert(0,j) 
                forskyvning = len(venstre)
            else:
                skalar = -1
                hoyre.append(j) 
                forskyvning = len(hoyre)
            
            posisjon = gruppe[pivot][0][0].get_center() + UP +skalar*LEFT*forskyvning*skalering+skalar*LEFT*.15 
            
            
            self.play(ApplyMethod(gruppe[j][0].move_to, posisjon))
            self.play(ApplyMethod(gruppe[j][0].shift, DOWN))
        self.wait(0.3)

        self.play(*[ApplyMethod(gruppe[j][0].shift, UP*2.5) for j in range(antall)])
        self.wait(.3)
        
        
        # self.play(*[ApplyMethod(gruppe[j][0].shift, DOWN*1.5) for j in venstre])

        ## TODO: Sortere venstre side
        self.play(ApplyMethod(gruppe[venstre[-1]][0].shift, DOWN*2.5))
        self.play(ApplyMethod(gruppe[venstre[-1]][0].shift, LEFT *np.floor(len(venstre)/2)*skalering))
        self.play(ApplyMethod(gruppe[venstre[-1]][0].set_color, GREEN))

        pivot = venstre[-1]
        venstre1 = []
        hoyre2 = []
        for j in venstre[0:-1]:
            self.play(ApplyMethod(gruppe[j][0].shift, DOWN*1.5))
            if gruppe[j][1] < gruppe[pivot][1]:
                skalar = 1
                venstre1.insert(0,j) 
                forskyvning = len(venstre1)
            else:
                skalar = -1
                hoyre2.append(j) 
                forskyvning = len(hoyre2)
            
            posisjon = gruppe[pivot][0][0].get_center() + UP +skalar*LEFT*forskyvning*skalering+skalar*LEFT*.15 
            
            
            self.play(ApplyMethod(gruppe[j][0].move_to, posisjon))
            self.play(ApplyMethod(gruppe[j][0].shift, DOWN))
        self.wait(0.3)
        self.play(*[ApplyMethod(gruppe[j][0].shift, UP*2.5) for j in venstre])

        self.wait(3)

        