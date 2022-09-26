from __future__ import annotations

from manim import ApplyComplexFunction, Create, NumberPlane, Scene

from riemapp.geometry import Polygon, Rectangle, RegularPolygon, Square,  Triangle

# from manim.utils.file_ops import open_file as open_media_file


class ComplexMap:
    def __init__(
        self, f: Square | Rectangle | Polygon | RegularPolygon | Triangle, transformation: callable
    ):
        self.f = f
        self.transformation = transformation

    def generate_animation(
        self, *, add_numberplane: bool = False, run_time: float = 1.0
    ):
        self.animate = self.Animate(
            self.f, self.transformation, add_numberplane, run_time
        )

    def render(self, open_file: bool = False):
        if not hasattr(self, "animate"):
            raise ValueError("generate an animation first")

        self.animate.render()

        # open_file and open_media_file(self.animate.renderer.file_writer.movie_file_path)

    class Animate(Scene):
        def __init__(
            self,
            f: Square | Rectangle | Polygon | RegularPolygon | Triangle,
            transformation: callable,
            add_numberplane: bool = False,
            run_time: float = 1.0,
        ):
            self.add_numberplane = add_numberplane
            self.run_time = run_time
            self.f = f
            self.transformation = transformation

        def construct(self):
            self.add_numberplane and self.add(NumberPlane)
            self.play(Create(self.f, run_time=self.run_time))
            self.play(
                ApplyComplexFunction(self.transformation, self.f),
            )


# def generate_animation(f, transformation, add_numberplane=False, open_file=False):
#     class Test(Scene):
#         def construct(self):
#             add_numberplane and self.play(Create(NumberPlane()))
#             self.play(Create(f))
#             self.play(
#                 ApplyComplexFunction(transformation, f),
#             )

#     test = Test()
#     test.render()

#     open_file and open_media_file(test.renderer.file_writer.movie_file_path)
