from model import MahasiswaModel
from view import MahasiswaView

class MahasiswaController(object):
    def createMahasiswa(self):
        view = MahasiswaView()
        data = view.formMahasiswa()

        return data
    def tampil(self,data):
        view = MahasiswaView()
        option = view.pilihPengaturan()

        if option == '1':
            self.viewMahasiswa(data)
        elif option == '2':
            print('stop')
        else:
            print('404 error')
            self.tampil(data)

    def viewMahasiswa(self, data):
        view = MahasiswaView()
        view.tampilMahasiswa(data)

        self.tampil(data)
    def run(self):
        register = self.createMahasiswa()
        nim = register['nim']
        nama = register['nama']
        alamat = register['alamat']

        data = MahasiswaModel(nim, nama, alamat)

        datamahasiswa = data.getAll()
        self.tampil(datamahasiswa)
