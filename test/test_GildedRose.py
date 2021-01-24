from src.GildedRose import *

# inventario
# sulfuras

# backstage
# brie
# normal


# conjured
# jamon, pata, escoba, libroencantado - -- libroencantad

"""
def ItemTypes():
    AgedItems = ['AgedBrie']
    EventItems = ['Backstage']
    Legendaries = ['Sulfuras']
    Conjured = []
    """


def test_Backstage():
    assert Backstage("backstage_passes", 15, 0).update_quality() == 0
    assert Backstage("backstage_passes", 15, 4).update_quality() == 18
    assert Backstage("backstage_passes", 15, 6).update_quality() == 17
    assert Backstage("backstage_passes", 0, 11).update_quality() == 1
