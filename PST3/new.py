class Students:
    total_monkeys = 0
    def __init__(self, name):
        self.name = name
        Students.total_monkeys += 1
    def show_total():
        print("Total monkeys created:", Students.total_monkeys)
s1 = Students("Cat")
s2 = Students("Naw")
Students.show_total()