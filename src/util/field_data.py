
field_id_rgb = {
    (255, 255, 255): 0,  # default
    (0, 0, 0): 1,        # stone
    (0, 255, 0): 2       # ground
}

"""
subtypes

lu - left-up corner
u - up border
ru - right-up corner

l - left border
c - center
r - right border

lb - left-bottom corner
b - bottom border
rb - right-bottom corner

s - separated single
vo - vertical "overhang"
ho - horizontal "overhang"

lt - left "tip"
ut - up "tip"
rt - right "tip"
bt - bottom "tip"
"""

field_neighbor_sub = {
    # left, up, right, bottom  :  subtype
    (0, 0, 1, 1): 'lu',
    (1, 0, 1, 1): 'u',
    (1, 0, 0, 1): 'ru',
    (0, 1, 1, 1): 'l',
    (1, 1, 1, 1): 'c',
    (1, 1, 0, 1): 'r',
    (0, 1, 1, 0): 'lb',
    (1, 1, 1, 0): 'b',
    (1, 1, 0, 0): 'rb',
    (0, 0, 0, 0): 's',
    (0, 1, 0, 1): 'vo',
    (1, 0, 1, 0): 'ho',
    (1, 0, 0, 0): 'lt',
    (0, 1, 0, 0): 'ut',
    (0, 0, 1, 0): 'rt',
    (0, 0, 0, 1): 'bt',
}


def rgb_to_id(rgb):
    rgb_key = (rgb[0], rgb[1], rgb[2])
    if rgb_key in field_id_rgb:
        return field_id_rgb[rgb_key]
    else:
        return 0


def get_indicator(field_id, left, up, right, bottom):
    if field_id == 0:
        return ''
    return field_neighbor_sub[(left, up, right, bottom)]
