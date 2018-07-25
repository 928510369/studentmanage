from studentmanage import entityclass
from studentmanage import student_tablefunc
from studentmanage import student_tablecreate
import datetime
class Teacher(object):

    def __init__(self,name,qq):
        self.name=name
        self.qq=qq
        self.teacher_class = []
        self.course_member = []
    def createclass(self,classobj):
        self.classobj=classobj
        self.teacher_class.append(self.classobj)

    def create(self):
        classname=input("请输入课程班级名称")
        coursesum=int(input("请输入课程节数"))
        infomation=student_tablefunc.sesson.query(student_tablecreate.Member).filter(student_tablecreate.Member.qq==self.qq).first()
        print(infomation.name,infomation.qq)
        t1 = entityclass.Teacher(infomation.name ,infomation.qq)
        c1 = entityclass.Course("%s"%(classname), coursesum)
        t1.createclass(c1)


        record=student_tablefunc.sesson.query(student_tablecreate.Member).filter(student_tablecreate.Member.name==t1.name).first()

        role1 = student_tablecreate.Course(teacher_id=record.id,name=c1.name,sum=c1.sum)
        student_tablefunc.sesson.add_all([role1])
        student_tablefunc.sesson.commit()
    def addstudent(self):
        studentinfo = student_tablefunc.sesson.query(student_tablecreate.Member).filter(student_tablecreate.Member.bestudent== 1).all()
        print(studentinfo)
        count=0
        while count<len(studentinfo):
            print("++++打印学生信息++++", studentinfo[count].qq, studentinfo[count].name)
            count+=1
        studentnum=input("你想将那位同学加入到你的班级,请输入他的qq号")
        course = student_tablefunc.sesson.query(student_tablecreate.Course).all()
        count=0
        while count<len(course):
            print("++++打印课程信息++++", course[count].id, course[count].name)
            count+=1
        coursenum=int(input("你想将学生加入到那个课程，请输入课程编号"))
        studentobj=student_tablefunc.sesson.query(student_tablecreate.Member).filter(student_tablecreate.Member.qq==studentnum).first()
        courseobj= student_tablefunc.sesson.query(student_tablecreate.Course).filter(student_tablecreate.Course.id==coursenum).first()
        print(studentobj.id,courseobj.id)
        coursestudent=student_tablecreate.CourseStudent(Course_id=courseobj.id,student_id=studentobj.id)
        student_tablefunc.sesson.add(coursestudent)
        student_tablefunc.sesson.commit()
    def createrecord(self):
        time=datetime.date.today()
        record=student_tablefunc.sesson.query(student_tablecreate.CourseStudent).all()
        count=0
        while count<len(record):
            record_id=record[count].id
            count += 1
            print(record_id)
            coursestru=student_tablefunc.sesson.query(student_tablecreate.CourseStudent).filter(student_tablecreate.CourseStudent.id==record_id).first()
            print(coursestru.student_id,coursestru.Course_id)
            studentinfo = student_tablefunc.sesson.query(student_tablecreate.Member).filter(student_tablecreate.Member.id==coursestru.student_id).first()
            courseinfo=courseobj= student_tablefunc.sesson.query(student_tablecreate.Course).filter(student_tablecreate.Course.id==coursestru.Course_id).first()
            print("请输入%s 在%s  %s的课堂记录:" % (studentinfo.name, time, courseinfo.name))
            sign = input("是否继续 是/1，否/0 :")
            if sign=="0":
                continue
            pingjia=input("请输入%s 在%s  %s的课堂记录:"%(studentinfo.name,time,courseinfo.name))
            stu_record=student_tablecreate.StudentRecord(coursestu_id=record_id,data=time,course_type=pingjia)
            student_tablefunc.sesson.add(stu_record)
            student_tablefunc.sesson.commit()

    def granthomeworkgrade(self):
        record = student_tablefunc.sesson.query(student_tablecreate.CourseStudent).all()
        count = 0
        while count < len(record):

            record_id = record[count].id
            count+=1
            homework=student_tablefunc.sesson.query(student_tablecreate.StudentHomework).filter\
                (student_tablecreate.StudentHomework.coursestu_id==record_id).filter(student_tablecreate.StudentHomework.homeworkgrade=="待定").all()

            if len(homework)==0:
                continue
            else:
                statu = input("是否继续输入成绩 是/1，否/0")
                if statu == "0":
                    break
                else:
                   num=0
                   while num<len(homework):
                       print('课程号',homework[num].courseid.Course_id)
                       print('学生号', homework[num].courseid.student_id)
                       print('第几次',homework[num].jieshu)
                       courseid=homework[num].courseid.Course_id
                       studentid=homework[num].courseid.student_id
                       studentinfo = student_tablefunc.sesson.query(student_tablecreate.Member).filter(student_tablecreate.Member.id == studentid).first()
                       courseinfo = courseobj = student_tablefunc.sesson.query(student_tablecreate.Course).filter(student_tablecreate.Course.id == courseid).first()
                       print(" %s   %s的第%s次课程成绩:" % (studentinfo.name, courseinfo.name,homework[num].jieshu))
                       grade=input("请输入成绩:")
                       homework[num].homeworkgrade=grade

                       student_tablefunc.sesson.commit()
                       statu = input("是否继续 是/1，否/0")
                       if statu=="0":
                           break

                       num+=1


