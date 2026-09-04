class basket_ball:
    def __init__(self):
        self.stack=[]
    def x(self,value):
        self.stack.append(value)
        print(" Score added successfully ")
    def add(self):
        n=len(self.stack)
        if(n>=2):
            new_score=self.stack[-1]+self.stack[-2]
            self.stack.append(new_score)
            print(" Recorded a new score sum of prev 2")
        else:
            print("there are less then 2 scores ")
    def D(self):
        if not self.stack:
            print(" there are no scores ")
        else:
            new_score=self.stack[-1]*2
            self.stack.append(new_score)
            print(" new score added double of prev 2  ")
    def C(self):
        if not self.stack:
            print(" there are no scores  ")
        else:
            remove=self.stack.pop()
            print(f" removed score = {remove}" )

basket=basket_ball()
while(True):
    print("choice Menu : ")
    print(" X - Add a new score ")
    print(" +  Record a new score that is the sum of the previous two scores. ")
    print(" D  Record a new score that is the double of the previous score. ")
    print(" C  Invalidate the previous score, removing it from the record. ")
    print(" E exit ")
    user_input=input("Enter a choice : ")
    match user_input:
        case 'X':
            value=int(input("Enter a score : "))
            basket.x(value)
        case '+':
            basket.add()
        case 'D':
            basket.D()
        case 'C':
            basket.C()
        case 'E':
            print("Exiting program ")
            break
        case _:
            print("Invalid choice. Please try again.")