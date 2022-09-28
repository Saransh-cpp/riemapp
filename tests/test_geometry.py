from __future__ import annotations

import riemapp as rp
import manim


def test_triangle():
    triangle = rp.geometry.Triangle()
    assert triangle.__repr__() == "Triangle()"
    assert isinstance(triangle, (rp.geometry.Triangle, manim.Triangle))
