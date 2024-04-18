import re

pattern = r'@#+([A-Z][a-zA-Z0-9]+[A-Z])@#+'

barcodes_quantity = int(input())

for barcodes in range(barcodes_quantity):
    curr_barcode = input()
    product_group = ''
    matches = re.findall(pattern, curr_barcode)

    if len(matches) > 0:
        if len(matches[0]) > 6:
            for char in matches[0]:
                if char.isdigit():
                    product_group += char
            if matches[0].isalpha():
                product_group = '00'
            print(f'Product group: {product_group}')
        else:
            print('Invalid barcode')
    else:
        print('Invalid barcode')
