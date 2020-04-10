row = -1
col = -1
matrix = None
falling = False
colors = ["S", "T", "V", "W", "X", "Y", "Z"]

def initialize():
    global row, col, matrix
    row = int(input())
    col = int(input())
    matrix = {}
    zeros = [0 for j in range(col)]
    for i in range(row):
    	matrix[i] = zeros

def print_matrix():
    global row, col, falling, matrix
    # for i in range(row):
    #     print("|")
    #     for j in range(col):
    #         if matrix[i][j] != 0:
    #             print("   ")
    #         else:
    #             print("[" + matrix[i][j] + "]")
    #     print("|")
    #     print(col * "___")
    for r,c in matrix.items():
    	print("|", end = "")
    	for i in c:
    		if i == 0:
    			print("   ", end = "")
    		else:
    			print(" {} ".format(i), end = "")
    	print("|")
    print("", col*"___", "")
        

def get_command():
    global falling
    while (True):
        user_input = input()

        if user_input[0:1].upper() == "F":
            faller = (user_input.split(" "))
    
        elif not user_input:
            falling = True
            drop(faller)

        elif user_input.upper() == "Q":
            quit()

def drop(faller):  
    c = int(faller[1])
    empty = 0
    
    for i in range(row):
        if matrix[i][c-1] == "0":
            empty += 1

    if empty >= 0:
        for i in reversed(range(1,row)):
            if matrix[i][c-1] == "0" and matrix[i-1][c-1] != "0":
                matrix[i][c-1], matrix[i-1][c-1] = matrix[i-1][c-1], matrix[i][c-1]

    else:
        quit()

    pos = (row-empty)
    if pos < (len(faller[1])-2):
        matrix[0][c-1] = faller[1][len(faller[1])-pos-1]
        
    print_matrix()
    
# def rotate(faller):
#     c = int(faller[1][1])
    
