from Connection.conn import Conn
from Common.CRUD import Crud_Dal


class InvoiceDetailsDal(Crud_Dal):
    def __init__(self):
        self.conn = Conn()
        Crud_Dal.__init__(self, tableName="invoice_details", conn=self.conn)
