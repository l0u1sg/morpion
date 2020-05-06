

i = 0
player = 0

a = [' ', ' ', ' ']
b = [' ', ' ', ' ']
c = [' ', ' ', ' ']


def positionx():

    if "x?0" in x and "y?0" in y and a[0] == ' ':
        a[0] = 'X'
    elif "x?1" in x and "y?0" in y and a[1] == ' ':
        a[1] = 'X'
    elif "x?2" in x and "y?0" in y and a[2] == ' ':
        a[2] = 'X'
    elif "x?0" in x and "y?1" in y and b[0] == ' ':
        b[0] = 'X'
    elif "x?1" in x and "y?1" in y and b[1] == ' ':
        b[1] = 'X'
    elif "x?2" in x and "y?1" in y and b[2] == ' ':
        b[2] = 'X'
    elif "x?0" in x and "y?2" in y and c[0] == ' ':
        c[0] = 'X'
    elif "x?1" in x and "y?2" in y and c[1] == ' ':
        c[1] = 'X'
    elif "x?2" in x and "y?2" in y and c[2] == ' ':
        c[2] = 'X'


def positionO():

    if "x?0" in x and "y?0" in y and a[0] == ' ':

        a[0] = 'O'
    elif "x?1" in x and "y?0" in y and a[1] == ' ':

        a[1] = 'O'
    elif "x?2" in x and "y?0" in y and a[2] == ' ':

        a[2] = 'O'
    elif "x?0" in x and "y?1" in y and b[0] == ' ':

        b[0] = 'O'
    elif "x?1" in x and "y?1" in y and b[1] == ' ':

        b[1] = 'O'
    elif "x?2" in x and "y?1" in y and b[2] == ' ':

        b[2] = 'O'
    elif "x?0" in x and "y?2" in y and c[0] == ' ':

        c[0] = 'O'
    elif "x?1" in x and "y?2" in y and c[1] == ' ':

        c[1] = 'O'
    elif "x?2" in x and "y?2" in y and c[2] == ' ':

        c[2] = 'O'


while i < 3:
    if player == 0:
        x = input("Choose x Player 1")
        y = input("Choose y Player 1")
        positionx()
        player = 1
        print(a)
        print(b)
        print(c)

    elif player == 1:
        x = input("Choose x Player 2")
        y = input("Choose y Player 2")
        positionO()
        player = 0
        print(a)
        print(b)
        print(c)

    i = i + 1

print(a)
print(b)
print(c)
