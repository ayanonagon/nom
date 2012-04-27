"""Contains class information for Restaurants and Items"""

class Restaurant(object):
    def __init__(self, city, address, min_order, name, delivery_time, 
            is_delivering, rid, tags):
        self._city = city
        self._address = address
        self._min_order = min_order
        self._name = name
        self._delivery_time = delivery_time
        self._is_delivering = is_delivering
        self._rid = rid
        self._tags = tags


    @property
    def city(self):
        return self._city
    @property
    def address(self):
        return self._address
    @property
    def min_order(self):
        return self._min_order
    @property
    def name(self):
        return self._name
    @property
    def delivery_time(self):
        return self._delivery_time
    @property
    def is_delivering(self):
        return self._is_delivering
    @property
    def rid(self):
        return self._rid
    @property
    def tags(self):
        return self._tags