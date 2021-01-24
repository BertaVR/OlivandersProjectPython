class GildedRose(object):


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class Updatable:
    def update_quality(self):
        pass


class NormalItem(Item, Updatable):


class ConjuredItem(Item, Updatable):


class Sulfuras(NormalItem):


class AgedBrie(NormalItem):


class Backstage(NormalItem)
