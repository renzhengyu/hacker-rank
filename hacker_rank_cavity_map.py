def is_cavity(grid, r, c):
    if int(grid[r-1][c])>=int(grid[r][c]):
        return False
    if int(grid[r][c-1])>=int(grid[r][c]):
        return False
    if int(grid[r][c+1])>=int(grid[r][c]):
        return False
    if int(grid[r+1][c])>=int(grid[r][c]):
        return False
    return True

def cavityMap(grid):
    if len(grid)<=2:
        return grid
    else:
        result=[]
        result.append(grid[0])
        for r in range(1,len(grid)-1):
            s=grid[r][0]
            for c in range(1,len(grid)-1):
                s+="X" if is_cavity(grid, r, c) else grid[r][c]
            s+=grid[r][-1]
            result.append(s)
        result.append(grid[-1])   
    return result