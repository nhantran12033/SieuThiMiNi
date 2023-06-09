from DataAccess.PurchaseOrderDetailsDal import PurchaseOrderDetailsDal


class PurchaseOrderDetailsBiz:
    def __init__(self):
        self.dal = PurchaseOrderDetailsDal()

    def get_all_purchase_order_details(self, cond=None, fields="*"):
        result = self.dal.listDataWithJson(where=cond, fields=fields, order_by="purchase_order_id DESC")
        if result:
            return result
        return []

    def add_purchase_order_details(self, data):
        result = self.dal.insert(data=data)
        if result == -1:
            return -1
        return result

    def update_purchase_order_details(self, data, cond):
        result = self.dal.update(update_data=data, where_data=cond)
        if result == -1:
            return -1
        return result

    def delete_purchase_order_details(self, id):
        result = self.dal.update(update_data={"is_active": 0}, where_data={"id": id})
        if result == -1:
            return -1
        return result

    def find_purchase_order_details_with_cond(self, key, value):
        result = self.dal.findDataWithJson(where={"{}".format(key): value})
        if result:
            return result
        return []

    def get_A_from_B(self, A, nameB, valueB):
        result = self.dal.findDataWithJson(fields=A, where={"{}".format(nameB): valueB}, limit=1)

        return result[0]


