#Make a class of Student View
class StudentView(object):
    def form_student(self):
        nim = int(input('input nim :'))
        name = input('input name :')
        address = input('input address :')

        data = {
            'nim' : nim,
            'name' : name,
            'address' : address
        }
        return data

    def optional(self):
        print("[1]. view : \n [2]. exit")
        option = (input('Choose :'))
        return option

    def show_student(self, data):
        print('nim' + ":" + str(data['nim']))
        print('name' + ":" + data['name'])
        print('address' + ":" + data['address'])