# A demo of the local libraries

from trottertools.WriteOnceDict import WriteOnceDict
from trottertools.myDBTable import myDBTable
from trottertools.mySQLh import mySQLh

sql = "SELECT * FROM information_schema.TABLES" 

SQLh = mySQLh.mySQLh()

results = SQLh._conn.execute(sql)
for this_result in results:
    print(this_result)

