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
    assert line.start == [2]
    assert line.end == [4]


def test_regularpolygon():
    regularpolygon = rp.geometry.RegularPolygon(n=6)
    assert (
        regularpolygon.__repr__()
        == f"RegularPolygon(n={regularpolygon.n}) (alias for manim.RegularPolygon)"
    )
    assert isinstance(
        regularpolygon, (rp.geometry.RegularPolygon, manim.RegularPolygon)
    )
    assert regularpolygon.n == 6


def test_polygon():
    polygon = rp.geometry.Polygon([2, 4, 8], [1, 0, 0], [4, 4, 8])
    assert (
        polygon.__repr__()
        == f"Polygon(vertices={[v for v in polygon.vertices]}) (alias for manim.Polygon)"
    )
    assert isinstance(polygon, (rp.geometry.Polygon, manim.Polygon))
    assert polygon.vertices == ([2, 4, 8], [1, 0, 0], [4, 4, 8])


def test_dot():
    dot = rp.geometry.Dot([0, 0, 0], 0.88)
    assert (
        dot.__repr__()
        == f"Dot(point={dot.point}, radius={dot.radius}) (alias for manim.Dot)"
    )
    assert isinstance(dot, (rp.geometry.Dot, manim.Dot))
    assert dot.point == [0, 0, 0]
    assert dot.radius == 0.88
