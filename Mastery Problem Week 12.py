# Mastery Problem Week 12
class School:
    def __init__(self, SchoolName, Mascot, TotalStudents, YearBuilt, PrincipalName):
        self.SchoolName = SchoolName
        self.Mascot = Mascot
        self.TotalStudents = TotalStudents
        self.YearBuilt = YearBuilt
        self.PrincipalName = PrincipalName
    def GetPrincipal(self):
        return f"The principal for {self.SchoolName} High School is {self.PrincipalName}."
    def GetMascot(self):
        return f"The mascot for {self.SchoolName} High School is the {self.Mascot}"
class StudentDemographic:
    def __init__(self, Name, Age, Address, GradeLevel, PhoneNumber):
        self.Name = Name
        self.Age = Age
        self.Address = Address
        self.GradeLevel = GradeLevel
        self.PhoneNumber = PhoneNumber
    def GetName(self):
        return f"The name of the student is {self.Name}."
    def GetGrade(self):
        return f"{self.Name}'s grade level is {self.GradeLevel}."
    def GetAge(self):
        return f"{self.Name} is {self.Age} years old."
class StudentGrades:
    def __init__(self, FirstPeriodGrade, SecondPeriodGrade, ThirdPeriodGrade, FourthPeriodGrade, FifthPeriodGrade, SixthPeriodGrade, SeventhPeriodGrade):
        self.FirstPeriodGrade = FirstPeriodGrade
        self.SecondPeriodGrade = SecondPeriodGrade
        self.ThirdPeriodGrade = ThirdPeriodGrade
        self.FourthPeriodGrade = FourthPeriodGrade
        self.FifthPeriodGrade = FifthPeriodGrade
        self.SixthPeriodGrade = SixthPeriodGrade
        self.SeventhPeriodGrade = SeventhPeriodGrade
    def GetGPA(self):
        if "A" in self.FirstPeriodGrade: 
            GPA1 = 4
        elif "B" in self.FirstPeriodGrade: 
            GPA1 = 3
        elif "C" in self.FirstPeriodGrade: 
            GPA1 = 2
        elif "D" in self.FirstPeriodGrade:
            GPA1 = 1
        elif "F" in self.FirstPeriodGrade: 
            GPA1 = 0

        if "A" in self.SecondPeriodGrade: 
            GPA2 = 4
        elif "B" in self.SecondPeriodGrade: 
            GPA2 = 3
        elif "C" in self.SecondPeriodGrade: 
            GPA2 = 2
        elif "D" in self.SecondPeriodGrade:
            GPA2 = 1
        elif "F" in self.SecondPeriodGrade: 
            GPA2 = 0

        if "A" in self.ThirdPeriodGrade: 
            GPA3 = 4
        elif "B" in self.ThirdPeriodGrade: 
            GPA3 = 3
        elif "C" in self.ThirdPeriodGrade: 
            GPA3 = 2
        elif "D" in self.ThirdPeriodGrade:
            GPA3 = 1
        elif "F" in self.ThirdPeriodGrade: 
            GPA3 = 0
        
        if "A" in self.FourthPeriodGrade: 
            GPA4 = 4
        elif "B" in self.FourthPeriodGrade: 
            GPA4 = 3
        elif "C" in self.FourthPeriodGrade: 
            GPA4 = 2
        elif "D" in self.FourthPeriodGrade:
            GPA4 = 1
        elif "F" in self.FourthPeriodGrade:
            GPA4 = 0
        
        if "A" in self.FifthPeriodGrade: 
            GPA5 = 4
        elif "B" in self.FifthPeriodGrade: 
            GPA5 = 3
        elif "C" in self.FifthPeriodGrade: 
            GPA5 = 2
        elif "D" in self.FifthPeriodGrade: 
            GPA5 = 1
        elif "F" in self.FifthPeriodGrade: 
            GPA5 = 0

        if "A" in self.SixthPeriodGrade: 
            GPA6 = 4
        elif "B" in self.SixthPeriodGrade:
            GPA6 = 3
        elif "C" in self.SixthPeriodGrade: 
            GPA6 = 2
        elif "D" in self.SixthPeriodGrade:
            GPA6 = 1
        elif "F" in self.SixthPeriodGrade: 
            GPA6 = 0

        if "A" in self.SeventhPeriodGrade: 
            GPA7 = 4
        if "B" in self.SeventhPeriodGrade:
            GPA7 = 3
        if "C" in self.SeventhPeriodGrade:
            GPA7 = 2
        if "D" in self.SeventhPeriodGrade:
            GPA7 = 1
        if "F" in self.SeventhPeriodGrade: 
            GPA7 = 0

        TotalGPA = (GPA1 + GPA2 + GPA3 + GPA4 + GPA5 + GPA6 + GPA7)/7
        x = TotalGPA
        Total_GPA = round(x, 2)
        return Total_GPA
    
        

Data = School("Butler Traditional", "Bears", 1600, 1954, "William Allen")
# Statement = Data.GetPrincipal()
# print(Statement)
# Mascot = Data.GetMascot()
# print(Mascot)
Student = StudentDemographic("Julia", 16, "11111 ABC Court Louisville, KY 22222", 11, 5021112222)
# Name = Student.GetName()
# print(Name)
# Grade = Student.GetGrade()
# print(Grade)
# Age = Student.GetAge()
# print(Age)
Data2 = StudentGrades("A", "A", "A", "A", "A", "A", "A")
# Statement2 = Data2.GetGPA()
# print(f"{Student.Name}'s unweighted GPA is:\n{Statement2}")

Data3 = School("PRP", "Tiger", 1200, 1958, "Kim Salyer")
# Statement_2 = Data3.GetPrincipal()
# print(Statement_2)
# Mascot2 = Data3.GetMascot()
# print(Mascot2)
Student2 = StudentDemographic("Ray", 16, "22222 ABC Court Louisville, KY 333333", 10, 5021113333)
# Name2 = Student2.GetName()
# print(Name2)
# Grade2 = Student2.GetGrade()
# print(Grade2)
# Age2 = Student2.GetAge()
# print(Age2)
Data_3 = StudentGrades("A", "C", "A", "B", "A", "B", "A")
# Statement3 = Data3.GetGPA()
# print(Statement3)
print (f'{Student.Name} attends {Data.SchoolName} High School and has a GPA of {Data2.GetGPA()}')
print (f'{Student2.Name} attends {Data3.SchoolName} High School and has a GPA of {Data_3.GetGPA()}')