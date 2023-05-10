from Connection.conn import Conn
from Common.CRUD import Crud_Dal

class ProductTypesDal(Crud_Dal):
    def __init__(self):
        self.conn = Conn()
        Crud_Dal.__init__(self, tableName="product_types", conn=self.conn)