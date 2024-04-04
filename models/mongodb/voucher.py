# models/mongodb/voucher.py

from .db import db

class Voucher:
    def __init__(self, voucher_id=None, image=None, priceDiscount=None, priceDeduct=None, expiryDate=None, activated=None, user=None, order=None):
        self.voucher_id = voucher_id
        self.image = image
        self.priceDiscount = priceDiscount
        self.priceDeduct = priceDeduct
        self.expiryDate = expiryDate
        self.activated = activated
        self.user = user
        self.order = order

    def to_json(self):
        json_data = {
            'voucher_id': self.voucher_id,
            'image': self.image,
            'priceDiscount': self.priceDiscount,
            'priceDeduct': self.priceDeduct,
            'expiryDate': self.expiryDate.isoformat() if self.expiryDate else None,
            'activated': self.activated,
        }
        return json_data