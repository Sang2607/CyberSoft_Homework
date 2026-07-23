import pandas as pd
class DataReader:
    _reader = {}

    @classmethod #chỉ làm việc với class
    def register(cls, ext, reader):

        cls._reader[ext] = reader

    @classmethod
    def load(cls, path):

        ext = path.split(".")[-1]

        return cls._reader[ext].read(path)
dataReader = DataReader()

class CsvReader(DataReader):

    def read(self, path):
        print("Đọc CSV")
        return pd.read_csv(path)
    
class JsonReader(DataReader):

    def read(self, path):
        print("Đọc JSON")

        return pd.read_json(path)
    
class XmlReader(DataReader):

    def read(self, path):
        print("Đọc XML")
        return pd.read_xml(path,parser='etree')
    
dataReader.register("csv", CsvReader())

dataReader.register("json", JsonReader())

dataReader.register("xml", XmlReader())