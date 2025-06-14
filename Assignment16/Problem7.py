def Marks():
    file = open("marks.txt", "w")
    for i in range(5):
        name = input(f"Enter name of student {i+1}: ")
        marks = input(f"Enter marks of {name}: ")
        file.write(f"{name},{marks}\n")
    file.close()

def Display():
    file = open("marks.txt", "r")
    for line in file:
        if line.strip() == "":
            continue
        name, marks = line.strip().split(",")
        if int(marks) > 75:
            print(f"{name} scored {marks}")
    file.close()

def main():
    Marks()
    Display()

if __name__ == "__main__":
    main()
