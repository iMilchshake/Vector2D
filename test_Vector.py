from Vector2D import Vector2D
import pytest

a = Vector2D(1, 2)
b = Vector2D(1, 2)
c = Vector2D(2, 4)


def test_str():
    assert str(a) == "[1, 2]"
    assert str(a) == str(b)
    assert str(a) != str(c)


def test_eq():
    assert True == (a == b)
    assert False == (a == c)


def test_add():
    assert (a + b) == c


def test_sub():
    assert (c - a) == b


def test_mul():
    assert a * 0 == Vector2D.zero()
    assert a * 1 == a
    assert a * 2 == Vector2D(2 * a.x, 2 * a.y)


def test_mag():
    assert a.magnitude() == pytest.approx(2.2360679775, 0.0000000001)
    assert c.magnitude() == pytest.approx(4.472135955, 0.0000000001)


def test_magSquared():
    assert a.magnitudeSquared() == 5
    assert c.magnitudeSquared() == 20


def test_zero():
    tmp = Vector2D(0, 0)
    assert tmp == Vector2D.zero()


def test_rnd():
    for i in range(100):
        tmp = Vector2D.rnd()
        assert 0 <= tmp.x <= 1 and 0 <= tmp.y <= 1


def test_unpacking():
    tmp = Vector2D(*a)
    assert 1, 2 == a
    assert a == tmp


def test_shifting():
    assert c == a.shifted(b)
