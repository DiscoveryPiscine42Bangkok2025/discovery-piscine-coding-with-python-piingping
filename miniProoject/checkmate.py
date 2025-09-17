def checkmate(board: str):
    try:
        print(board)
        rows = board.splitlines()
        n = len(rows)
        if n == 0 or any(len(r) != n for r in rows):
            print("Error")
            return

        print(rows)

        # หา King
        kings = [(i, j) for i in range(n) for j in range(n) if rows[i][j] == 'K']
        if len(kings) != 1:
            print("Error")
            return
        kr, kc = kings[0]

        def in_bounds(r, c): return 0 <= r < n and 0 <= c < n

        # Pawn (โจมตีทแยงขึ้นซ้าย/ขวา)
        for dr, dc in [(-1, -1), (-1, 1)]:
            print(kr)
            print(kc)

            print(in_bounds(kr+dr, kc+dc))
            print(rows[kr+dr][kc+dc] == 'P')
            if in_bounds(kr+dr, kc+dc) and rows[kr+dr][kc+dc] == 'P':
                print("Success")
                return

        # Bishop, Rook, Queen
        directions = {
            'B': [(-1,-1),( -1,1),(1,-1),(1,1)],
            'R': [(-1,0),(1,0),(0,-1),(0,1)],
            'Q': [(-1,-1),(-1,1),(1,-1),(1,1),(-1,0),(1,0),(0,-1),(0,1)]
        }

        for r in range(n):
            for c in range(n):
                piece = rows[r][c]
                if piece in directions:
                    for dr, dc in directions[piece]:
                        rr, cc = r+dr, c+dc
                        while in_bounds(rr, cc):
                            if rows[rr][cc] != '.':
                                if (rr, cc) == (kr, kc):
                                    print("Success")
                                    return
                                break
                            rr += dr
                            cc += dc
        print("Fail")
    except Exception:
        print("Error")
