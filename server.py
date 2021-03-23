# nilai = var // array//list
# studi kasus sequential search
def warkop():
    produk = ['kopi', 'teh', 'susu']  # list
    cari = input('cari data :')
    ketemu = False  # boolean

# perulangan
    for i in range(len(produk)):
        if produk[i] == cari:
            print(f'data Ketemu = {cari}')
            ketemu = True
        break
    else:
         print('Tidak Ketemu')
    return ketemu, cari
print(warkop())