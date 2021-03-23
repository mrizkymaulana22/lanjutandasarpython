class MahasiswaView(object):
    def formMahasiswa(self):
        nim = int(input('input nim :'))
        nama = input('input nama :')
        alamat = input('input alamat :')

        data = {
            'nim' : nim,
            'nama' : nama,
            'alamat' : alamat
        }
        return data
    def pilihPengaturan(self):
        print("[1]. view : \n [2]. exit")
        option = (input('Pilih :'))
        return option
    def tampilMahasiswa(self, data):
        print('nim' + ":" + str(data['nim']))
        print('nama' + ":" + data['nama'])
        print('alamat' + ":" + data['alamat'])