import numpy as np
import re

#Radians to degrees coordinate converter

def convert_rads_to_degs(input_file_path, output_file_path):
    with open(input_file_path, 'r') as input_file:
        lines = input_file.readlines()

    convert_coords = []

    for line in lines:
        parts = line.strip().split(' ')
        residue_name = parts[0]
        radian_coords = parts[1:]

        converted_coords = []
        for coord in radian_coords:
            if coord.lower() == 'none':
                converted_coords.append('None')
            else:
                real_coord = re.sub(r'[^-.\d]+', '', coord)
                try:
                    converted_coords.append(str(np.degrees(float(real_coord))))
                except ValueError:
                    converted_coords.append('None')

        converted_line = ' '.join([residue_name] + converted_coords)
        
        convert_coords.append(converted_line)

    with open(output_file_path, 'w') as output_file:
        output_file.write('\n'.join(convert_coords))

input_file_path = r"C:\Users\Tania\Documents\Pr_res_rads.txt"
output_file_path = r"C:\Users\Tania\Documents\rad_to_deg_file.txt"
convert_rads_to_degs(input_file_path, output_file_path)
