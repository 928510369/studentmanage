from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String,ForeignKey,Integer,DATE
from sqlalchemy.orm import relationship

engine=create_engine("mysql+pymysql://root:1234@localhost:3306/studentmanage?utf-8",encoding='utf-8')

Base=declarative_base()
class Member(Base):
    __tablename__='member'
    id=Column(Integer,primary_key=True)
    qq=Column(String(32))
    passwd=Column(String(32))
    name=Column(String(64))
    bestudent=Column(Integer)


class Course(Base):
    __tablename__='course'
    id=Column(Integer,primary_key=True)
    teacher_id=Column(Integer,ForeignKey("member.id"))
    name=Column(String(32))
    sum=Column(Integer)
    check1 = relationship("Member",  foreign_keys=[teacher_id])

class CourseStudent(Base):
    __tablename__ = 'coursestudent'
    id = Column(Integer, primary_key=True)
    Course_id = Column(Integer, ForeignKey("course.id"))
    student_id = Column(Integer, ForeignKey("member.id"))
    select1=relationship("Course" )
    select2=relationship("Member", backref="selectcourse")
class StudentSelect(Base):
    __tablename__="Student"
    id = Column(Integer, primary_key=True)
    courseselect=Column(Integer,ForeignKey("coursestudent.id"))
    course_grade = Column(String(32))


class StudentRecord(Base):
    __tablename__="studentrecord"
    id = Column(Integer, primary_key=True)
    coursestu_id=Column(Integer,ForeignKey("coursestudent.id"))
    data=Column(String(32))
    course_type=Column(String(32))
    studentnum=relationship("CourseStudent",backref="sturecord",foreign_keys=[coursestu_id])

class StudentHomework(Base):
    __tablename__="studenthomework"
    id = Column(Integer,primary_key=True)
    coursestu_id = Column(Integer, ForeignKey("coursestudent.id"))
    jieshu=Column(Integer)
    homeworkstate=Column(String(32))
    homeworkgrade=Column(String(32))
    courseid=relationship("CourseStudent")

Base.metadata.create_all(engine)
