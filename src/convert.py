from PIL import Image
from src.util.field_data import rgb_to_id, get_indicator
import numpy, pandas

# level name
lvl_name = 'level1'

# raw field ids
raw_fields = []

# open image and read
with Image.open(f'images/{lvl_name}.png') as img:

    # converts image to table of rgb values
    pixels = numpy.array(img)

    # for each row of pixels in pixel table
    for pixel_row in pixels:
        id_row = []  # field ids

        # for each rgb value in pixel row
        for pix in pixel_row:
            id_row.append(rgb_to_id(pix))

        raw_fields.append(id_row)


# field ids with field subtype indicators
y_size = len(raw_fields)
x_size = len(raw_fields[0])
full_fields = [[None for i in range(x_size)] for j in range(y_size)]

# iterate over every field
for y in range(y_size):
    for x in range(x_size):

        # reading raw id
        field_id = raw_fields[y][x]

        # neighbor-fields-occupied indicator list
        # border-fields count as having a neighbor on the outer side
        left_n = 1 if x == 0 or not raw_fields[y][x - 1] == 0 else 0
        up_n = 1 if y == 0 or not raw_fields[y - 1][x] == 0 else 0
        right_n = 1 if x == x_size - 1 or not raw_fields[y][x + 1] == 0 else 0
        bottom_n = 1 if y == y_size - 1 or not raw_fields[y + 1][x] == 0 else 0

        # get field subtype indicator
        field_indicator = get_indicator(field_id, left_n, up_n, right_n, bottom_n)

        # save to new table
        full_fields[y][x] = str(field_id)+field_indicator


# save level as csv
pandas.DataFrame(full_fields).to_csv(f'levels/{lvl_name}.csv', header=None, index=None)


