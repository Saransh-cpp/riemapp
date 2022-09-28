from __future__ import annotations

from typing import Any, Sequence

import manim
import numpy as np
import numpy.typing as npt

__all__ = [
    "Square",
    "Rectangle",
    "Polygon",
    "RegularPolygon",
    "Triangle",
    "Dot",
    "Line",
]


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


class Rectangle(manim.Rectangle):
    def __init__(self, height: float, width: float, **kwargs: dict[str, Any]) -> None:
        self.height = height
        self.width = width
        manim.Rectangle.__init__(self, height=self.height, width=self.width, **kwargs)

    def __repr__(self) -> str:
        return f"Rectangle(height={self.height}, width={self.width})"


class Polygon(manim.Polygon):
    def __init__(
        self, *vertices: Sequence[Sequence[float]], **kwargs: dict[str, Any]
    ) -> None:
        self.vertices = vertices
        manim.Polygon.__init__(self, *vertices, **kwargs)

    def __repr__(self) -> str:
        return f"Polygon(vertices={[v for v in self.vertices]})"


class RegularPolygon(manim.RegularPolygon):
    def __init__(self, n: int, **kwargs: dict[str, Any]) -> None:
        self.n = n
        manim.RegularPolygon.__init__(self, self.n, **kwargs)

    def __repr__(self) -> str:
        return f"RegularPolygon(n={self.n})"


class Triangle(manim.Triangle):
    def __init__(self, **kwargs: dict[str, Any]) -> None:
        manim.Triangle.__init__(self, **kwargs)

    def __repr__(self) -> str:
        return "Triangle()"


class Dot(manim.Dot):
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
        return f"Dot(point={self.point}, radius={self.radius})"


class Line(manim.Line):
    def __init__(self, start: list | np.array, end: list | np.array, **kwargs):
        self.start = start
        self.end = end
        manim.Line.__init__(self, start=self.start, end=self.end, **kwargs)

    def __repr__(self):
        return f"Line(start={self.start}, end={self.end})"
