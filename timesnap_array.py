def mtrx_snake(i, j, n):
    """
    Возвращает значение, расположенное в матрице размером n x n
    в строке i и в столбце j. Матрица заполнена порядковыми числами
    спиралью по часовой стрелке
    """
    k = min(i, j, n-i-1, n-j-1)
    if i == k:
        return 4 * (k * n - k**2) + j - k + 1
    elif j == n - k - 1:
        return 4 * (k * n - k**2) + n - 3 * k + i
    elif i == n - k - 1:
        return 4 * (k * n - k**2) + 3 * n - 5 * k - j - 2
    else:
        return 4 * (k * n - k**2) + 4 * n - 7 * k - i - 3
n = int(input())
mtrx = [[0 for j in range(n)] for i in range(n)]
print()
for i in range(n):
    for j in range(n):
        mtrx[i][j] = mtrx_snake(i, j, n)
        print(mtrx[i][j], end = '\t')
    print()