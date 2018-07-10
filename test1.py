# -- coding: utf-8 --

import time,unittest,pyodbc,socket

PC_NAME = socket.gethostname()
SERVER = PC_NAME+'\\ZOOLOGIC'


class GlobalID(unittest.TestCase):

    def setear_global_ids(self):
        """Setea el campo GLOBALID de la tabla [DRAGONFISH_REP 002].[ZooLogic].[CLI]."""

        # Parameters
        db = 'DRAGONFISH_REP 002'

        # Create the connection
        conn = pyodbc.connect('DRIVER={SQL SERVER};SERVER=' + SERVER + ';DATABASE=' + db + ';Trusted_Connection=yes')

        # Create a cursor
        cur = conn.cursor()

        # Execute query
        cur.execute(u"UPDATE [DRAGONFISH_REP 002].[ZooLogic].[CLI] SET GLOBALID = 'D8870D15-BB03-43F8-A86E-486466ABFA37' where CLCOD = '0000000001'")    
        cur.execute(u"UPDATE [DRAGONFISH_REP 002].[ZooLogic].[CLI] SET GLOBALID = '9D5EFE99-EDD7-4694-9C8A-937DCC900879' where CLCOD = '0000000002'")    
        cur.execute(u"UPDATE [DRAGONFISH_REP 002].[ZooLogic].[CLI] SET GLOBALID = '4CBEAF6E-E8AC-4D97-BB73-7C35CE383B3D' where CLCOD = '0000000003'")    
        cur.execute(u"UPDATE [DRAGONFISH_REP 002].[ZooLogic].[CLI] SET GLOBALID = '892B844D-AA9F-40B2-A03B-AA3A703AB295' where CLCOD = '0000000004'")            

        conn.commit()
        cur.close()
        conn.close()


if __name__ == "__main__":
    unittest.main()
