


def isDm(arr,n):

    for i in range(0, n):
        sum = 0
        for j in range(0, n):
            sum = sum + abs(arr[i][j])
        sum = sum - abs(arr[i][i])
        if (abs(arr[i][i]) < sum):
            return False
    return True

def jacobi(arr,e):


    if(isDm(arr,3)):
        f1 = lambda x, y, z: (arr[0][3] - arr[0][1] * y - arr[0][2]) / arr[0][0]
        f2 = lambda x, y, z: (arr[1][3] - arr[1][0] * x - arr[1][2] * z) / arr[1][1]
        f3 = lambda x, y, z: (arr[2][3] - arr[2][0] * x - arr[2][1] * y) / arr[2][2]

        x0 = 0
        y0 = 0
        z0 = 0

        condition = True
        while condition:
            x1 = f1(x0, y0, z0)
            y1 = f2(x0, y0, z0)
            z1 = f3(x0, y0, z0)

            e1 = abs(x0 - x1);
            e2 = abs(y0 - y1);
            e3 = abs(z0 - z1);

            x0 = x1
            y0 = y1
            z0 = z1

            condition = e1 > e and e2 > e and e3 > e

        print('\nx=%0.3f, y=%0.3f and z = %0.3f\n' % (x1, y1, z1))
    else:
        print('Is not Diagonally Dominant Matrix ')


def gaussSeidel(arr,e):

    if (isDm(arr, 3)):
        f1 = lambda x, y, z: (arr[0][3] - arr[0][1] * y - arr[0][2]) / arr[0][0]
        f2 = lambda x, y, z: (arr[1][3] - arr[1][0] * x - arr[1][2] * z) / arr[1][1]
        f3 = lambda x, y, z: (arr[2][3] - arr[2][0] * x - arr[2][1] * y) / arr[2][2]

        x0 = 0
        y0 = 0
        z0 = 0

        condition = True
        while condition:
            x1 = f1(x0, y0, z0)
            y1 = f2(x1, y0, z0)
            z1 = f3(x1, y1, z0)

            e1 = abs(x0 - x1);
            e2 = abs(y0 - y1);
            e3 = abs(z0 - z1);

            x0 = x1
            y0 = y1
            z0 = z1

            condition = e1 > e and e2 > e and e3 > e

        print('\nx=%0.3f, y=%0.3f and z = %0.3f\n' % (x1, y1, z1))
    else:
        print('Is not Diagonally Dominant Matrix ')


if __name__ == '__main__':

    e = 0.001
    arr1=[[4,2,0,2],[2,10,4,6],[0,4,5,5]]

    #4x+2y=2
    #2x+10y+4z=6
    #4y+5z=5

    jacobi(arr1,e)
    gaussSeidel(arr1,e)


