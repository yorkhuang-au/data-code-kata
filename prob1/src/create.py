import json

def create_fixed_width_file(specfile, fixed_width_filename, data=None):
    """ Helper function to create fixed width file.
        Arguments:
        specfile                --- A Json filename containing the fixed width file's specification.
        fixed_width_filename    --- The fixed width filename
        data                    --- Data to be output. It is a collection of record. Each record is an
                                    array of fields.
    """

    # This function trim every string values in a record according to the lengths in spec.
    def trim_fields(spec, record):
        return [f[0:int(l)] for f, l in zip(record, spec['Offsets'])]

    # Read spec file
    with open(specfile) as f_json:
        spec = json.load(f_json)

    # If there is no data, create 10 dummy records
    if not data:
        row_size = len(spec['Offsets'])
        data = [tuple(['abcde'] * row_size)] * 10

    fmt = ''.join([f"%{offset}s" for offset in spec['Offsets']]) + '\n'

    with open(fixed_width_filename, mode='w', encoding=spec['FixedWidthEncoding']) as f_fixed_width:
        # if spec['IncludeHeader'].lower() == 'true':
        #     f_fixed_width.write(fmt % tuple(trim_fields(spec, spec['ColumnNames'])))

        for row in data:
            f_fixed_width.write(fmt % tuple(trim_fields(spec, row)))

