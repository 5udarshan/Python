class Marks:
    def details(self):
        self.roll=int(input("Enter Roll no.:"))
        self.name=str(input("Enter Name:"))
        self.classes=str(input("Enter Class:"))

    def oops(self):
        print("Enter Theory,Internal,Practical of OOP out of 75,25,50")
        self.oops_ext=int(input("Thoery Marks:"))
        self.oops_int=int(input("Internal Marks:"))
        self.oops_prac=int(input("Practical Marks:"))
        self.oops_total=self.oops_ext+self.oops_int+self.oops_prac
        print("OOP's Total",self.oops_total)

    def wp(self):
        print("Enter Theory,Internal,Practical of WP out of 75,25,50")
        self.wp_ext=int(input("Thoery Marks:"))
        self.wp_int=int(input("Internal Marks:"))
        self.wp_prac=int(input("Practical Marks:"))
        self.wp_total=self.wp_ext+self.wp_int+self.wp_prac
        print("WP Total",self.wp_total)

    def dm(self):
        print("Enter Theory,Internal,Practical of DM out of 75,25,50")
        self.dm_ext=int(input("Thoery Marks:"))
        self.dm_int=int(input("Internal Marks:"))
        self.dm_prac=int(input("Practical Marks:"))
        self.dm_total=self.dm_ext+self.dm_int+self.dm_prac
        print("DM Total",self.dm_total)

    def pp(self):
        print("Enter Theory,Internal,Practical of PP out of 75,25,50")
        self.pp_ext=int(input("Thoery Marks:"))
        self.pp_int=int(input("Internal Marks:"))
        self.pp_prac=int(input("Practical Marks:"))
        self.pp_total=self.pp_ext+self.pp_int+self.pp_prac
        print("PP Total",self.pp_total)

    def dbms(self):
        print("Enter Theory,Internal,Practical of DBMS out of 75,25,50")
        self.dbms_ext=int(input("Thoery Marks:"))
        self.dbms_int=int(input("Internal Marks:"))
        self.dbms_prac=int(input("Practical Marks:"))
        self.dbms_total=self.oops_ext+self.oops_int+self.oops_prac
        print("DBMS Total",self.dbms_total)

    def ITtools(self):
        print("Enter Theory,Internal,Practical of ITtools out of 75,25,50")
        self.ITtools_ext=int(input("Thoery Marks:"))
        self.ITtools_int=int(input("Internal Marks:"))
        self.ITtools_prac=int(input("Practical Marks:"))
        self.ITtools_total=self.ITtools_ext+self.ITtools_int+self.ITtools_prac
        print("ITtools total",self.ITtools_total)

    def final_result(self):
        self.result=self.oops_total+self.wp_total+self.dm_total+self.pp_total+self.dbms_total+self.ITtools_total
        self.total=150*6
        self.percentage=(self.result/self.total)*100
        print("Percentage is :",self.percentage)

    def grade(self):
        if(self.percentage>=80):
            print("Grade:O")
            print("Marks: 80 & Above")
            print("Grade Points: 10")
            print("SGPA: 10")
        elif(self.percentage>=70 and self.percentage<80):
            print("Grade:A+")
            print("Marks: 70 to 79.99")
            print("Grade Points: 9")
            print("SGPA: 9 - 9.99")
            print("Position: Excellent")
        elif(self.percentage>=60 and self.percentage<70):
            print("Grade:A")
            print("Marks: 60 to 69.99")
            print("Grade Points: 8")
            print("SGPA: 8 - 8.99")
            print("Position: Very Good")
        elif(self.percentage>=55 and self.percentage<60):
            print("Grade:B+")
            print("Marks: 55 to 59.99")
            print("Grade Points: 7")
            print("SGPA: 7 - 7.99")
            print("Position: Good")
        elif(self.percentage>=50 and self.percentage<55):
            print("grade:B")
            print("Marks: 50 to 54.99")
            print("Grade Points: 6")
            print("SGPA: 6 - 6.99")
            print("position: above average")
        elif(self.percentage>=45 and self.percentage<50):
            print("Grade:C")
            print("Marks: 45 to 49.99")
            print("Grade Points: 5")
            print("SGPA: 5 - 5.99")
            print("Position: Average")
        elif(self.percentage>=40 and self.percentage<45):
            print("Grade:D")
            print("Marks: 40 to 44.99")
            print("Grade Points: 4")
            print("SGPA: 4 - 4.99")
            print("Position: Pass")
        else:
            print("Grade:F")
            print("Marks: Less than 40")
            print("Grade Points: 0")
            print("SGPA: NA")
            print("Position: Fail")

r1=Marks()
r1.details()
r1.oops()
r1.wp()
r1.dm()
r1.pp()
r1.dbms()
r1.ITtools()
r1.final_result()
r1.grade()

    

        









        
