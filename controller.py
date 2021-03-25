import unittest
from model import StudentModel
from view import StudentView

#Make a class of Student Controller
class StudentController(object):
    def create_student(self):
        view = StudentView()
        data = view.form_student()

        return data

    def show(self,data):
        view = StudentView()
        option = view.optional()

        if option == '1':
            self.view_student(data)
        elif option == '2':
            print('stop')
        else:
            print('404 error')
            self.show(data)

    def view_student(self, data):
        view = StudentView()
        view.show_student(data)
        self.show(data)

    def run(self):
        register = self.create_student()
        nim = register['nim']
        name = register['name']
        address = register['address']

        data = StudentModel(nim, name, address)

        data_student = data.getAll()
        self.show(data_student)
