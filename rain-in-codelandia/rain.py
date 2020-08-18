"""How much rain is trapped in Codelandia?

No buildings mean no rain is captured::

    >>> rain([])
    0

All-same height buildings capture no rain::

    >>> rain([10])
    0

    >>> rain([10, 10])
    0

    >>> rain([10, 10, 10, 10])
    0

If there's nothing between taller buildings, no rain is captured::

    >>> rain([2, 3, 10])
    0

    >>> rain([10, 3, 2])
    0

If two tallest buildings are same height and on ends, it's easy::

    >>> rain([10, 5, 10])
    5

    >>> rain([10, 2, 3, 4, 10])
    21

    >>> rain([10, 4, 3, 2, 10])
    21

    >>> rain([10, 2, 4, 3, 10])
    21

If two tallest buildings are ends, but not the same height,
it will fall off the shorter of the two::

    >>> rain([10, 2, 3, 4, 9])
    18

Rain falls off the left and right edges::

    >>> rain([2, 3, 10, 5, 5, 10, 3, 2])
    10

Trickier::

    >>> rain([2, 3, 5, 4, 3, 10, 7, 10, 5, 4, 3, 6, 2, 5, 2])
    15

Should also work with floats::

    >>> r = rain([4.5, 2.2, 2.2, 4])
    >>> round(r, 2)
    3.6
"""

def tallest_to_left(buildings):
    ret = []
    tallest_so_far = 0
    for b in buildings:
        ret.append(tallest_so_far)
        if b > tallest_so_far:
            tallest_so_far = b
    return ret

def tallest_to_right(buildings):
    return tallest_to_left(buildings[::-1])[::-1]
  
def min_height(tall_left, tall_right):
    ret = []
    for i in range(len(tall_left)):
        ret.append(min(tall_left[i], tall_right[i]))
    return ret

def add_water(buildings, min_b_height):
    ret = []
    for i in range(len(buildings)):
        if min_b_height[i] > buildings[i]:
            ret.append(min_b_height[i] - buildings[i])
        else:
            ret.append(0)
    return ret

def rain(buildings):
    """How much rain is trapped in Codelandia?"""
  
    tall_left = tallest_to_left(buildings)
    tall_right = tallest_to_right(buildings)
    min_building_height = min_height(tall_left, tall_right)
    water = add_water(buildings, min_building_height)
    return sum(water)
        
if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YAY!\n")
