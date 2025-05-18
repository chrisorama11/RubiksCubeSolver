class Cube:

    def __init__(self, cubeState):
        if len(cubeState) != 54:
            raise ValueError("Cube state must be a 54-element list.")
        self.Cube = cubeState
        # Faces: U=0, F=1, R=2, B=3, L=4, D=5

    def horizontal_turn(self, direction, row):
        """
        Simulates a horizontal turn (row across front/right/back/left).
        direction: 0 = right, 1 = left
        row: 0 = top, 1 = middle, 2 = bottom
        """
        row_offsets = [0, 3, 6]
        i = row_offsets[row]

        # Face ranges: F=9, R=18, B=27, L=36
        F = self.Cube[9 + i : 9 + i + 3]
        R = self.Cube[18 + i : 18 + i + 3]
        B = self.Cube[27 + i : 27 + i + 3]
        L = self.Cube[36 + i : 36 + i + 3]

        if direction == 0:  # right
            self.Cube[18 + i : 18 + i + 3] = F
            self.Cube[27 + i : 27 + i + 3] = R
            self.Cube[36 + i : 36 + i + 3] = B
            self.Cube[9  + i : 9  + i + 3] = L
        elif direction == 1:  # left
            self.Cube[36 + i : 36 + i + 3] = F
            self.Cube[27 + i : 27 + i + 3] = L
            self.Cube[18 + i : 18 + i + 3] = B
            self.Cube[9  + i : 9  + i + 3] = R
        else:
            raise ValueError("Direction must be 0 (right) or 1 (left)")

        if row == 0:
            self._rotate_face(0, direction)          # Up face
        elif row == 2:
            self._rotate_face(5, 1 - direction)      # Down face

    def vertical_turn(self, direction, col):
        """
        Simulates a vertical turn (column across U/F/D/B).
        direction: 0 = down, 1 = up
        col: 0 = left, 1 = middle, 2 = right
        """
        if col not in [0, 1, 2]:
            raise ValueError("Column must be 0, 1, or 2")

        def col_indices(base, c):
            return [base[c], base[3 + c], base[6 + c]]

        U = [0,1,2,3,4,5,6,7,8]
        F = [9,10,11,12,13,14,15,16,17]
        D = [45,46,47,48,49,50,51,52,53]
        B = [27,28,29,30,31,32,33,34,35]

        U_col = col_indices(U, col)
        F_col = col_indices(F, col)
        D_col = col_indices(D, col)
        B_col = col_indices(B, 2 - col)  # mirrored

        u_vals = [self.Cube[i] for i in U_col]
        f_vals = [self.Cube[i] for i in F_col]
        d_vals = [self.Cube[i] for i in D_col]
        b_vals = [self.Cube[i] for i in B_col]

        if direction == 0:  # down
            for i in range(3):
                self.Cube[F_col[i]] = u_vals[i]
                self.Cube[D_col[i]] = f_vals[i]
                self.Cube[B_col[2 - i]] = d_vals[i]
                self.Cube[U_col[i]] = b_vals[2 - i]
        elif direction == 1:  # up
            for i in range(3):
                self.Cube[B_col[2 - i]] = u_vals[i]
                self.Cube[D_col[i]] = b_vals[i]
                self.Cube[F_col[i]] = d_vals[i]
                self.Cube[U_col[i]] = f_vals[i]
        else:
            raise ValueError("Direction must be 0 (down) or 1 (up)")

        if col == 0:
            self._rotate_face(4, 1 - direction)  # Left face
        elif col == 2:
            self._rotate_face(2, direction)      # Right face

    def _rotate_face(self, face_index, direction):
        """
        Rotates one of the six faces by 90 degrees.
        direction: 0 = clockwise, 1 = counter-clockwise
        """
        start = face_index * 9
        face = self.Cube[start:start + 9]

        if direction == 0:
            rotated = [face[i] for i in [6,3,0,7,4,1,8,5,2]]
        else:
            rotated = [face[i] for i in [2,5,8,1,4,7,0,3,6]]

        self.Cube[start:start + 9] = rotated
