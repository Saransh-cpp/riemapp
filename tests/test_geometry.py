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


def test_line():
    line = rp.geometry.Line(start=[2], end=[4])
    assert (
        line.__repr__()
        == f"Line(start={line.start}, end={line.end}) (alias for manim.Line)"
    )
    assert isinstance(line, (rp.geometry.Line, manim.Line))
    assert line.start == [2], line.end == [4]
