
import dropbox

#path="C:/Users/ACER/Downloads/BOOK7 (7).pdf"
path="test.txt"
db=dropbox.Dropbox("XM1_qV2E_T0AAAAAAAAAARAb3HOM6Lz6446Gu28hdwtFLbah5R82mOkU9z44utAB")
f=open(path,'rb')
fileto="/testAvikshit.txt"
db.files_upload(f.read(),fileto)