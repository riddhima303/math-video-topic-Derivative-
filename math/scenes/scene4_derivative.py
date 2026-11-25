from scenes.common import *
class Scene4Derivative(LectureScene):
    def construct(self):
        self.start_voice(4)
        self.header('04 · Instantaneous change','The derivative: a limit')
        lim=Text("f′(x) = lim (h → 0) [f(x+h) - f(x)] / h",font_size=29,color=INK).move_to(UP*1.25)
        self.play(Write(lim),run_time=2)
        pieces=[(r'h', 'a small change in the input x'),(r'x+h','the nearby input after that small change'),(r'f(x+h)-f(x)','the resulting change in output'),('output change / h','output change divided by input change'),('limit as h → 0','let the input step shrink toward zero')]
        glossary=VGroup(lim)
        y=.25
        for sym,meaning in pieces:
            left=Text(sym,font_size=23,color=GOLD).move_to(LEFT*4.3+DOWN*y)
            right=Text(meaning,font_size=18,color=MUTED).move_to(LEFT*.75+DOWN*y)
            glossary.add(left,right)
            self.play(FadeIn(left,shift=RIGHT*.1),FadeIn(right,shift=LEFT*.1),run_time=.65); self.wait(6.5); y-=.66
        cap=Text("f'(x) is the instantaneous rate of change at x",font_size=26,color=CYAN,weight=BOLD).to_edge(DOWN,buff=.34)
        self.play(Write(cap),run_time=1); self.wait(1.3)
        self.play(FadeOut(glossary),FadeOut(cap),run_time=.7)
        graph=Axes(x_range=[0,3,1],y_range=[0,9,3],x_length=4.8,y_length=2.7,axis_config={'color':MUTED}).to_corner(UR,buff=.5).shift(DOWN*.35)
        curve=graph.plot(lambda x:x*x,x_range=[0,2.5],color=CYAN)
        x0=1.4; dot=Dot(graph.c2p(x0,x0*x0),color=GOLD)
        tangent=graph.plot(lambda x:2*x0*x-x0*x0,x_range=[.45,2.35],color=GREEN,stroke_width=4)
        note=Text("The tangent slope here is f′(x).",font_size=24,color=GREEN,weight=BOLD).move_to(LEFT*3.1+DOWN*.1)
        self.play(Create(graph),Create(curve),FadeIn(dot),Create(tangent),FadeIn(note),run_time=1.8); self.wait(2)
        self.finish_voice(4)
