from Logic import PointRepository
from Logic import MyPoint
test = PointRepository([])

"""
20 data examples for the functions
"""
def dataExamples():
    points = PointRepository([])
    # 1
    points.AddPoint(1,1,"yellow")
    print(points) # [MyPoint(1,1,"yellow")]
    # 2
    points.DeleteByIndex(0)
    print(points) # []

    points.AddPoint(1,2,"green")
    points.AddPoint(2,3, "blue")
    # 3
    points.DeleteByIndex(0)
    print(points) # [MyPoint(2,3,"blue")]
    # 4
    points.DelPointsInSquare(0,5,5)
    print(points) # []
    # 5
    points.AddPoint(1,1,"magenta")
    print(points) # [MyPoint(1,1,"magenta")]
    # 6
    points.Update(0,5,5,"blue")
    print(points) # [MyPoint(5,5,"blue")]
    # 7
    points.DelInCircle(0,0,10)
    print(points) # []
    # 8
    points.AddPoint(1,1,"green")
    print(points) # [MyPoint(1,1,"green")]
    # 9
    points.AddPoint(2,2,"yellow")
    print(points) # [MyPoint(1,1,"green"), MyPoint(2,2,"yellow")]
    # 10
    points.ShiftOnX(2)
    print(points) # [MyPoint(3,1,"green"), MyPoint(4,2,"yellow")]

    points = PointRepository([MyPoint(0,0,"green"),MyPoint(2,2,"magenta"),MyPoint(3,5,"blue")])

    # 11
    points.ShiftOnX(10)
    print(points) # [MyPoint(10,0,"green"),MyPoint(12,2,"magenta"),MyPoint(13,5,"blue")]

    # 12
    points.ShiftOnX(-20)
    print(points) # [MyPoint(-10,0,"green"),MyPoint(-8,2,"magenta"),MyPoint(-7,5,"blue")]

    # 13
    points.Update(0,0,0,"magenta")
    print(points) # [MyPoint(0,0,"magenta"),MyPoint(-8,2,"magenta"),MyPoint(-7,5,"blue")]

    # 14
    points.Update(1,1,1,"green")
    print(points) # [MyPoint(0,0,"magenta"),MyPoint(1,1,"green"),MyPoint(-7,5,"blue")]

    # 15
    points.Update(2,2,2,"yellow")
    print(points) # [MyPoint(0,0,"magenta"),MyPoint(1,1,"green"),MyPoint(2,2,"yellow")]

    # 16
    print(points.PointsOfColor("magenta")) # [MyPoint(0,0,"magenta")]

    # 17
    print(points.PointsOfColor("green"))  # [MyPoint(1,1,"green")]

    # 18
    print(points.PointsOfColor("yellow"))  # [MyPoint(2,2,"yellow")]

    # 19
    print(points.PointsOfColor("blue"))  # []

    # 20
    points.DeleteByIndex(2)
    print(points) # [MyPoint(0,0,"magenta"),MyPoint(1,1,"green")]


"""
test functions for each function in logic
"""

def test_add_point():
    assert test.AddPoint(1, 2, "green") == [[1, 2, "green"]]
    assert test.AddPoint(3, 4, "blue") == [[1, 2, "green"], [3, 4, "blue"]]
    assert test.AddPoint(6, 8, "yellow") == [[1, 2, "green"], [3, 4, "blue"], [6, 8, "yellow"]]
    assert test.AddPoint(9, 12, "magenta") == [[1, 2, "green"], [3, 4, "blue"], [6, 8, "yellow"], [9, 12, "magenta"]]


def test_get_points():
    assert test.GetPoints() == []

    test.AddPoint(1, 2, "red")
    assert test.GetPoints() == [(1, 2, "red")]

    test.AddPoint(5, 7, "magenta")
    assert test.GetPoints() == [(1, 2, "red"), (5, 7, "magenta")]


def test_get_point_at_index():
    test.AddPoint(1, 2, "red")
    assert test.GetPointAtIndex(0) == (1, 2, "red")

    test.AddPoint(5, 7, "magenta")
    assert test.GetPointAtIndex(1) == (5, 7, "magenta")

    test.AddPoint(2, 3, "blue")
    assert test.GetPointAtIndex(2) == [2, 3, "blue"]


