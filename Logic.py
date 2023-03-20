import math
import matplotlib.pyplot as plt


class MyPoint:
    """
    the properties of each point are:
        coord_x given as a number
        coord_y given as a number
        color given as string(possible values 'red', 'green', 'blue', 'yellow' and 'magenta'
    """
    def __init__(self,x,y,color):
        self.__coord_x = x
        self.__coord_y = y
        if color != "red" and color != "green" and color != "blue" and color != "yellow" and color != "magenta":
            raise AttributeError("The color is not available")
        self.__color = color

    """
    get and set the coordinates and the color of a point
    """
    def get_x(self):
        return self.__coord_x

    def get_y(self):
        return self.__coord_y

    def get_color(self):
        return self.__color

    def set_x(self, value):
        self.__coord_x = value

    def set_y(self, value):
        self.__coord_y = value

    def set_color(self, color):
        if color != "red" and color != "green" and color != "blue" and color != "yellow" and color != "magenta":
            raise AttributeError("The color is not available")
        self.__color = color

    """
    the string representation of a point
    """
    def __repr__(self):
        return "Point(" + str(self.__coord_x) + "," + str(self.__coord_y) + ") of color " + self.__color + "."


class PointRepository:
    """
    data is the list of points
    """
    def __init__(self,data):
        self.__data = data[:]

# 1.Add a point to the repository
    def AddPoint(self,x,y,color):
        p = MyPoint(x,y,color)
        self.__data.append(p)
        return self.__data[:]

# 2.Get all points
    def GetPoints(self):
        return self.__data[:]

# 3.Get a point at a given index
    def GetPointAtIndex(self,index):
        if index >= 0 and index < len(self.__data):
            return self.__data[index]
        else:
            raise IndexError("The index should be between 0 and the length of the list")

# 4.Get all points of a given color
    def PointsOfColor(self,color):
        if color != "red" and color != "green" and color != "blue" and color != "yellow" and color != "magenta":
            raise AttributeError("The color is not available")
        else:
            points = []
            for i in range(0,len(self.__data)):
                if self.__data[i].get_color() == color:
                    points.append(self.__data[i])
            return points[:]

# 5.Get all points that are inside a given square (up-left corner and length given)
    def PointsInSquare(self,corner1_x,corner1_y,length):
        points = []
        for i in range(0, len(self.__data)):
            if(corner1_x <= self.__data[i].get_x() <= corner1_x + length and corner1_y - length <= self.__data[i].get_y() <= corner1_y):
                points.append(self.__data[i])
        if len(points) > 0:
            return points[:]
        else:
            raise ValueError("There are no points inside the square")

# 6.Get the minimum distance between two points
    def MinDist(self):
        if len(self.__data) > 1:
            distances = []
            for i in range(len(self.__data)):
                for j in range(i+1,len(self.__data)):
                    distances.append(math.sqrt((self.__data[i].get_x()-self.__data[j].get_x())**2+(self.__data[i].get_y()-self.__data[j].get_y())**2))
            return min(distances)
        else:
            raise IndexError("There should be at least 2 points in the list")

# 7.Update a point at a given index
    def Update(self,index,new_x,new_y,new_color):
        self.__data[index].set_x(new_x)
        self.__data[index].set_y(new_y)
        self.__data[index].set_color(new_color)
        return self.__data[index]

# 8.Delete a point by index
    def DeleteByIndex(self,index):
        self.__data.pop(index)
        return self.__data[:]

# 9.Delete all points that are inside a given square
    def DelPointsInSquare(self,corner_x,corner_y,length):
        for i in range(len(self.__data)-1, -1,-1):
            if(corner_x <= self.__data[i].get_x() <= corner_x + length and corner_y - length <= self.__data[i].get_y() <= corner_y):
                del self.__data[i]
        return self.__data[:]

# 10.Plot all points in a chart (using library matplotlib)
    def PlotPoints(self):
        x_list = []
        y_list = []
        c_list = []
        for i in range(len(self.__data)):
            x_list.append(self.__data[i].get_x())
            y_list.append(self.__data[i].get_y())
            c_list.append(self.__data[i].get_color())
        plt.title("Points")
        plt.scatter(x_list,y_list,s = 100, c = c_list)
        plt.show()

# 13.Get the maximum distance between two points
    def MaxDist(self):
        if len(self.__data) > 1:
            distances = []
            for i in range(len(self.__data)):
                for j in range(i+1,len(self.__data)):
                    distances.append(math.sqrt((self.__data[i].get_x()-self.__data[j].get_x())**2 + (self.__data[i].get_y()-self.__data[j].get_y())**2))
            return max(distances)
        else:
            raise IndexError("There should be at least 2 points in the list")

# 16.Shift all points on  the x-axis
    def ShiftOnX(self,value):
        for i in range(0,len(self.__data)):
            value += self.__data[i].get_x()
            self.__data[i].set_x(value)
        return self.__data[:]

# 19.Delete all points that are inside a given circle
    def DelInCircle(self,center_x,center_y,radius):
        for i in range(len(self.__data)-1, -1, -1):
            if self.__data[i].get_x() <= center_x + radius and self.__data[i].get_x() >= center_x - radius and self.__data[i].get_y() <= center_y + radius and self.__data[i].get_y() >= center_y-radius:
                del self.__data[i]
        return self.__data[:]

        




