from __future__ import annotations

from typing import Any, Callable, Sequence

import manim
import numpy as np
import numpy.typing as npt

__all__ = [
    "ArbitraryCurve",
    "Square",
    "Polygon",
    "RegularPolygon",
    "Triangle",
    "Circle",
    "Dot",
    "Line",
]


class ArbitraryCurve:
    """
    Constructs an arbitrary curve.

    Args:
        curve:
            A curve in the form of a Python function
        x_range:
            The `(x_min, x_max, x_step)` values of the x-axis
        y_range:
            The `(y_min, y_max, y_step)` values of the y-axis
    """

    def __new__(
        cls,
        curve: Callable[[float], Any],
        *,
        x_range: Sequence[float] = (-5, 5, 1),
        y_range: Sequence[float] = (0, 5, 1),
        **kwargs: dict[str, Any],
    ) -> manim.ParametricFunction:
        axes = manim.Axes(x_range=x_range, y_range=y_range, **kwargs)
        plotted_curve = axes.plot(curve)

        def _new_repr(self):
            return f"ArbitraryCurve(curve={curve.__name__})"

        manim.ParametricFunction.__repr__ = _new_repr

        return plotted_curve


class Square(manim.Square):
    """
    Constructs a square geometry with the specified side length.

    An alias class for manim.Square.

    Args:
        side_length:
            square's side length
    """

    def __init__(self, side_length: float, **kwargs: dict[str, Any]) -> None:
        self.side_length = side_length
        manim.Square.__init__(self, self.side_length, **kwargs)

    def __repr__(self) -> str:
        return f"Square(side_length={self.side_length}) (alias for manim.Square)"


class Polygon(manim.Polygon):
    """
    Constructs a shape consisting of one close loop of vertices.

    An alias class for manim.Polygon.

    Args:
        *vertices:
            Polygon's vertices points
    """

    def __init__(
        self, *vertices: Sequence[Sequence[float]], **kwargs: dict[str, Any]
    ) -> None:
        self.vertices = vertices
        manim.Polygon.__init__(self, *vertices, **kwargs)

    def __repr__(self) -> str:
        return (
            f"Polygon(vertices={[v for v in self.vertices]}) (alias for manim.Polygon)"
        )


class RegularPolygon(manim.RegularPolygon):
    """
    Constructs a n-sided regular Polygon.

    An alias class for manim.RegularPolygon.

    Args:
        n:
            number of sides of the RegularPolygon
    """

    def __init__(self, n: int, **kwargs: dict[str, Any]) -> None:
        self.n = n
        manim.RegularPolygon.__init__(self, self.n, **kwargs)

    def __repr__(self) -> str:
        return f"RegularPolygon(n={self.n}) (alias for manim.RegularPolygon)"


class Triangle(manim.Triangle):
    """
    Constructs an equilateral Triangle geometry.

    An alias class for manim.Triangle.

    """

    def __init__(self, **kwargs: dict[str, Any]) -> None:
        manim.Triangle.__init__(self, **kwargs)

    def __repr__(self) -> str:
        return "Triangle() (alias for manim.Triangle)"


class Circle(manim.Circle):
    """
    Constructs a circular geometry with specified radius.

    An alias class for manim.Circle.

    Args:
        radius:
            the radius of the circle
    """

    def __init__(self, radius: float, **kwargs: dict[str, Any]) -> None:
        self.radius = radius
        manim.Circle.__init__(self, self.radius, **kwargs)

    def __repr__(self) -> str:
        return f"Circle(radius={self.radius}) (alias for manim.Circle)"


class Dot(manim.Dot):
    """
    Constructs a circle with a very small radius.

    An alias class for manim.Dot.

    """

    def __init__(
        self,
        point: list[float] | npt.NDArray[np.float64],
        radius: float,
        **kwargs: dict[str, Any],
    ) -> None:
        self.radius = radius
        self.point = point
        manim.Dot.__init__(self, point=self.point, radius=self.radius, **kwargs)

    def __repr__(self) -> str:
        return f"Dot(point={self.point}, radius={self.radius}) (alias for manim.Dot)"


class Line(manim.Line):
    """
    Constructs a Line geometry with the specified staring and end points.

    An alias class for manim.Line.

    Args:
        start:
            Line's starting points
        end:
            Line's end points
    """

    def __init__(
        self,
        start: Sequence[float] | npt.NDArray[np.float64],
        end: Sequence[float] | npt.NDArray[np.float64],
        **kwargs: dict[str, Any],
    ):
        self.start = start
        self.end = end
        manim.Line.__init__(self, start=self.start, end=self.end, **kwargs)

    def __repr__(self) -> str:
        return f"Line(start={self.start}, end={self.end}) (alias for manim.Line)"