class Student(object):
    def __init__(self, name, qq):
        self.name = name
        self.qq = qq
    def lookgrade(self):
        stu_id=student_tablefunc.sesson.query(student_tablecreate.Member).filter(student_tablecreate.Member.qq==self.qq).first()
        count=0
        while count<len(stu_id.selectcourse):
            coursestuid=stu_id.selectcourse[count].id
            courseid=stu_id.selectcourse[count].Course_id
            studentid=stu_id.selectcourse[count].student_id

            course = student_tablefunc.sesson.query(student_tablecreate.Course).filter(
                student_tablecreate.Course.id == courseid).first()

            coursegrade=student_tablefunc.sesson.query(student_tablecreate.StudentHomework).filter(student_tablecreate.StudentHomework.coursestu_id==coursestuid).all()
            num=0
            while  num<len(coursegrade):
                print("%s 在%s 第%s节 的成绩为%s"%(stu_id.name,course.name,coursegrade[num].jieshu,coursegrade[num].homeworkgrade))
                num+=1
            count+=1

    def lookcourse(self):
       stu_id = student_tablefunc.sesson.query(student_tablecreate.Member).filter(student_tablecreate.Member.qq == self.qq).first()
       count = 0
       while count < len(stu_id.selectcourse):
           course_id = stu_id.selectcourse[count].Course_id
           course = student_tablefunc.sesson.query(student_tablecreate.Course).filter(student_tablecreate.Course.id == course_id).first()
           print("%s 选课 %s"%(stu_id.name,course.name))
           count += 1

    def handhomework(self):
        stu_id = student_tablefunc.sesson.query(student_tablecreate.Member).filter(student_tablecreate.Member.qq == self.qq).first()

        record=student_tablefunc.sesson.query(student_tablecreate.CourseStudent).filter(student_tablecreate.CourseStudent.student_id==stu_id.id).all()
        count=0
        while count<len(record):
            record_id=record[count].id
            course_id=record[count].Course_id
            coursename=student_tablefunc.sesson.query(student_tablecreate.Course).filter(student_tablecreate.Course.id==course_id).first()
            print(coursename.name,coursename.sum)
            num=int(input("请输入%s提交第几节作业:"%(stu_id.name)))
            statue=input("是否继续 是/1 否/0")

            if num>coursename.sum:

                print("请重新输入")
                continue
            elif statue=="0":
                print("提交失败")
                count+=1
                continue
            sign="提交完成"
            homegrade="待定"
            s=student_tablecreate.StudentHomework(coursestu_id=record_id,jieshu=num,homeworkstate=sign,homeworkgrade=homegrade)
            student_tablefunc.sesson.add(s)
            student_tablefunc.sesson.commit()
            count += 1

class Course(object):

    def __init__(self,name,sum):
        self.name = name
        self.sum=sum

if __name__=="__main__":
    t1=Teacher('wang','928510369')
    s1=Student('阿狗','456456415')
    s2=Student("傻牛","553615")
    s3=Student("小王",'41563415')
    c1=Course("高数",10)
    print(c1.name)


    t1.createclass(c1)
    print(t1.teacher_class[0].name)

