from cube import Cube

def get_cube_input():
    print("This tool takes in a Rubik's cube state as a single 54-letter input (or 6 faces of 9 letters each).")
    print("Use W, R, G, Y, O, B to represent White, Red, Green, Yellow, Orange, Blue respectively.")
    print("Enter faces in this order: Up, Right, Front, Down, Left, Back (U, R, F, D, L, B).")

    try:
        up    = input("Enter UP face (top) [9 letters]: ").strip().upper()
        right = input("Enter RIGHT face [9 letters]: ").strip().upper()
        front = input("Enter FRONT face [9 letters]: ").strip().upper()
        down  = input("Enter DOWN face (bottom) [9 letters]: ").strip().upper()
        left  = input("Enter LEFT face [9 letters]: ").strip().upper()
        back  = input("Enter BACK face [9 letters]: ").strip().upper()

        faces = [up, right, front, down, left, back]

        if not all(len(face) == 9 for face in faces):
            raise ValueError("Each face must be exactly 9 characters.")

        cube = list("".join(faces))

        if len(cube) != 54:
            raise ValueError("Total cube input must be exactly 54 characters.")

        return cube

    except ValueError as e:
        print("Input error:", e)
        return None


def print_cube(cube):
    def face_str(face):
        return "\n".join([
            " ".join(face[i:i+3]) for i in range(0, 9, 3)
        ])

    labels = ["Up", "Right", "Front", "Down", "Left", "Back"]
    for i in range(6):
        face = cube[i*9:(i+1)*9]
        print(f"{labels[i]}:\n{face_str(face)}\n")



def apply_moves(cube_obj, move_str):
    move_map = {
        'U': lambda: cube_obj.horizontal_turn(0, 0),
        'U\'': lambda: cube_obj.horizontal_turn(1, 0),
        'U2': lambda: [cube_obj.horizontal_turn(0, 0) for _ in range(2)],
        'D': lambda: cube_obj.horizontal_turn(1, 2),
        'D\'': lambda: cube_obj.horizontal_turn(0, 2),
        'D2': lambda: [cube_obj.horizontal_turn(1, 2) for _ in range(2)],
        'F': lambda: cube_obj.horizontal_turn(0, 1),
        'F\'': lambda: cube_obj.horizontal_turn(1, 1),
        'F2': lambda: [cube_obj.horizontal_turn(0, 1) for _ in range(2)],
        'B': lambda: cube_obj.horizontal_turn(1, 1),
        'B\'': lambda: cube_obj.horizontal_turn(0, 1),
        'B2': lambda: [cube_obj.horizontal_turn(1, 1) for _ in range(2)],
        'R': lambda: cube_obj.vertical_turn(0, 2),
        'R\'': lambda: cube_obj.vertical_turn(1, 2),
        'R2': lambda: [cube_obj.vertical_turn(0, 2) for _ in range(2)],
        'L': lambda: cube_obj.vertical_turn(1, 0),
        'L\'': lambda: cube_obj.vertical_turn(0, 0),
        'L2': lambda: [cube_obj.vertical_turn(1, 0) for _ in range(2)],
    }

    for move in move_str.strip().split():
        if move not in move_map:
            raise ValueError(f"Invalid move: {move}")
        action = move_map[move]
        if isinstance(action(), list):
            continue

def main():
    cube_input = get_cube_input()
    if cube_input:
        cube = Cube(cube_input)
        print("Initial state:")
        print_cube(cube)

        scramble = input("Enter scramble moves (e.g., R U R' U'): ")
        apply_moves(cube, scramble)

        print("After scramble:")
        print_cube(cube)

if __name__ == "__main__":
    main()