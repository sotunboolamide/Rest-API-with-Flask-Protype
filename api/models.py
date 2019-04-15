from mongoengine import Document
from mongoengine.fields import (
    DateTimeField, ReferenceField, StringField,
)
class StudentName(Document):
    meta = {'collection': 'student_name'}
    name = StringField()

class Courses(Document):
    """list of courses taken"""
    meta = {'collection': 'courses'}
    name = StringField()

class Student(Document):
    """docstring fos Student"""
    meta= {'collection':'student'}
    student_name = ReferenceField(StudentName)
    courses = ReferenceField(Courses)

