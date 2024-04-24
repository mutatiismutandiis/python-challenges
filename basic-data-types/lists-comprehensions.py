# INPUT: three integers x, y and z representing the dimensions of a cuboid along with an integer n. 
# OUTPUT: list of all possible coordinates given by (i, j, k) on a 3D grid where the sum of x+y+z is not equal to n.

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    coordinates = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1)]
    valid_coordinates = [coord for coord in coordinates if sum(coord) != n]
    
    print(valid_coordinates)
