from ast import match_case
from tokenize import group


map = [[" . ", " . ", " . "], [" . ", " . ", " . "], [" . ", " . ", " . "]]
symboles = (' X ', ' O ')
tour = 0
current_symbole_index = 1 if tour % 2 == 0 else 0
register_positions = {1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: "", 8: "", 9: ""}

def draw_grid():
    for line in range(3):
        for case in range(3):
            print(map[line][case], end='')
        print()

def set_position_and_next(position: int, symbole_index: int)-> int:
    if(position <= 3):
        map[0][position - 1] = symboles[symbole_index]
    else:
        match position:
            case 4:
                map[1][0] = symboles[symbole_index]
            case 5:
                map[1][1] = symboles[symbole_index]
            case 6:
                map[1][2] = symboles[symbole_index]
            case 7:
                map[2][0] = symboles[symbole_index]
            case 8:
                map[2][1] = symboles[symbole_index]
            case 9:
                map[2][2] = symboles[symbole_index]

    if(symbole_index == 0):
        return 1
    else:
        return 0

def check_line() -> bool:
    if(register_positions[1] and register_positions[2] and register_positions[3]):
        if(register_positions[1] == register_positions[2] and register_positions[2] == register_positions[3]):
            return True
    if(register_positions[4] and register_positions[5] and register_positions[6]):
        if(register_positions[4] == register_positions[5] and register_positions[5] == register_positions[6]):
            return True
    if(register_positions[7] and register_positions[8] and register_positions[9]):
        if(register_positions[7] == register_positions[8] and register_positions[8] == register_positions[9]):
            return True

    return False
    
def check_column()-> bool:
    if(register_positions[1] and register_positions[4] and register_positions[7]):
        if(register_positions[1] == register_positions[4] and register_positions[4] == register_positions[7]):
            return True
    if(register_positions[2] and register_positions[5] and register_positions[8]):
        if(register_positions[2] == register_positions[5] and register_positions[5] == register_positions[8]):
            return True
    if(register_positions[3] and register_positions[6] and register_positions[9]):
        if(register_positions[3] == register_positions[6] and register_positions[6] == register_positions[9]):
            return True

    return False

def check_diag()->bool:
    if(register_positions[1] and register_positions[5] and register_positions[9]):
        if(register_positions[1] == register_positions[5] and register_positions[5] == register_positions[9]):
            return True
    if(register_positions[3] and register_positions[5] and register_positions[7]):
        if(register_positions[3] == register_positions[5] and register_positions[5] == register_positions[7]):
            return True

    return False

def inc_tour()-> int:
    global tour
    tour += 1
    return tour

def change_symbole()-> int:
     global current_symbole_index
     current_symbole_index = 1 if tour % 2 == 0 else 0
     return current_symbole_index

draw_grid()
def main()-> None:
    while True:
        position = int(input('[1-9] > '))
        if(register_positions[position]):
            continue
        else:
            symbole_index = set_position_and_next(position, current_symbole_index)
            tour = inc_tour()
            current_symbole = change_symbole()
            register_positions[position] = symboles[current_symbole]
            print(f"Joueur: {symboles[current_symbole]} \n")
            draw_grid()
            if tour > 5:
                is_win_lines = check_line()
                is_win_by_col = check_column()
                is_win_by_diag = check_diag()

                if(is_win_by_col or is_win_by_diag or is_win_lines):
                    inc_tour()
                    current_symbole = change_symbole()
                    print(f"le Joueur {symboles[current_symbole]} a gagné !")
                    break

                
main()
