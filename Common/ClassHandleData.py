import pandas as pd
from Common.FunctPandasHandle import checkDataFrame

class DataReader:
    _reader = {}

    @classmethod #chỉ làm việc với class
    def register(cls, ext, reader):
        cls._reader[ext] = reader

    @classmethod
    def load(cls, path,parm1 = None):
        ext = path.split(".")[-1]
        #giải lập overload
        if(parm1 is None):
            return cls._reader[ext].read(path)
        else:
            return cls._reader[ext].read(path,parm1)
            
    def concat_dataFrame(self,dataFrame, dataFile):
        if(not (checkDataFrame(dataFrame) and checkDataFrame(dataFile))):
            raise Exception("Param must be DataFrame tpye!")
        result = pd.concat([dataFrame, dataFile], ignore_index=True)
        return result
    
dataReader = DataReader()

class CsvReader(DataReader):

    def read(self, path):
        print("Đã đọc CSV")
        return pd.read_csv(path)
    
class JsonReader(DataReader):

    def read(self, path):
        print("Đã đọc JSON")
        try:
            return pd.read_json(path)
        except ValueError as ex:
            if "Trailing data" in str(ex):
                return pd.read_json(path, lines=True)
            raise
    
class XmlReader(DataReader):

    def read(self, path):
        print("Đã đọc XML")
        return pd.read_xml(path,parser='etree')
    
class XlsxReader(DataReader):
    #không truyền SheetName => lấy hết
    def read(self, path,SheetName=None):
        print("Đã đọc XML")
        return pd.read_excel(path,sheet_name=SheetName)
    
dataReader.register("csv", CsvReader())
dataReader.register("json", JsonReader())
dataReader.register("xml", XmlReader())
dataReader.register("xlsx", XlsxReader())