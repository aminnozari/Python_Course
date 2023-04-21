Input = int(input("number of the students in the class"))
Scores = 0
Array = []
for i in range(Input):
    score = int(input("enter the score"))
    Array.append(score)
    Scores += score
print(max(Input))
print(min(Input))
print(float(Scores/Input))