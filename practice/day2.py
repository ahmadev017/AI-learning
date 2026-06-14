scores = [65,35,45,67,87,95,78,33]

passed = [s for s in scores if s >=60]

print(f'passed: {passed}')

grade = lambda s: "A" if s>=90 else "B" if s>=80 else "C" if s >=70 else "C" if s>=60 else "F"

results = {s:grade(s) for s in scores}

print(results)

def stats(scores):
    return {
        'Total': len(scores),
        'average':round(sum(scores)/len(scores),1),
        'heighest':max(scores),
        'passed' :[s for s in scores if s>=60]
    }

print(stats(scores))


class Developer:
    def __init__(self,name, skills):
        self.name = name
        self.skills = skills

    def addSkill(self, skill):
        self.skills.append(skill)
        print(f'I have learned this too : {skill}')

    def introduce(self, name):
        return f'My name is {name} and i have these skills: {','.join(self.skills)}'

me = Developer('Ahmad', ['Javascript', 'python', 'c++'])

me.addSkill('R')    

intro = me.introduce('Ahmad')
print(intro)

with open("skills.txt","w") as f:
  f.write(me.introduce('Ahmad'))

with open("skills.txt","r") as f:
   print(f.read())