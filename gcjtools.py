import sys


class GenericProblem():
    '''A generic problem class for Google Code Jam contest

    Use by derivating this class and implement `solve_one`:

        class my_class(GenericProblem):
            def solve_one(self):

    You can also add a main procedure using this:

        if __name__ == '__main__':
            problem = my_class()
            problem.solve_all()
    '''
    def __init__(self):
        self.case = 1
        pass

    def write_case(self, output):
        '''Writes : 'Case #<self.case>: ' '''
        print("Case #{0}: {1}".format(self.case, output))
        self.case += 1

    def read_number_of_cases(self):
        self.number_of_cases = int(sys.stdin.readline())

    def solve_all(self):
        self.case = 1
        self.read_number_of_cases()

        for i in range(self.number_of_cases):
            output = self.solve_one()
            self.write_case(output)

if __name__ == '__main__':
    write_case(1)
    write_case(2)
    write_case(3)
    write_case(4)

