from scenes.common import *
class Scene5Example(LectureScene):
    def construct(self):
        self.start_voice(5)
        self.header('05 · Worked example','Find the rate for f(x) = x²')
        avg=['Average rate from 2 to 4','= [f(4) - f(2)] / (4 - 2)','= (4² - 2²) / 2','= (16 - 4) / 2','= 12 / 2 = 6']
        group=VGroup(*[Text(s,font_size=29,color=INK) for s in avg]).arrange(DOWN,aligned_edge=LEFT,buff=.16).to_edge(LEFT,buff=.65).shift(DOWN*.2)
        for line in group:
            self.play(Write(line),run_time=.9); self.wait(.35)
        avlabel=Text('average slope = 6',font_size=23,color=PINK).next_to(group,DOWN,buff=.18,aligned_edge=LEFT)
        self.play(FadeIn(avlabel)); self.wait(16)
        self.play(FadeOut(VGroup(group,avlabel)),run_time=.5)
        deriv=["f′(x) = lim (h → 0) [f(x+h) - f(x)] / h","= lim (h → 0) [(x+h)² - x²] / h","= lim (h → 0) [x² + 2xh + h² - x²] / h","= lim (h → 0) [2xh + h²] / h","= lim (h → 0) (2x + h)","= 2x"]
        lines=VGroup(*[Text(s,font_size=23,color=INK) for s in deriv]).arrange(DOWN,aligned_edge=LEFT,buff=.12).to_edge(LEFT,buff=.55).shift(DOWN*.05)
        for line in lines:
            self.play(Write(line),run_time=.8); self.wait(5.2)
        final=Text("f′(x) = 2x",font_size=34,color=CYAN).next_to(lines,DOWN,buff=.2,aligned_edge=LEFT)
        self.play(Write(final)); self.wait(1)
        self.play(FadeOut(VGroup(lines,final)),run_time=.5)
        at2=Text("f′(2) = 2(2) = 4",font_size=37,color=GOLD).move_to(UP*1.15)
        meaning=Text('At x = 2, the curve is rising 4 output units per input unit.',font_size=22,color=INK).next_to(at2,DOWN,buff=.2)
        self.play(Write(at2),FadeIn(meaning),run_time=1.3)
        ax=Axes(x_range=[0,4,1],y_range=[0,17,4],x_length=6.4,y_length=3.35,axis_config={'color':MUTED}).shift(DOWN*1.35+LEFT*.1)
        curve=ax.plot(lambda x:x*x,x_range=[0,4],color=CYAN,stroke_width=4)
        dot=Dot(ax.c2p(2,4),color=GOLD,radius=.09)
        tangent=ax.plot(lambda x:4*x-4,x_range=[.6,3.4],color=GREEN,stroke_width=4)
        tl=Text('y = 4x - 4',font_size=24,color=GREEN).next_to(ax.c2p(3.25,9),UP,buff=.1)
        self.play(Create(ax),Create(curve),Create(tangent),FadeIn(dot),Write(tl),run_time=2); self.wait(2)
        self.finish_voice(5)
