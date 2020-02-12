#overriding
class Employee:
    
    def add(self,salary,incentive):
        print('Total salary in base class=', salary + incentive)

class Department(Employee):
    temp = 'I am employee of department class'
    def add(self,salary,incentive):
        print(self.temp)
        print('Total salary in department classs=',salary + incentive)
        super(Department,self).add(salary,  incentive)

Dept = Department()
Dept.add(45000, 5000)
