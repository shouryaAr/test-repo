numof_lines = input("")
numof_lines=numof_lines.split()
v = int(numof_lines[0])
h = int(numof_lines[1])
count=0
coordsv=[]
coordsh=[]
pointsv={}
pointsh={}
def take_vinput():
    for i in range(v):
        while True:
            x = input(f"Enter Vertical Coords {i+1} (format: X Y1 Y2): ")
            coords = x.split()

            if len(coords) != 3:
                print("Please enter exactly three values (X Y1 Y2).")
                continue

            try:
                x_val, y1_val, y2_val = map(int, coords)

                if all(0 <= c <= 100 for c in (x_val, y1_val, y2_val)):
                    coordsv.append((x_val, y1_val, y2_val))
                    print(f"Coordinates accepted: {x_val}, {y1_val}, {y2_val}")
                    break
                else:
                    print("All values must be between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter integers only.")
def take_hinput():
    for i in range(h):
        while True:
            x = input(f"Enter Horizontal Coords {i+1} (format: Y X1 X2): ")
            coords = x.split()

            if len(coords) != 3:
                print("Please enter exactly three values (Y X1 X2).")
                continue

            try:
                y_val, x1_val, x2_val = map(int, coords)

                if all(0 <= c <= 100 for c in (y_val, x1_val, x2_val)):
                    coordsh.append((y_val, x1_val, x2_val))
                    print(f"Coordinates accepted: Y={y_val}, X1={x1_val}, X2={x2_val}")
                    break
                else:
                    print("All values must be between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter integers only.")

take_vinput()

take_hinput()

for i, s in enumerate(coordsv):
    X = int(s[0])
    Y1 = int(s[1])
    Y2 = int(s[2])
    pointsv.update({f"A{i+1}": (X, Y1), f"B{i+1}": (X, Y2)})

for j, q in enumerate(coordsh):
    Y = int(q[0])
    X1 = int(q[1])
    X2 = int(q[2])
    pointsh.update({f"C{j+1}": (X1, Y), f"D{j+1}": (X2, Y)})
vcord = []
hcord = []
for i in range(1, len(pointsv)):
    x1 = pointsv[f"A{i}"][0]
    x2 = pointsv[f"B{i}"][0]
    y1 = pointsv[f"A{i}"][1]
    y2 = pointsv[f"B{i}"][1]
    vcord.append([x1, x2, y1, y2])

for i in range(1, len(pointsh)):
    x3 = pointsh[f"C{i}"][0]
    x4 = pointsh[f"D{i}"][0]
    y3 = pointsh[f"C{i}"][1]
    y4 = pointsh[f"D{i}"][1]
    hcord.append([x3, x4, y3, y4])

def find_intersection(x1, y1, y2, y3, x3, x4):
    # Check if the vertical line's X is within the horizontal line's X range
    if min(x3, x4) <= x1 <= max(x3, x4) and min(y1, y2) <= y3 <= max(y1, y2):
        # Intersection point
        return (x1, y3)
    else:
        return None
for i in vcord+hcord:
    a=0
    if a%2==0:
        q=i[0]
        w=i[1]
        r=i[2]
        t=i[3]
        a+=1
    else:
        a+=1
        continue
    if a%2 !=0:
        e=i[0]
        y=i[1]
        o=i[2]
        p=i[3]
        a+=1
    else:
        a+=1
        continue
print(find_intersection(q,r,t,o,e,y))
