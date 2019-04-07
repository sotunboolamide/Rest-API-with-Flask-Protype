import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from models import StudentName as StudentNameModel
from models import Courses as CoursesModel
from models import Student as StudentModel

class StudentName(MongoengineObjectType):

    class Meta:
        model = StudentNameModel
        interfaces = (Node,)

class Courses(MongoengineObjectType):

    class Meta:
        model = CoursesModel
        interfaces = (Node,)

class Student(MongoengineObjectType):

    class Meta:
        model = StudentModel
        interfaces = (Node,)

class Query(graphene.ObjectType):
    node = Node.Field()
    all_students = MongoengineConnectionField(Student)
    all_courses = MongoengineConnectionField(Courses)
    all_names = MongoengineConnectionField(StudentName)

schema = graphene.Schema(query=Query, types=[Student,StudentName,Courses])
