Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:37:02) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def check_winner(board):
    req=4
    result=[]
    diag1=[]
    diag2=[]
    col=[]
    x=len(board[0])
    y=len(board)
    for i in range(y):
        row=""        
        for j in range(x):
            row += str(board[i][j])[0]
            if i==0:
                col.append(str(board[i][j])[0])
                diag1.append(str(board[i][j])[0])
                diag2.append(str(board[i][j])[0])
            else:
                col[j] += str(board[i][j])[0]
                if j==x-1:
                    diag2.append(str(board[i][j])[0])
                    diag1[j] += str(board[i][j])[0]
                elif j==0:
                    diag1.insert(0,str(board[i][j])[0])
                    diag2[i+j] += str(board[i][j])[0]
                else:
                    diag1[j] += str(board[i][j])[0]
                    diag2[i+j] += str(board[i][j])[0]
        result.append(row)
    result.extend(col)
    result.extend(diag1)
    result.extend(diag2)
    for option in result:
        #print(option)
        if "X"*req in option:
            return "X"
        elif "O"*req in option:
            return "O"