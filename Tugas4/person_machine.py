from person import Person
import json
import logging

'''
PROTOCOL FORMAT

string terbagi menjadi 2 bagian, dipisahkan oleh spasi
COMMAND spasi PARAMETER spasi PARAMETER ...

FITUR

- create : untuk membuat record
  request : create
  parameter : nama spasi notelpon
  response : berhasil -> ok
             gagal -> error

- delete : untuk menghapus record
  request: delete
  parameter : id
  response: berhasil -> OK
            gagal -> ERROR

- list : untuk melihat daftar record
  request: list
  parameter: tidak ada
  response: daftar record person yang ada

- get : untuk mencari record berdasar nama
  request: get 
  parameter: nama yang dicari
  response: record yang dicari dalam bentuk json format

- jika command tidak dikenali akan merespon dengan ERRCMD

'''

class PersonMachine:
    def proses(self,string_to_process,connection):
        p = Person()
        s = string_to_process
        cstring = s.split(" ")
        try:
            command = cstring[0].strip()
            if (command=='put'):
                logging.warning("put")
                nama_file = cstring[1].strip()
                p.create_data(nama_file,connection)
                return "OK"
            elif (command=='list'):
                logging.warning("list")
                hasil = p.list_data()
                return json.dumps(hasil)
            elif (command=='get'):
                logging.warning("get")
                nama_file = cstring[1].strip()
                hasil = p.get_data(nama_file,connection)
                return json.dumps(hasil)
            else:
                return "ERRCMD"
        except:
            return "ERROR"


# if __name__=='__main__':
#     # pm = PersonMachine()
#     # hasil = pm.proses("list")
#     # print(hasil)
#     # hasil = pm.proses("get vanbasten")
#     # print(hasil)