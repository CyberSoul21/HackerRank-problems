
import copy
def row_maximisation(input_matrix):
    #write code
    n = len(input_matrix) #rows
    m = len(input_matrix) #columns
    aux_matrix = copy.deepcopy(input_matrix)
    lst_max = []
    # 1. Find the n maximun values. 
    max = 0
    pos = (0,0)
    
    for x in range(n):
        for i in range(n):
            for j in range(m):
                if aux_matrix[i][j] > max:
                    max = aux_matrix[i][j]
                    pos = (i,j)
                    aux_matrix[i][j] = 0
        lst_max.append((max,pos[0],pos[1])) # save value and its position.
        
        max = 0                    
    print(input_matrix)   
    # 2. Find how many changes are necesaries to maximize the first row 
    ch = len(lst_max) # count changes
    for x in lst_max:        
        if x[0] in input_matrix[0]:
            ch = ch - 1


    return ch

if __name__ == '__main__':
    #words = input().strip()
    matrix = [[38,40,9],[23,40,25],[45,34,33]]
    print(row_maximisation(matrix))    
