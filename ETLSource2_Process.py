from  Common.ClassHandleData import dataReader as dr

endpoin = "RawData/ETLFile/"
dfcsv = dr.load(endpoin + "source2.csv")
dfjson = dr.load(endpoin + "source2.json")
result = dr.concat_dataFrame(dfcsv,dfjson)
print(result)