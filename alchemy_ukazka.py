########
"""
jmeno, prijmeni, pobocka
Pepa, Novak, Praha
Jana, Novakova, Praha
Petr, Novak, Brno


"""
#######

class Employee:
    def __init__(self, jmeno, prijmeni, pobocka):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.pobocka = pobocka

    def __repr__(self):
        return f"{self.jmeno} {self.prijmeni} ({self.pobocka})"

petr_novak = Employee("Petr", "Novak", "Brno")
jana_novakova = Employee("Jana", "Novakova", "Praha")
pepa_novak = Employee("Pepa", "Novak", "Praha")

#####
select = "select * from employees where pobocka in ('Praha', 'Brno')"