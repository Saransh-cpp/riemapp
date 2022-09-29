from __future__ import annotations

import os

import numpy as np
import pytest

import riemapp as rp


def test_complex_map():

    f = rp.geometry.Square(2.0)

    def transform(z):
        return np.e**z

    cm = rp.ComplexMap(f, transform)
    assert isinstance(cm, rp.ComplexMap)
    assert cm.f == f
    assert cm.transformation == transform

    with pytest.raises(ValueError):
        cm.render()

    animation = cm.generate_animation()
    assert isinstance(cm.animate, cm.Animate)
    assert animation == cm.animate

    cm.render()
    assert os.path.exists("./media/videos/1080p60/Animate.mp4")
