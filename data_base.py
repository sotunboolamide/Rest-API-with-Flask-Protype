from mongoengine import connect


from models import StudentName,Courses

connect('graphene-mongo-example', host='mongomock://localhost', alias='default')

def init_db():
    #Creating the fixtures of the daatabase
    Tobiloba = StudentName(name= 'Tobiloba')
    Tobiloba.save()

    John = StudentName(name='John')
    John.save()

    Ayomide = StudentName(name='Ayomide')
    Ayomide.save()

    MEG101 = Courses(name='MEG101')
    MEG101.save()

    CEG103 = Courses(name='CEG103')
    CEG103.save()

    FSC103 = Courses(name='FSC103')
    FSC103.save()

    # John_profile = Student(StudentName=John, Courses={FSC103,MEG101,CEG103})
    # John_profile.save()

    # Tobiloba_profile = Student(StudentName=Tobiloba,Courses={MEG101,CEG103})
    # Tobiloba_profile.save()

    # Ayomide_profile= Student(StudentName=Ayomide,Courses={FSC103,MEG101})
    # Ayomide_profile.save()
