# models/mongodb/order.py

from .db import db

class Order:
    # Constructor and field definition
    def __init__(self, orderId, eta, orderPlaced, status, locationLongitude, locationLatitude, deliveryAddress, phoneNumber, specialRequest, packageString, paymentMethod, onSitePickup, amount, sst, voucherDeduction, subtotal, deliveryFee, roundingAdjustment, appWalletDiscount, totalPrice, active, cartItems, vouchers):
        self.orderId = orderId
        self.eta = eta
        self.orderPlaced = orderPlaced
        self.status = status
        self.locationLongitude = locationLongitude
        self.locationLatitude = locationLatitude
        self.deliveryAddress = deliveryAddress
        self.phoneNumber = phoneNumber
        self.specialRequest = specialRequest
        self.packageString = packageString
        self.paymentMethod = paymentMethod
        self.onSitePickup = onSitePickup
        # payment details 
        self.amount = amount
        self.sst = sst
        self.voucherDeduction = voucherDeduction
        self.subtotal = subtotal
        self.deliveryFee = deliveryFee
        self.roundingAdjustment = roundingAdjustment
        self.appWalletDiscount = appWalletDiscount
        self.totalPrice = totalPrice
        self.active = active
        # child objects
        self.cartItems = cartItems
        self.vouchers = vouchers

    # Writes an 'Order' object to the database.
    def save(self):
        db.orders.insert_one({
            'orderId': self.orderId,
            'eta': self.eta,
            'orderPlaced': self.orderPlaced,
            'status': self.status,
            'locationLongitude': self.locationLongitude,
            'locationLatitude': self.locationLatitude,
            'deliveryAddress': self.deliveryAddress,
            'phoneNumber': self.phoneNumber,
            'specialRequest': self.specialRequest,
            'packageString': self.packageString,
            'paymentMethod': self.paymentMethod,
            'onSitePickup': self.onSitePickup,
            'amount': self.amount,
            'sst': self.sst,
            'voucherDeduction': self.voucherDeduction,
            'subtotal': self.subtotal,
            'deliveryFee': self.deliveryFee,
            'roundingAdjustment': self.roundingAdjustment,
            'appWalletDiscount': self.appWalletDiscount,
            'totalPrice': self.totalPrice,
            'active': self.active,
            # child objects
            'cartItems': self.cartItems,
            'vouchers': self.vouchers,
        })