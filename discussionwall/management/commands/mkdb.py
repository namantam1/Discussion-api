from django.core.management.base import BaseCommand
from discussionwall.models import (
    MyUser,LoginMethod,Subject,StudentClass,StudentBoard,Student
)

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        login_method = ['email','google','facebook']
        klass = ['8th', '9th', '10th']
        board = ['CBSE', 'Other']
        subject = ['Mathematics']
        user = [
            ['mirrorscore','student1','password123',False,'student1@gmail.com','student1',1,1,1],
            ['mirrorscore','student2','password123',False,'student2@gmail.com','student2',2,1,1],
            ['mirrorscore','student3','password123',False,'student3@gmail.com','student3',3,2,1],
            ['mirrorscore','teacher','password123',False,'teacher@gmail.com','teacher',1,1,1],
            ['mirrorscore','admin','password123',True,'admin@gmail.com','admin'],
        ]
        for method in login_method:
            LoginMethod.objects.create(login_method=method)
            print("created loginmethod {}".format(method))
        
        print('------------------------------------------------------------')

        for k in klass:
            StudentClass.objects.create(studentclass=k)
            print("created class {}".format(k))

        print('------------------------------------------------------------')
        for k in board:
            StudentBoard.objects.create(studentboard=k)
            print("created board {}".format(k))

        print('------------------------------------------------------------')
        for k in subject:
            Subject.objects.create(subject=k)
            print("created subject {}".format(k))

        print('------------------------------------------------------------')
        
        for k in user:
            u = MyUser(
                first_name = k[0],
                last_name = k[1],
                email = k[4],
                is_superuser = k[3],
                is_staff = k[3],
                username = k[5]
            )
            u.set_password(k[2])
            u.save()
            if u.is_superuser:
                Student.objects.create(
                    user=u,
                    studentclass=k[6],
                    studentboard=k[7],
                    subject=k[8]
                )
            print("created user {}".format(k[4]))

        