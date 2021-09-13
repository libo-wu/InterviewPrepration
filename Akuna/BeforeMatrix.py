# Matrix Summation
# 两个Matrix，已知 After求 Before。他们之间的转换关系是
# After[0,0]=Before[0,0]
# After[0,1]=Before[0,0]+Before[0,1]
# After[1,0]=Before[0,0]+Before[1,0]
# After[1,1]=Before[0,0]+Before[1,0]+Before[0,1]
# Example: After = [[2, 5], [7, 17]]
#          before = [[2, 3], [5, 7]]


# solution: Before(i,j) = After(i,j)+After(i-1,j-1)-After(i-1,j)-After(i,j-1)

def BeforeMatrix(after):
    before = []
    row_num = len(after)
    col_num = len(after[0])
    before_ij = 0
    for i in range(row_num):
        before_row = []
        for j in range(col_num):
            if i==0 and j==0:
                before_ij = after[0][0]
            elif i == 0:
                before_ij = after[0][j] - after[0][j-1] 
            elif j==0:
                before_ij = after[i][0] - after[i-1][0]
            else:
                before_ij = after[i][j] + after[i-1][j-1] -after[i-1][j]-after[i][j-1]
            before_row.append(before_ij)
        before.append(before_row)
    return before

if __name__ == "__main__":
    after= [[2, 5,8], [7, 17, 23]]
    before = BeforeMatrix(after)
    print(before)
