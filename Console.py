from Logic import PointRepository
from Logic import MyPoint


def printmenu():
    # Displays the menu
    msg = "Menu:\n"
    msg += "\t 1 Add point\n"
    msg += "\t 2 Get all points\n"
    msg += "\t 3 Get point at index\n"
    msg += "\t 4 Get points of same color\n"
    msg += "\t 5 Get points in square\n"
    msg += "\t 6 Get minimum distance between 2 points\n"
    msg += "\t 7 Update point at index\n"
    msg += "\t 8 Delete point at index\n"
    msg += "\t 9 Delete points in square\n"
    msg += "\t 10 Plot points in chart\n"
    msg += "\t 11 Get the maximum distance between 2 points\n"
    msg += "\t 12 Shift Points on the X axis\n"
    msg += "\t 13 Delete points in circle\n"
    msg += "\t 0 Exit\n"
    print(msg)


def main():
    # Starts the app
    # We initialised the list of points with: MyPoint(1,2,"red"),MyPoint(6,7,"magenta"),MyPoint(2,3,"green")
    test_points = [MyPoint(1,2,"red"),MyPoint(6,7,"magenta"),MyPoint(2,3,"green")]
    my_points = PointRepository(test_points)

    stop = False
    while stop == False:
        printmenu()
        option = int(input("Enter option:"))
        """
        We choose an option until our option is 'Exit'
        """
        if option == 0:
            print("Goodbye!")
            stop = True
        elif option == 1:
            print("Give the coordinates of the points")
            x = int(input("x="))
            y = int(input("y="))
            print("The available colors are: red, green, blue, yellow and magenta.")
            c = str(input("color="))
            if c != "red" and c != "green" and c != "blue" and c != "yellow" and c != "magenta":
                print("The color isn't available")
            else:
                print("The new list of points is: ",my_points.AddPoint(x,y,c))
        elif option == 2:
            if len(my_points.GetPoints()) == 0:
                print("There are no points")
            else:
                print("The list of the points is: ",my_points.GetPoints())
        elif option == 3:
            print("Give an index:")
            i = int(input("i="))
            if i < 0 and i > len(my_points.GetPoints())-1:
                print("The index is invalid")
            else:
                print("The point at index ",i, " is ",my_points.GetPointAtIndex(i))
        elif option == 4:
            if len(my_points.GetPoints()) == 0:
                print("There are no points")
            else:
                print("Give a color from the list: red, green, blue, yellow and magenta")
                c = str(input("c="))
                if c != "red" and c != "green" and c != "blue" and c != "yellow" and c != "magenta":
                    print("The color isn't available")
                else:
                    if len(my_points.PointsOfColor(c)) > 0:
                        print("The points of color ", c, "are: ", my_points.PointsOfColor(c))
                    else:
                        print("There are no points of color",c)
        elif option == 5:
            if len(my_points.GetPoints()) == 0:
                print("There are no points")
            else:
                print("Give the coordinates of the corner and the length")
                x = int(input("x="))
                y = int(input("y="))
                l = int(input("l="))
                if l <= 0:
                    print("the length must be positive")
                else:
                    if len(my_points.PointsInSquare(x,y,l)) > 0:
                        print("The points in the square are: ", my_points.PointsInSquare(x,y,l))
                    else:
                        print("There are no points inside the square")
        elif option == 6:
            if len(my_points.GetPoints()) < 2:
                print("There should be at least 2 points")
            else:
                print("The minimum distance is: ", my_points.MinDist())
        elif option == 7:
            if len(my_points.GetPoints()) == 0:
                print("There are no points")
            else:
                print("Select the index and the new coordinates and color")
                i = int(input("i="))
                x = int(input("x="))
                y = int(input("y="))
                c = str(input("c="))
                if i < 0 or i > len(my_points.GetPoints())-1:
                    print("The index is invalid")
                elif c != "red" and c != "green" and c != "blue" and c != "yellow" and c != "magenta":
                    print("The color isn't available")
                else:
                    print("The new point is: ",my_points.Update(i,x,y,c))
        elif option == 8:
            if len(my_points.GetPoints()) == 0:
                print("There are no points")
            else:
                print("Give an index")
                i = int(input("i="))
                if i < 0 or i > len(my_points.GetPoints())-1:
                    print("The index is invalid")
                else:
                    print("The new list of points is: ",my_points.DeleteByIndex(i))
        elif option == 9:
            if len(my_points.GetPoints()) == 0:
                print("There are no points")
            else:
                print("Give the coordinates of the corner and the length")
                x = int(input("x="))
                y = int(input("y="))
                l = int(input("l="))
                if l <= 0:
                    print("the length must be positive")
                else:
                    print("The remaining points are:",my_points.DelPointsInSquare(x,y,l))
        elif option == 10:
            if len(my_points.GetPoints()) == 0:
                print("There are no points")
            else:
                my_points.PlotPoints()
        elif option == 11:
            if len(my_points.GetPoints()) < 2:
                print("There should be at least 2 points")
            else:
                print("The maximum distance is: ", my_points.MaxDist())
        elif option == 12:
            if len(my_points.GetPoints()) == 0:
                print("There are no points")
            else:
                value = int(input("value="))
                print("The shifted points by ",value, "are: ", my_points.ShiftOnX(value))
        elif option == 13:
            if len(my_points.GetPoints()) == 0:
                print("There are no points")
            else:
                print("Give the coordinates and the radius of the circle:")
                x = int(input("x="))
                y = int(input("y="))
                r = int(input("r="))
                if r <= 0:
                    print("The radius must be positive")
                else:
                    print(my_points.DelInCircle(x,y,r))
        else:
            print("Invalid option")