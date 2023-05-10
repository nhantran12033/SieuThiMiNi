from DataAccess.ProductDal import ProductDal


class ProductBiz:
    def __init__(self):
        self.dal = ProductDal()

    def get_info_prdct(self, cond=None, fields="*"):
        result = self.dal.listDataWithJson(where=cond, fields=fields, order_by="id ASC")
        if result:
            count_active = 0
            count_no_active = 0
            for item in result:
                if item[6] == 1:
                    count_active += 1
                if item[6] == 0:
                    count_no_active += 1
            return {
                "hoatdong": count_active,
                "kohoatdong": count_no_active,
            }
        return 0

    def get_all_product(self, cond=None, fields="*"):
        result = self.dal.listDataWithJson(where=cond, fields=fields, order_by="id DESC")
        if result:
            return result
        return []

    def find_product_with_cond(self, key, value):
        # mặc định nó sẽ tìm 1 row vì t để fetch_one, còn key
        result = self.dal.findDataWithJson(where={"{}".format(key): value})
        if result:
            return result
        return None

    def add_product(self, products):
        result = self.dal.insert(products)
        if result == -1:
            return -1
        return result

    def update_product(self, product, cond):
        result = self.dal.update(update_data=product, where_data=cond)
        if result == -1:
            return -1
        return result

    def update_payment(self, count, cond, key):
        if key == "decrease":
            result = self.dal.update_decrease(count=count, where=cond)
            if result == -1:
                return -1
            return result

        elif key == "increase":
            result = self.dal.update_increase(count=count, where=cond)
            if result == -1:
                return -1
            return result

    def delete_product(self, id):
        result = self.dal.update(update_data={"is_active": 0}, where_data={"id": id})
        if result == -1:
            return -1
        return result

    def get_new_id(seft):
        result = seft.dal.findDataWithJson(fields=['id'], order_by="id DESC", limit=1)

        if result:
            currentId = result[0]
            temp = int(currentId + 1)
            return seft.to_str_id(temp)
        return "SP01"

    def to_str_id(seft, id):
        return "SP0{}".format(id) if id < 10 else "SP{}".format(id)

    def get_A_from_B(self, A, nameB, valueB):
        result = self.dal.findDataWithJson(fields=A, where={"{}".format(nameB): valueB}, limit=1)

        return result[0]





