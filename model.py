#Make a class of Student Model
class StudentModel(object):
    def __init__(self, nim, name, address):
        self.nim = nim
        self.name = name
        self.address = address

    def get_nim(self):
        return self.nim

    def set_nim(self, nim):
        self.nim = nim

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    def getAll(self):
        data = {
            'nim' : '1119101746',
            'name' : 'iky',
            'address' : 'banyuwangi'
        }
        return data