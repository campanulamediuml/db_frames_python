from data.server import Data

res = Data.find('test',[('id','!=',0)])
print(res)