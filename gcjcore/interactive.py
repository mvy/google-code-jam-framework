# -*- coding: utf-8 -*-
from gcjcore.core import GenericProblem


class InteractiveProblem(GenericProblem):
    CORRECT = u'CORRECT'
    WRONG = u'WRONG_ANSWER'
    
    def write_case(self):
        pass
    
    def solve_all(self):
        self.case = 1
        self.read_number_of_cases()

        for i in range(self.number_of_cases):
            self.solve_one()