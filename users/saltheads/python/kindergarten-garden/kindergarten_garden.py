from typing import List, Dict


class Garden:
    def __init__(self, diagram: List[str], **kwargs: Dict[str, list]):
        self.garden0, self.garden1 = [list(line)
                                      for line in diagram.splitlines()]
        if 'students' in kwargs:
            self.names = sorted(kwargs['students'])
        else:
            self.names = ['Alice', 'Bob', 'Charlie', 'David',
                          'Eve',  'Fred',  'Ginny',  'Harriet',
                          'Ileana', 'Joseph', 'Kincaid', 'Larry']
        self.plant = {'R': 'Radishes',
                      'V': 'Violets',
                      'G': 'Grass',
                      'C': 'Clover', }

    def plants(self, students: str):
        idx = self.names.index(students)
        start, end = idx*2, (idx+1)*2
        return [self.plant[p] for p in self.garden0[start:end]] + \
               [self.plant[p] for p in self.garden1[start:end]]
