import fdb
from fdb.fbcore import DatabaseError

class Interface:

    def __init__(self, database, user='SYSDBA', password='masterkey', host='localhost', port=3050, immediateConnection=False, databaseAlias='Database') -> None:
        self.__user = user
        self.__host = host
        self.__port = port
        self.__password = password
        self.__database = database
        self.__databaseAlias = databaseAlias
        self.__conn = None
        self.__cursor = None

        if immediateConnection: self.createConnection()

    def __throwMessage(self, type_message, message):
        print('%s => %s' % (type_message, message))

    def createConnection(self) -> bool:
        try:
            self.__conn = fdb.connect(
                user=self.__user,
                password=self.__password,
                host=self.__host,
                database=self.__database,
                port=self.__port,
            )
            self.__cursor = self.__conn.cursor()
        except DatabaseError as error:
            self.__throwMessage('[%s CONNECTION ERROR]' % self.__databaseAlias, error)
            return False
        
        self.__throwMessage('[SUCCESS]', '%s connected' % self.__databaseAlias)
        return True

    def closeConnection(self) -> bool:
        try:
            self.__cursor.close()
            self.__conn.close()
            self.__throwMessage('[SUCCESS]', '%s disconnected' % self.__databaseAlias)
            return True
        except DatabaseError as error:
            self.__throwMessage('[%s CONNECTION ERROR]' % self.__databaseAlias, error)
            return False

    def select(self, query) -> list or False:
        try:
            result = self.__cursor.execute(query)
            return [row for row in result]
        except DatabaseError as error:
            self.__throwMessage('[SQL ERROR]', error)
            return False

    def execute(self, query) -> bool:
        try:    
            self.__cursor.execute(query)
            self.__conn.commit()
            return True
        except DatabaseError as error:
            self.__throwMessage('[SQL ERROR]', error)
            return False