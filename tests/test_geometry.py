from __future__ import annotations

import manim

import riemapp as rp


def test_triangle():
    triangle = rp.geometry.Triangle()
    assert triangle.__repr__() == "Triangle() (alias for manim.Triangle)"
    assert isinstance(triangle, (rp.geometry.Triangle, manim.Triangle))


def test_square():
    square = rp.geometry.Square(side_length=2.0)
    assert (
        square.__repr__()
        == f"Square(side_length={square.side_length}) (alias for manim.Square)"
    )
    assert isinstance(square, (rp.geometry.Square, manim.Square))
    assert square.side_length == 2.0


def test_circle():
    circle = rp.geometry.Circle(radius=1.0)
    assert (
        circle.__repr__() == f"Circle(radius={circle.radius}) (alias for manim.Circle)"
    )
    assert isinstance(circle, (rp.geometry.Circle, manim.Circle))
    assert circle.radius == 1.0


def test_line():
    line = rp.geometry.Line(start=[2], end=[4])
    assert (
        line.__repr__()
        == f"Line(start={line.start}, end={line.end}) (alias for manim.Line)"
    )
    assert isinstance(line, (rp.geometry.Line, manim.Line))
    assert line.start == [2], line.end == [4]

def test_rectangle():
    rectangle = rp.geometry.Rectangle(height=4, width=6)
    assert (
        rectangle.__repr__() 
        == f"Rectangle(height={rectangle.height}, width={rectangle.width} (alias for manim.Rectangle))"
    )
    assert isinstance(rectangle, (rp.geometry.Rectangle, manim.Rectangle))
    assert rectangle.height == 4, rectangle.width == 6
