from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///test.db"
db = SQLAlchemy(app)
   
class All_user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(200), nullable=False)
    role=db.Column(db.String(200), nullable=False) #just Teacher and student
    course=db.Column(db.String(200), nullable=True)
    def __init__(self, name, role, course):
        self.name=name
        self.role=role
        self.course=course
    def __repr__(self):
        return  f"user('{self.id}','{self.name}','{self.role}','{self.course}')"

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    c_name=db.Column(db.String(200), nullable=False)
    def __init__(self, c_name):
        self.c_name=c_name
    def __repr__(self):
        return  f"user('{self.id}','{self.c_name}')"
db.create_all()

class database():
    def add_user(self,name, role, course):
        a=All_user(name, role, course)
        db.session.add(a)
        db.session.commit()
    def delete_user(self,id):
        a=All_user.query.get_or_404(id)
        db.session.delete(a)
        db.session.commit()
    def add_course(self,c_name):
        a=Course(c_name)
        db.session.add(a)
        db.session.commit()
    def delete_course(self,id):
        a=Course.query.get_or_404(id)
        db.session.delete(a)
        db.session.commit()
    def get_managae_data(self):
        teacher_list=db.session.query(All_user).filter(All_user.role=='teacher').all()
        teacher_list=[{
            'id':x.id,
            'name':x.name,
            'role':x.role,
            'course':x.course
        } for x in teacher_list]
        stu_list=db.session.query(All_user).filter(All_user.role=='student').all()
        stu_list=[{
            'id':x.id,
            'name':x.name,
            'role':x.role,
            'course':x.course
        } for x in stu_list]
        course_list=db.session.query(Course).all()
        course_list=[{
            'id':x.id,
            'c_name':x.c_name,
        } for x in course_list]
        return{
            'teacher_list':teacher_list,
            'stu_list':stu_list,
            'course_list':course_list,
            'teacher_num':len(teacher_list),
            'stu_num':len(stu_list),
            'message':{
                'new':2,
                'mess_list':[
                    {
                        'title':'Học Phí tháng 6',
                        'content':'Bạn chưa thanh toán học phí tháng 6',
                        'date':'6/6/2021'
                    },
                    {
                        'title':'Học Phí tháng 5',
                        'content':'Bạn chưa thanh toán học phí tháng 5',
                        'date':'5/5/2021'
                    },
                    {
                        'title':'Học Phí tháng 4',
                        'content':'Bạn chưa thanh toán học phí tháng 4',
                        'date':'4/4/2021'
                    }
                ]
            },
            'calendar':[
                {
                    'date':'26-7-2021',
                    'start':'19:30',
                    'end':'21:00',
                    'content':'READING'
                },
                {
                    'date':'27-7-2021',
                    'start':'17:30',
                    'end':'19:00',
                    'content':'LISTENING'
                },
               {
                    'date':'29-7-2021',
                    'start':'17:30',
                    'end':'19:00',
                    'content':'WRITING'
                },
               {
                    'date':'30-7-2021',
                    'start':'17:30',
                    'end':'19:00',
                    'content':'SPEAKING'
                },
            ],
           'courseInfo':[
                {
                    'coursename':'IELTS 2',
                    'paymentstatus':'-1 000 000 vnd',
                    'teachername':'Ngo Bao Chau',
                    'start':'2020-12-25',
                    'end':'2021-06-27'
                },
                {
                    'coursename':'IELTS 1',
                    'paymentstatus':'Paid',
                    'teachername':'Tran Thuy Duong',
                    'start':'2020-03-25',
                    'end':'2021-11-20'
                }
            ]
        }
Database=database()
