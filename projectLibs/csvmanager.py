import csv
import json
import datetime as dt
from filemanagers import FileManager

class CSCManager(FileManager):
    """
    CSV Dosyalarını işlemek için olusturulan ve FileManager dan implement edilen sınıf
    """

    def open_file(self, file_path: str, mode: str):
        self.file = open(file_path,mode,newline="")

    def close_file(self):
        if self.file:
            self.file.close()
    
    def read_entire_file(self, file_path: str) -> list:
        data = []
        with open(file_path,newline="") as csv_file:
            content = csv.reader(csv_file)
            for row in content:
                data.append(row)
        return data 
    
    def read_line_from_file(self, file_path: str) -> list:
        """"Bu fonksiyon csv dosyasının sadece baslıklarını verir"""
        with open(file_path,newline="") as csv_file:
            content = csv.reader(csv_file)
            return next(content)
        
    def write_to_file(self, file_path: str, data:list):
        with open(file_path,"w",newline="") as csv_file:
            content = csv.writer(csv_file)
            content.writerows(data)

    def append_to_file(self, file_path: str, data:list):
        with open(file_path,"a",newline="") as csv_file:
            content=csv.writer(csv_file)
            content.writerows(data)

    def csv_to_json(self,csv_file_path:str,json_file_path:str):
        """CSV dosyalarını,json formatına dönüştüren fonsiyon"""
        #TODO: burda patlama ihtimali, var. BUGa açık dosya..

        data = {}
        headers = self.read_line_from_file(csv_file_path)
        for header in headers:
            data[header] = []

        with open(csv_file_path, newline="") as csv_file:
            content=csv.reader(csv_file)

            for i, row in enumerate(content):
                if i == 0 :
                    continue
                for key_ , value_ in zip(headers,row):
                    data[key_].append(value_)

        with open(json_file_path,"w",newline="") as json_file:
            json.dump(data,json_file,indent=4)

        # BU FONSİYON EKSİK KALMIS
    def update_value_in_cell(self,file_path:str,value_to_replace:str,new_value:str):
        """
        Değiştirilecek olan degerin konumunu bulacak ve yeni ifade ile değiştirecek olan fonsksiyon.
        """
        with open(file_path) as file:
            content = file.read()
        content = content.replace(value_to_replace,new_value)

        #BUG
    def update_cell_by_ref(self,)
        
    def delete_file(self, file_path:str):
        super().delete_file(file_path)

    def get_file_size(self, file_path: str) -> int:
        return super().get_file_size(file_path)
    
    def get_file_creation_time(self, file_path) -> dt:
        return super().get_file_creation_time(file_path)
    
    def get_modification_time(self, file_path: str) -> dt:
        return super().get_modification_time(file_path)
    
