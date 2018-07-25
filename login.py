from studentmanage import student_tablefunc
from studentmanage import student_tablecreate

from studentmanage.entityclass import Teacher,Student,Course

count=0
while count<=3:
    user = input("请输入用户名:")
    passwd = input("请输入密码:")
    course_user=student_tablefunc.sesson.query(student_tablecreate.Member).filter(student_tablecreate.Member.qq==user).first()
    if user==course_user.qq and passwd==course_user.passwd:
        print(" =============== welcome to studentmanage system=================")

        if course_user.bestudent==0:
            print(" Hello  %s  Teacher "%(course_user.name))
            h=Teacher(course_user.name,user)
            num=input("是否选择登陆 是/1 否/0")
            while num=='1':
                while True:
                    print("hello %s"%(user))
                    print("1: 创建课程班级")
                    print("2: 添加学生")
                    print("3: 创建学生记录")
                    print("4: 批改学生学习成绩")
                    print("5: 退出")
                    selectid = input('请输入你的选择')

                    if selectid=='1':
                        h.create()
                    if selectid=="2":
                        h.addstudent()
                    if selectid=="3":
                        h.createrecord()
                    if selectid=="4":
                        h.granthomeworkgrade()
                    if selectid=="5":
                        break
                num = input("是否选择离开是/0 否/1")

        else:
            print("Hello %s Student"%(course_user.name))
            h = Student(course_user.name,user)
            num = input("是否选择登陆 是/1 否/0")
            while num == '1':
                while True:
                    print("hello %s" % (user))
                    print("1: 查看选课结果")
                    print("2: 提交作业")
                    print("3: 查看班级排名")
                    print("4: 退出")

                    selectid = input('请输入你的选择')

                    if selectid == '1':
                        h.lookcourse()
                    if selectid == "2":
                        h.handhomework()
                    if selectid == "3":
                        h.lookgrade()
                    if selectid == "4":
                        break
                num = input("是否选择离开是/0 否/1")


    else:
        print("登录失败 ")
        count+=1
