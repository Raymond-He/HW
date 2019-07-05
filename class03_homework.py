class course(): #課程的所有資料
    def __init__(self,code,subject,credits,classification,intro,teacher,time):
        self.code=code
        self.subject=subject
        self.credits=credits
        self.classification=classification
        self.intro=intro
        self.teacher=teacher
        self.time=time
    def show(self):
        print("Course Code:",self.code)
        print("Course Subject:",self.subject)
        print("Course Credits:",self.credits)
        print("Enrollment Classification:",self.classification)
        print("Course Introduction:",self.intro)
        print("Class Teacher:",self.teacher)
        print("Course Time:",self.time)
        print("*****************************************************")
class grade(course): #有修課才有成績
    def __init__(self,code,subject,credits,classification,intro,teacher,time,coursegrade):
        self.coursegrade=coursegrade
    def showgrade(self):
        pass

#======================================================我是分隔線=================================================================
        
class human(): #人員資料(含所選課程)
    def __init__(self,name,ID,chooseclass):
        self.name=name
        self.ID=ID
        self.chooseclass=chooseclass
class student(human): #學生所有資料(含所修課程及該課的成績)
    def __init__(self,name,ID,chooseclass,thisclassgrade):
        super().__init__(name,ID,chooseclass)
        self.thisclassgrade=thisclassgrade
    def showself(self):
        print("Student Name:",self.name)
        print("Student ID:",self.ID)
        for i in self.chooseclass:
            print("修課內容:",i)
            print("This Class Grade:",self.thisclassgrade.pop(0))   
        print("------------------------------------------------")

#======================================================我是分隔線=================================================================

#(code,subject,credits,classification,intro,teacher,time)
#課程所有資料的實體化
Credits=[3,2,3,2,1,2,3,3,1,3]
WebProgramming=course("IECS272","Web程式設計",Credits[0],"選修","教導學生開發Responsive Web應用程式的知識與能力。","陳錫民","(二)10:10-12:00 (四)17:10-18:00")
ShihChi=course("CHIN205","史記",Credits[1],"選修","研讀史記。","楊美美","(四)13:10-15:00")
CryptoGraphy=course("IECS352","密碼學",Credits[2],"選修","概述密碼學及其相關應用的基礎知識。","魏國瑞","(三)18:10-21:00")
Japanese=course("LC101","日文(一)",Credits[3],"選修","從日語的五十音教起，配合選定教材，讓同學活用於日常會話之中。","林盈萱","(三)15:10-17:00")
TopicsStudy=course("COME492","專題研究(二)",Credits[4],"必修","專題討論。","陳益生","(六)12:10-13:00")
Korean=course("LC124","韓文(二)",Credits[5],"選修","本課程希望透過韓文，增進同學對韓國的社會變遷與生活環境有深刻的瞭解。","韓連善","(三)13:10-15:00")
ElectroMagnetics=course("COME21","電磁學(二)",Credits[6],"必修","學習Maxwell's Equation。","林漢年","(二) 10:10~12:00 (四)08:10~09:00")
Compatibility=course("COME413","電磁相容導論",Credits[7],"選修","學習EMI和EMS。","彭嘉美","(四) 09:10~12:00")
Experiments=course("COME414","電磁相容實習",Credits[8],"選修","量測電磁干擾。","林漢年","(三) 13:10~16:00")
Analysis=course("COME634","微波電路分析",Credits[9],"選修","本課程主要在講授微波電路，內容涵蓋阻抗匹配、低雜訊放大器、功率放大器、混頻器等。","何滿龍","(四) 14:10~17:00")
#放在課程下的成績
studentAgrade=grade("","","","","","","",[90,84,80,90,92])
studentBgrade=grade("","","","","","","",[95,84,80])

def CourseDetails(parameters): #印出課程資訊
    for i in parameters:
        i.show()
CourseDetails([WebProgramming,ShihChi,CryptoGraphy,Japanese,TopicsStudy,Korean,ElectroMagnetics,Compatibility,Experiments,Analysis])

#======================================================我是分隔線=================================================================

#實體化學生所有資訊
StudentInformation1=student("老王","D0000000",[TopicsStudy.subject,ElectroMagnetics.subject,Compatibility.subject,Experiments.subject,Analysis.subject],studentAgrade.coursegrade)
StudentInformation2=student("小王","D1111111",[TopicsStudy.subject,WebProgramming.subject,CryptoGraphy.subject],studentBgrade.coursegrade)

def HumanDetails(parameters): #印出學生資料
    for j in parameters:
        j.showself()
HumanDetails([StudentInformation1,StudentInformation2])