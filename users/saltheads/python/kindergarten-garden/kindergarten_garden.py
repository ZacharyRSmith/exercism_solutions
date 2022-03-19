from typing import List, Dict


class Garden:
    names: Dict[str, int] = {name: idx for idx, name in enumerate(
        ['Alice', 'Bob', 'Charlie', 'David',
         'Eve',  'Fred',  'Ginny',  'Harriet',
         'Ileana', 'Joseph', 'Kincaid', 'Larry', ])}

    symbol_to_plant: Dict[str, str] = {'R': 'Radishes',
                       'V': 'Violets',
                       'G': 'Grass',
                       'C': 'Clover', }

    def __init__(self, diagram: str, students: List[str] = None):
        self.garden0, self.garden1 = [list(line)
                                      for line in diagram.splitlines()]
        if students:
            self.names = {name: idx for idx, name in enumerate(
                sorted(students))}

    def plants(self, students: str):
        idx = self.names[students]
        start, end = idx * 2, (idx+1) * 2
        return [self.symbol_to_plant[s] for s in self.garden0[start:end]] + \
               [self.symbol_to_plant[s] for s in self.garden1[start:end]]
