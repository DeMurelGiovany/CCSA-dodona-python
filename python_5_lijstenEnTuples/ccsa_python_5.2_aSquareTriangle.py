import math
from typing import List


def triangle(r: int) -> List[List[int]]:
    assert isinstance(r, int) and r >= 0, "invalid number of rows"

    if r == 0:
        return []
    

    listOfRows = []
    row = []

    listOfRows.append([1])
    for i in range(1, r):
        row = [1]
        for j in range(1, i):
            row.append(listOfRows[i-1][j-1] + listOfRows[i-1][j])
        row.append(1)    
        listOfRows.append(row)

    return listOfRows
 
def hexagon(row: int, col: int) -> List[int]:
    assert isinstance(row, int), "invalid internal position"
    assert isinstance(col, int), "invalid internal position"
    
    pTriangle = triangle(row+2)
    
    row -=1
    col -=1
    assert row > col > 0, "invalid internal position"
    hex = []
    hex.append( pTriangle[row-1][col-1] )
    hex.append( pTriangle[row-1][col] ) 
    hex.append( pTriangle[row][col+1] ) 
    hex.append( pTriangle[row+1][col+1] ) 
    hex.append( pTriangle[row+1][col] )  
    hex.append( pTriangle[row][col-1] ) 
    return hex 

def square(row: int, col: int) -> str:
    output = ""
    factors = hexagon(row, col)
    product = math.prod(factors)
    root = math.sqrt(product)
    output = f'{" x ".join(str(f) for f in factors)} = {product} = {int(root)} x {int(root)}'
    return output