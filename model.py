#mahasiswa
class MahasiswaModel(object):
    def __init__(self, nim, nama, alamat):
        self.nim = nim
        self.nama = nama
        self.alamat = alamat
    def getNim(self):
        return self.nim
    def setNim(self, nim):
        self.nim = nim
    def getNama(self):
        return self.nama
    def setNama(self, nama):
        self.nama = nama
    def getAlamat(self):
        return self.alamat
    def setAlamat(self, alamat):
        self.alamat = alamat
    def getAll(self):
        data = {
            'nim' : '1119101746',
            'nama' : 'iky',
            'alamat' : 'banyuwangi'
        }
        return data