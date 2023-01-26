class Employee:
    count = 0
    salary = 0

    def __init__(self, name, family, salary, depart):
        self.name = name
        self.family = family
        self.salary = salary
        self.department = depart
        Employee.salary += salary
        Employee.count += 1

    def avg_salary(self):
        avg_sala = Employee.salary/Employee.count
        return avg_sala

    def total_empls(self):
        return Employee.count


class FullTime(Employee):
    def __init__(self, name, family, salary, depart):
        Employee.__init__(self, name, family, salary, depart)


emp1 = Employee("swamy", "yalamanchily", 8000, "IT")
emp2 = Employee("srikanth", "Gadipudi", 6000, "Tax")
emp3 = Employee("Abdhul", "rahaman", 4000, "Income")
emp4 = FullTime("Sai", "Maccena", 2000, "Revenue")

print("Average salary of employees is " + str(emp2.avg_salary()))
print("No.of Employees are " + str(FullTime.count))


