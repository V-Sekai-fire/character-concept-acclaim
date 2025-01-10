import csv
import os

input_file = './export - Score - Grid.csv'
output_file = './export - Score - Grid_cleaned.csv'

def extract_url(image_field):
    start = image_field.find('(') + 1
    end = image_field.find(')')
    return image_field[start:end]

if os.path.exists(input_file):
    with open(input_file, mode='r', newline='', encoding='utf-8') as infile, \
         open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
        
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        if fieldnames is not None:
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            
            writer.writeheader()
            
            for row in reader:
                if 'Image' in row:
                    row['Image'] = extract_url(row['Image'])
                writer.writerow(row)
        else:
            print("The input CSV file is empty or improperly formatted.")

    print(f"Cleaned CSV file has been saved to {output_file}")
else:
    print(f"Input file {input_file} does not exist.")
