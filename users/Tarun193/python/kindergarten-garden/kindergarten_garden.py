class Garden:
    _SYMBOL_TO_PLANT = {'R':"Radishes",'G':'Grass',"V":'Violets','C':'Clover'}
    students=[
        "Alice","Bob","Charlie",
        "David","Eve","Fred","Ginny","Harriet",
        "Ileana","Joseph","Kincaid","Larry"
    ]
    def __init__(self, diagram, students = students):
        self.diagram = diagram.split('\n')
        self.students = sorted(students)

    def plants(self,student):
        index = self.students.index(student)
        result = []
        for row in self.diagram:
            result.append(Garden._SYMBOL_TO_PLANT[row[index*2:index*2+2][0]])
            result.append(Garden._SYMBOL_TO_PLANT[row[index*2:index*2+2][1]])
        return result
