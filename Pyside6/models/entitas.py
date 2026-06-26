from dataclasses import dataclass

@dataclass
class Student:
    id:int
    nim:str
    nama_lengkap:str
    jurusan:str
    tanggal_masuk:str

    #tanpa dataclass nanti kita harus buat konstruktor sendiri , kek __ini__()
    
