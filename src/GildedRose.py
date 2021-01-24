class Inventory(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            item.update_quality()


class Item:
    def __init__(self, name, quality, sell_in):
        self.name = name
        self.quality = quality
        self.sell_in = sell_in

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.quality, self.sell_in)

    # holaholahola esto lo estoy escribiendo desde rama Berta
    # jjbujbub


class Updateable:
    # def ItemTypes():
    #     AgedItems=['AgedBrie']
    #     EventItems=['Backstage']
    #     Legendaries=['Sulfuras']
    #     Conjured=[]

    def update_quality(self):
        pass


class ConjuredItem(Item, Updateable):
    def __init__(self, name, quality, sell_in):
        Item.__init__(self, name, sell_in, quality)


class NormalItem(Item, Updateable):
    def __init__(self, name, quality, sell_in):
        Item.__init__(self, name, sell_in, quality)


class Sulfuras(NormalItem):
    def __init__(self, name, quality, sell_in):
        Item.__init__(self, name, sell_in, quality)

    def update_quality(self):

        pass


class AgedBrie(NormalItem):
    def __init__(self, name, quality, sell_in):
        Item.__init__(self, name, sell_in, quality)

    def update_quality(self):

        pass


class Backstage(NormalItem):
    def __init__(self, name, quality, sell_in):
        Item.__init__(self, name, quality, sell_in)

    def update_quality(self):

        if self.sell_in > 10:
            self.quality += 1
        elif self.sell_in > 5:
            self.quality += 2
        elif self.sell_in > 0:
            self.quality += 3
        elif self.sell_in == 0:
            self.quality = 0
        return self.quality

####REFACTORIZABLE BRO####
