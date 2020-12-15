import json
import csv
import argparse

#
# Parse fixed width file to delimited file
#
def main():
    """Main function
    """
    parser = argparse.ArgumentParser()
    # parser.add_argument("op", choices=['create', 'parse', 'test'], help="create/parse/test", type=str)
    parser.add_argument("specfile", help="spec Json file", type=str)
    parser.add_argument("fixed_width_filename", help="Fixed width filename to be parsed.", type=str)
    parser.add_argument("output_filename", help="Output delimited filename.", type=str)
    args = parser.parse_args()

    parse_to_csv(args.specfile, args.fixed_width_filename, args.output_filename)
    print(f"File {args.output_filename} is created.")


def parse_to_csv(specfile, fixed_width_filename, output_filename, delimiter=',', lineterminator='\n'):
    """Parse a fixed width file and save to a delimited file.
        Arguments:
        specfile                --- A Json filename containing the fixed width file's specification.
        fixed_width_filename    --- The fixed width filename
        output_filename         --- The output delimited filename
        delimiter               --- The delimiter of output file. Default ','
        linedelimiter           --- The line delimiter of output file. Default '\n'

        Note:
            Assume fixed width file does NOT contain header in the first line. The IncludeHeader flag 
            in spec file only controls if output file will contain header.
    """

    def split_line(spec):
        ## Return a split function to split fixed widht line into record, using the spec.
        ##
        start_index = 0
        end_index = 0

        # A dict containing column name mapping to start and end indices in the fixed width line
        field_def = {}
        for col, offset in zip(spec['ColumnNames'], spec['Offsets']):
            end_index = start_index + int(offset)
            field_def[col] = [start_index, end_index]
            start_index = end_index

        def do_split_line(line):
            row = {}
            for col, indices in field_def.items():
                row[col] = line[indices[0]:indices[1]].strip() # Remove spaces from both ends
            return row

        return do_split_line

    # Read spec file
    with open(specfile) as f_json:
        spec = json.load(f_json)

    # Read fixed width file, parse and save to csv file.
    with open(fixed_width_filename, mode='r', encoding=spec['FixedWidthEncoding']) as f_in, \
        open(output_filename, mode='w', encoding=spec['DelimitedEncoding'], newline='') as f_out:

        writer = csv.DictWriter(f_out, fieldnames=spec['ColumnNames'], delimiter=delimiter, 
            lineterminator=lineterminator, quoting=csv.QUOTE_MINIMAL)

        # The IncludeHeader flag is used to output header in delimited file only.
        # The fixed width file always contains data only (My assumption. Otherwise there should be another
        # flag for flexibility).
        if spec['IncludeHeader'].lower() == 'true':
            writer.writeheader()
        
        split = split_line(spec)
        for line in f_in.readlines():
            writer.writerow(split(line))


if __name__ == '__main__':
    main()