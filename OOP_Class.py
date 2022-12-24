class Member:
    def __init__(self, firstname, age, job):
        self.name = firstname
        self.age = age
        self.job = job


member1 = Member('Ahmed', 23, 'Engineer')
member2 = Member('Abdullah', 26, 'Engineer')

print(member1.name, member1.age, member1.job)
print(member2.name, member2.age, member2.job)
