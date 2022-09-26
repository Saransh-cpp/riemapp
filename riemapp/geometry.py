# TODO: probably create Line, Dot, Triangle, Circle
# TODO: docs + tests
from __future__ import annotations

import manim

__all__ = ["Square", "Rectangle", "Polygon", "RegularPolygon", "Triangle", "Dot"]


class Square(manim.Square):
    def __init__(self, side_length: float, **kwargs) -> None:
        self.side_length = side_length
        manim.Square.__init__(self, self.side_length, **kwargs)

    def __repr__(self):
        return f"Square(side_length={self.side_length})"


class Rectangle(manim.Rectangle):
    def __init__(self, height: float, width: float, **kwargs) -> None:
        self.height = height
        self.width = width
        manim.Rectangle.__init__(self, height=self.height, width=self.width, **kwargs)

    def __repr__(self):
        return f"Rectangle(height={self.height}, width={self.width})"


class Polygon(manim.Polygon):
    def __init__(self, *vertices, **kwargs) -> None:
        self.vertices = vertices
        manim.Polygon.__init__(self, *vertices, **kwargs)

    def __repr__(self):
        return f"Polygon(vertices={[v for v in self.vertices]})"


class RegularPolygon(manim.RegularPolygon):
    def __init__(self, n: int, **kwargs) -> None:
        self.n = n
        manim.RegularPolygon.__init__(self, self.n, **kwargs)

    def __repr__(self):
        return f"RegularPolygon(n={self.n})"


class Triangle(manim.Triangle):
    def __init__(self, **kwargs) -> None:
        manim.Triangle.__init__(self, **kwargs)

    def __repr__(self) -> str:
        return "Triangle()"


class Dot(manim.Dot):
    def __init__(self, radius: float, **kwargs) -> None:
        self.radius = radius
        manim.Dot.__init__(self, radius=self.radius, **kwargs)

    def __repr__(self):
        return f"Dot(radius={self.radius})"
