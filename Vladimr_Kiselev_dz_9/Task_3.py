# Task_3
class Worker:

    def __init__(self, worker_name, worker_surname, position, income):
        self.name = worker_name
        self.surname = worker_surname
        self.position = position
        self._wage = income['wage']
        self._bonus = income['bonus']

class Position(Worker):

    def get_full_name(self):
        full_name = f'{self.name} {self.surname} - {self.position}'
        return full_name

    def get_total_income(self):
        total_income = self._wage + self._bonus
        return total_income

employee = Position('Konstantin', 'Repin', 'welder', {'wage': 100.25 , 'bonus':200.45})
print(f'employee: {employee.get_full_name()}, income: {employee.get_total_income()}')