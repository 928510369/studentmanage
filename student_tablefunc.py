from sqlalchemy.orm import sessionmaker
from studentmanage import student_tablecreate

Sesson=sessionmaker(bind=student_tablecreate.engine)

sesson=Sesson()
def createobj():
    while True:
        obj=input("创建那种对象 0/教师 1/学生")
        if obj=="0":
            objname=input("对象姓名:")
            objqq=input("对象QQ:")

            member=student_tablecreate.Member(qq=objqq,passwd="123456",name=objname,bestudent=0)
        else:
            objname = input("对象姓名:")
            objqq = input("对象QQ:")

            member = student_tablecreate.Member(qq=objqq, passwd="123456",name=objname, bestudent=1)
        sesson.add(member)
        sesson.commit()
        sign=input("创建成功是否继续创建 是/1 否/0:")
        if sign=='0':
            break
