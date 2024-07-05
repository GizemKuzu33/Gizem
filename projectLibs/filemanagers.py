from abc import ABC, abstractmethod

import os

import datetime as dt

class FileManager(ABC):
    """
    Alt sınıflar için soyut sınıf tanımı
    """
    def __init__(self):
        super().__init__()
    
    @abstractmethod
    def open_file(self,filePath:str,mode:str):
        """_summary_

        Args:
            filePath (str): Acılacak olan dosya yolu
            mode(str): dosya açma metodu
        """
        pass

    @abstractmethod
    def close_file(self):
        """
           Açılan dosyaı kapatmak amacıyla kullanılacak fonksiyon
        """
        pass

    @abstractmethod
    def read_entire_file(self,file_path:str)-> str:
         """_summary_

        Args:
            file_Path (str): Acılacak olan dosya yolu
        
        Returns:
             str:Dosyanın içeriğini döndürür
        """
         pass
    
    @abstractmethod
    def read_line_from_file(self,file_path:str)-> str:
         """_summary_

        Args:
            file_Path (str): Acılacak olan dosya yolu
        
        Returns:
             str:Dosyanın içeriğini döndürür
        """
         pass
    
    @abstractmethod
    def write_to_file(self,file_path:str,data:str):
        """_summary_

        Args:
            file_Path (str): Acılacak olan dosya yolu
            data(str): dosyaya yazılacak olan bilgi
        """
        pass

    @abstractmethod
    def append_to_file(self,file_path:str,data:str):
        """_summary_

        Args:
            file_Path (str): Acılacak olan dosya yolu
            data(str): dosyaya yazılacak olan bilgi
        """
        pass
    
    def delete_file(self,file_path:str):
        """Dosyayı tamamı ile siler

         Args:
            file_Path (str): silinecek olan dosya yolu
        """
        try:
            os.remove(file_path)
        except Exception as e:
            print(str(e),"Dosya silme hatası")
        
    def get_file_size(self,file_path:str)->int:
        """Dosya boyutu

        Args:
            file_path(str): Dosya boyutu alınacak olan eleman

        Returns:
            int:Dosya boyutu
        """

        return os.path.getsize(file_path)
    
    def get_file_creation_time(self,file_path)-> dt:
        """Dosyanının olusturulma zamanını döner
        
        Args:
        file_path(_type_): Dosya yolunu belirtir
        
        Returns:
            datetime:Dosyanın olusturuldugu tarih ve saati döner
        """

        return dt.datetime.fromtimestamp(os.path.getctime(file_path))
    
    def get_modification_time(self,file_path:str)->dt:
        """Dosya değiştirilme tarih ve saati
        Args:
           file_path (str) dosya yolu

         Returns:
            dt:Dosyanın degiştirilme tarih ve saatini verir
           
           """
        
        return dt.datetime.fromtimestamp(os.path.getmtime(file_path))
    
if __name__ == "__main__":
   print("Bu dosya direkt olarak çalıstırmak icin yaratılmadı. Git bir yerden import et!!!!")