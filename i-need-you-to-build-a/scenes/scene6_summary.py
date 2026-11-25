from scenes.common import *
class Scene6Summary(LectureScene):
    def construct(self):
        self.start_voice(6)
        self.header('06 · Summary','One idea, two time scales')
        rows=[('AVERAGE','across an interval','secant line','(f(b) - f(a)) / (b - a)',PINK),('INSTANTANEOUS','at one input','tangent line',"f′(x) = lim (h → 0) [f(x+h) - f(x)] / h",GREEN)]
        y=1.25
        for name,when,line,formula,color in rows:
            title=Text(name,font_size=17,color=color,weight=BOLD).move_to(LEFT*5.15+UP*y)
            descr=Text(when+'  ·  '+line,font_size=16,color=MUTED).move_to(LEFT*1.1+UP*y)
            form=Text(formula,font_size=16,color=INK).move_to(RIGHT*4.35+UP*y)
            self.play(FadeIn(title),FadeIn(descr),Write(form),run_time=1.25); y-=1.25
        summary=Text('Secant slopes approach a tangent slope as the interval shrinks.',font_size=23,color=CYAN).move_to(DOWN*1.35)
        self.play(Write(summary),run_time=1); self.wait(25)
        credits=VGroup(Text('Thanks for learning with us.',font_size=29,color=INK,weight=BOLD),Text('References: OpenStax Calculus Vol. 1, 3.1; Stewart Calculus, 8e, 2.1.',font_size=16,color=MUTED),Text('AI disclosure: AI-assisted lesson script and Manim scenes; voice uses Edge Neural en-US-JennyNeural.',font_size=15,color=MUTED)).arrange(DOWN,buff=.2).move_to(DOWN*2.2)
        self.play(FadeIn(credits,shift=UP*.15)); self.wait(2)
        self.finish_voice(6)
