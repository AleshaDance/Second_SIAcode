def towers(height, from_tower, to_tower):
    if height == 1:
        print('Move disk 1 from pin {} to {}'.format(from_tower, to_tower))
    else:
        sup_tower = 6 - from_tower - to_tower
        towers(height-1, from_tower, sup_tower)
        print('Move disk {} from pin {} to {}'.format(height, from_tower, to_tower))
        towers(height-1, sup_tower, to_tower)


towers(3, 1, 3)  # towers(*высота, *с какой башни, *на какую башню)
# towers(int(input(Height? )),int(input(From tower? )),int(input(To tower? )))
