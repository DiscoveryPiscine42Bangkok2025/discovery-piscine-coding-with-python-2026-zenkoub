def check_error(board):
    count_error = 0
    count_K = 0
    for i in range(0,len(board),1):
        if abs(len(board[i])-len(board)) >= 1:
            count_error += 1
    for row in board:
        for col in row:
            if col == "K":
                count_K += 1
    if count_K != 1:
        count_error += 1

    return count_error

def crerate_board(board):
    board_spl = []
    rows = board.splitlines()
    for i in rows:
        i = i.strip()
        board_spl.append(list(i))
    return board_spl


def checkmate(board):
    board_spl = crerate_board(board)
    if check_error(board_spl) >= 1:
        print("error")
        quit()
    row_r = None
    col_r = None
    row_p = None
    col_p = None
    row_b = None
    col_b = None
    row_q = None
    col_q = None
    row_k = None
    col_k = None

    have_r = None
    have_p = None
    have_b = None
    have_q = None
    have_k = None

    sus = 0
    fail = 0

    for i in range(0,len(board_spl),1):
        for j in range(0,len(board_spl[i]),1):
            if board_spl[i][j] in ["R","P","B","Q","K"]:
                if board_spl[i][j] == "R":
                    have_r = 1
                    row_r = i
                    col_r = j
                elif  board_spl[i][j] == "P":
                    have_p = 1
                    row_p = i
                    col_p = j
                elif  board_spl[i][j] == "B":
                    have_b = 1
                    row_b = i
                    col_b = j
                elif  board_spl[i][j] == "Q":
                    have_q = 1
                    row_q = i
                    col_q = j
                elif  board_spl[i][j] == "K":
                    have_k = 1
                    row_k = i
                    col_k = j
    if have_p != None:
        if abs(col_p - col_k) == 1 and (row_p + 1 == row_k or row_p - 1 == row_k):
            sus += 1
        else:
            fail += 1
        # print("row p:",row_p)
        # print("col p:",col_p)
    if have_r != None:
        if row_r == row_k or col_r == col_k:
            sus += 1
        else:
            fail += 1
        # print("row r:",row_r)
        # print("col r:",col_r)
    if have_b != None:
        if abs(row_b - row_k) == abs(col_b - col_k):
            sus += 1
        else:
            fail += 1
        # print("row b:",row_b)
        # print("col b:",col_b)
    if have_q != None:
        if (row_q == row_k or col_q == col_k) or abs(row_q - row_k) == abs(col_q - col_k):
            sus += 1
        else:
            fail += 1
    #     print("row b:",row_b)
    #     print("col b:",col_b)
    if have_k != None and (have_b == have_q == have_p == have_r == None):
        sus += 1
    # print("row k:",row_k)
    # print("col k:",col_k)
    if sus >= 1:
        print("Success")
    elif fail >= 1:
        print("Fail")