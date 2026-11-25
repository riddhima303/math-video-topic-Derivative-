from scenes.common import *
class Scene1Intro(LectureScene):
    def construct(self):
        self.start_voice(1)
        self.header('01 · Introduction','How fast is “right now”?')
        # A car moving on a road makes the speed-vs-time idea concrete.
        road = Line(LEFT*6.2+DOWN*1.65, RIGHT*6.2+DOWN*1.65, color='#58647B', stroke_width=5)
        dashes = VGroup(*[Line(LEFT*5.8+RIGHT*i*1.7+DOWN*1.65, LEFT*5.25+RIGHT*i*1.7+DOWN*1.65, color=INK, stroke_width=3) for i in range(8)])
        car = RoundedRectangle(width=1.55,height=.58,corner_radius=.12,fill_color=CYAN,fill_opacity=1,stroke_color=CYAN).move_to(LEFT*4.8+DOWN*1.15)
        roof = Polygon(car.get_center()+LEFT*.34+UP*.3,car.get_center()+LEFT*.05+UP*.64,car.get_center()+RIGHT*.43+UP*.3,fill_color='#B6F3F7',fill_opacity=1,stroke_width=0)
        wheels = VGroup(*[Circle(radius=.16,fill_color='#172033',fill_opacity=1,stroke_color=INK,stroke_width=1.5).move_to(car.get_center()+RIGHT*x+DOWN*.31) for x in [-.45,.45]])
        speed = Text('0', color=GOLD, font_size=38).move_to(RIGHT*3.5+UP*.35)
        speed_final = Text('72', color=GOLD, font_size=38).move_to(speed)
        label = Text('speedometer · km/h',font_size=22,color=MUTED).next_to(speed,DOWN,buff=.14)
        self.play(Create(road),FadeIn(dashes),FadeIn(car),FadeIn(roof),FadeIn(wheels),Write(speed),FadeIn(label),run_time=1.4)
        self.play(car.animate.shift(RIGHT*7.8),roof.animate.shift(RIGHT*7.8),wheels.animate.shift(RIGHT*7.8),Transform(speed, speed_final),run_time=4,rate_func=linear)
        question=Text('How quickly is the speed changing at this instant?',font_size=26,color=INK).to_edge(DOWN,buff=.45)
        self.play(Write(question),run_time=1.1); self.wait(1.8)
        self.play(FadeOut(VGroup(road,dashes,car,roof,wheels,speed,label,question)),run_time=.6)
        title=Text('DERIVATIVE',font_size=54,color=CYAN,weight=BOLD)
        subtitle=Text('A precise language for change',font_size=27,color=INK).next_to(title,DOWN,buff=.25)
        self.play(Write(title),FadeIn(subtitle,shift=UP*.2),run_time=1.2); self.wait(2)
        self.finish_voice(1)