def test_points_of_colour():
    test.AddPoint(1, 2, "red")
    test.AddPoint(3, 4, "red")
    test.AddPoint(9, 11, "blue")

    assert test.PointsOfColor("red") == [(1, 2, "red"), (3, 4, "red")]
    assert test.PointsOfColor("blue") == [(9, 11, "blue")]
    assert test.PointsOfColor("yellow") == []


def test_points_in_square():
    test.AddPoint(1, 2, "blue")
    test.AddPoint(3, 4, "green")
    test.AddPoint(4, 5, "magenta")

    assert test.PointsInSquare(-3, 6, 10) == [[1, 2, "blue"], [3, 4, "green"], [4, 5, "magenta"]]
    assert test.PointsInSquare(-6, 8, 8) == [[1, 2, "blue"]]
    assert test.PointsInSquare(-100, 100, 200) == [[1, 2, "blue"], [3, 4, "green"], [4, 5, "magenta"]]


def test_min_dist():
    test.AddPoint(-2, 7, "green")
    test.AddPoint(0, 0, "magenta")
    assert test.MinDist() == 7.280

    test.AddPoint(-1, 5, "red")
    assert test.MinDist() == 2.236

    test.AddPoint(0, 1, "blue")
    assert test.MinDist() == 1


def test_update_point():
    test.AddPoint(-2, 7, "green")
    test.AddPoint(0, 0, "magenta")
    test.AddPoint(-1, 5, "red")
    assert test.Update(0, 5, 5, "magenta") == [(5, 5, "magenta"), (0, 0, "magenta"), (-1, 5, "red")]
    assert test.Update(1, 2, 2, "blue") == [(-2, 7, "green"), (2, 2, "blue"), (-1, 5, "red")]
    assert test.Update(2, 3, 3, "green") == [(-2, 7, "green"), (0, 0, "magenta"), (3, 3, "green")]


def test_delete_by_index():
    test.AddPoint(-2, 7, "green")
    test.AddPoint(0, 0, "magenta")
    test.AddPoint(-1, 5, "red")
    assert test.DeleteByIndex(0) == [(0, 0, "magenta"), (-1, 5, "red")]
    assert test.DeleteByIndex(1) == [(-2, 7, "green"), (-1, 5, "red")]
    assert test.DeleteByIndex(2) == [(-2, 7, "green"), (0, 0, "magenta")]


def test_del_points_in_square():
    test.AddPoint(1, 2, "blue")
    test.AddPoint(3, 4, "green")
    test.AddPoint(4, 5, "magenta")

    assert test.DelPointsInSquare(-3, 6, 10) == []
    assert test.DelPointsInSquare(-6, 8, 8) == [(3, 4, "green"), (4, 5, "magenta")]
    assert test.DelPointsInSquare(-100, 100, 200) == []


def test_max_dist():
    test.AddPoint(-2, 7, "blue")
    test.AddPoint(0, 0, "red")
    assert test.MaxDist() == 7.280

    test.AddPoint(-1, 5, "red")
    assert test.MaxDist() == 7.280

    test.AddPoint(6, 6, "blue")
    assert test.MaxDist() == 8.485


def test_shift_on_x():
    test.AddPoint(-2, 7, "blue")
    test.AddPoint(0, 0, "red")
    test.AddPoint(4, 5, "magenta")

    assert test.ShiftOnX(2) == [(0, 7, "blue"), (2, 0, "red"), (6, 5, "magenta")]
    assert test.ShiftOnX(0) == [(-2, 7, "blue"), (0, 0, "red"), (4, 5, "magenta")]
    assert test.ShiftOnX(-2) == [(-4, 7, "blue"), (-2, 0, "red"), (2, 5, "magenta")]


def test_del_in_circle():
    test.AddPoint(-2, 7, "blue")
    test.AddPoint(0, 0, "red")
    test.AddPoint(4, 5, "magenta")

    assert test.DelInCircle(0, 0, 1) == [(-2, 7, "blue"), (4, 5, "magenta")]
    assert test.DelInCircle(0, 0, 5) == [(-2, 7, "blue")]
    assert test.DelInCircle(0, 0, 10) == []
