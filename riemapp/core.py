from __future__ import annotations

from typing import Callable

from manim import ApplyComplexFunction, Create, NumberPlane, Scene

from riemapp.geometry import (
    Circle,
    Dot,
    Line,
    Polygon,
    RegularPolygon,
    Square,
    Triangle,
)

__all__ = ["ComplexMap"]


class ComplexMap:
    """
    Construct and animate a complex mapping.

    Args:
        f:
            A geometry (or `MObject`) created using `riemapp.geometry` or `manim`.
        transformation:
            The complex transformation as a function reference.
    """

    def __init__(
        self,
        f: Square | Polygon | RegularPolygon | Triangle | Circle | Dot | Line,
        transformation: Callable[[float], float],
    ) -> None:
        self.f = f
        self.transformation = transformation

    def __repr__(self) -> str:
        return (
            f"ComplexMap(f={self.f!r}, transformation={self.transformation.__name__})"
        )

    def generate_animation(
        self, *, add_numberplane: bool = False, run_time: float = 1.0
    ) -> ComplexMap.Animate:
        """
        Generates a mathematical animation.

        Args:
            add_numberplane:
                Adds NumberPlane to the scene.
            run_time:
                Run time for creating the provided geometry.

        Returns:
            animate:
                A custom manim Scene object
        """
        self.animate = self.Animate(
            self.f,
            self.transformation,
            add_numberplane=add_numberplane,
            run_time=run_time,
        )

        return self.animate

    def render(self, preview: bool = False) -> None:
        """
        Renders the animation.

        Args:
            preview:
                Automatically opens the generated animation.
        """
        if not hasattr(self, "animate"):
            raise ValueError("generate an animation first")

        self.animate.render(preview=preview)

    class Animate(Scene):
        """
        A placeholder class for manim Scene.

        This class is used to construct and generate manim animations programatically.

        Args:
            f:
                A geometry (or `MObject`) created using `riemapp.geometry` or `manim`.
            transformation:
                The complex transformation as a function reference.
            add_numberplane:
                Adds NumberPlane to the scene.
            run_time:
                Run time for creating the provided geometry.

        """

        def __init__(
            self,
            f: Square | Polygon | RegularPolygon | Triangle | Circle | Dot | Line,
            transformation: Callable[[float], float],
            *,
            add_numberplane: bool = False,
            run_time: float = 1.0,
        ) -> None:
            self.add_numberplane = add_numberplane
            self.run_time = run_time
            self.f = f
            self.transformation = transformation
            super().__init__()

        def __repr__(self) -> str:
            return (
                f"Animate(f={self.f!r}, transformation={self.transformation.__name__})"
            )

        def construct(self) -> None:
            """
            The default manim constructer
            """
            self.add_numberplane and self.add(NumberPlane())
            self.play(Create(self.f, run_time=self.run_time))
            self.play(
                ApplyComplexFunction(self.transformation, self.f),
            )
