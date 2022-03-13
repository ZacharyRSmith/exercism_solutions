import re
import operator

OPERATION=re.compile(r"^What is (.+)\?$") 

def answer(question):
    """
    Returns answer to simple math questions returning the answer as an integer
    """        
    math_problem = extract_operation(question)
    op = Operation()    
    if len(math_problem):
        for elem in math_problem:
            op.parse(elem) 
        if op.is_final_state():
            return op.compute()
        else:
            raise ValueError("syntax error")
    else:
        raise ValueError("unknown operation")

class Operation:
    """
    Parses the mathematical problem word by word

    args: numeric operands
    op: function to execute
    compute_flag: is set to True once the operation is computable
    handler: a class that will parse a token at a time
    
    """
    def __init__(self):
        self.args = []
        self.op = None
        self.compute_flag = False
        self.handler = FirstOperandParser()

    def is_final_state(self):
        """
        Returns true if the math operation has ended in a supported state
        e.g. What is 1 plus would fail this test
        """
        if self.op:
            return False
        return True
    
    def compute(self):
        """
        Returns computes the result
        Result is always kept in the first argument in args (i.e. args[0])
        """
        try:
            if self.compute_flag:
                self.args = [self.op(*self.args)] 
                self.op = None
                self.compute_flag = False
            return self.args[0]            
        except:
            raise ValueError("Error computing")
        
    def parse(self,str):
        """
        Parse a token
        """
        self.handler.parse(str,self)
        self.compute()
        self.handler = self.handler.next_status
        
        
    

def extract_operation(question):
    """
    Extracts the mathematical formula from question
    """
    if question.startswith("Who is"):
        raise ValueError("unknown operation")
    result = OPERATION.match(question)
    if result:
        return result.group(1).split()
    raise ValueError("syntax error")

    
def is_number(str)-> bool:
    """
    helper function to check if a string is a number. 
    """
    try:
        return bool(float(str))        
    except ValueError:
        return False
                

class NumberParser:
    """
    Parses numbers
    """   
    def parse(self,str, op: Operation):            
        if is_number(str):
            op.args.append(eval(str))
            self.next_status = OperatorParser()              
        else:
            raise ValueError("syntax error")

class FirstOperandParser(NumberParser): 
    """
    Parses numbers: First Operand
    """
    pass

class SecondOperandParser(NumberParser): 
    """
    Parses numbers: Second Operand. After the 2nd operand has been parsed the number can be computed
    """
    def parse(self,str, op: Operation):       
        super().parse(str,op)
        op.compute_flag = True
                      

class ByParser: 
    """
    Parsers the By keyword after multiplied/divided
    """
    def parse(self,str, op: Operation):
        self.next_status = SecondOperandParser()
        if not str == "by":
            raise ValueError("by expected")

            
class OperatorParser:
    """
    Parses operator
    """

    supported = {'plus': [operator.add, SecondOperandParser],
                 'minus': [operator.sub, SecondOperandParser],
                 'multiplied': [operator.mul, ByParser],
                 'divided': [operator.truediv, ByParser]}
    unsupported = ['cubed']

    def parse(self,str, op: Operation):        
        if str in OperatorParser.supported:
            self.next_status = OperatorParser.supported[str][1]()
            op.op = OperatorParser.supported[str][0] 
        elif str in OperatorParser.unsupported:
            raise  ValueError("unknown operation")
        else:
            raise ValueError("syntax error")
        

        





        
    