class Solution:
    def solve(self, board: List[List[str]]) -> None:
        queue = deque()
        visit = set()
        rows, cols = len(board), len(board[0])
        # left col
        for i in range(len(board)):
            if board[i][0] == "O" and (i, 0) not in visit:
                queue.append([i, 0])
                visit.add((i, 0))
        #top row
        for i in range(len(board[0])):
            if board[0][i] == "O" and (0, i) not in visit:
                queue.append([0, i])
                visit.add((0, i))
        #right col
        for i in range(len(board)):
            if board[i][len(board[0]) - 1] == "O" and (i, len(board[0]) - 1) not in visit:
                queue.append([i, len(board[0]) - 1])
                visit.add((i, len(board[0]) - 1))
        # bottom row
        for i in range(len(board[0])):
            if board[len(board) - 1][i] == "O" and (len(board) - 1, i) not in visit:
                queue.append([len(board) - 1, i])
                visit.add((len(board) - 1, i))
        if len(queue) == 0:
            for i in range(rows):
                for j in range(cols):
                    if board[i][j] == "O":
                        board[i][j] = "X"
            return
        neighbors = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        while queue:
            r, c = queue.popleft()
            for dr, dc in neighbors:
                rdr, cdc = r + dr, c + dc
                if (min(rdr, cdc) < 0 or rdr == rows or cdc == cols or board[rdr][cdc] == "X" or (rdr, cdc) in visit):
                    continue
                if board[rdr][cdc] == "O":
                    queue.append([rdr, cdc])
                    visit.add((rdr, cdc))
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O" and (i, j) not in visit:
                    board[i][j] = "X"