import pytest
import csv
import json
from parse import parse_to_csv
from create import create_fixed_width_file


@pytest.fixture
def normal_data():
    return [
        ['a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1', 'i1', 'j1'], 
        ['a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2', 'i2', 'j2'], 
        ['a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3', 'i3', 'j3'], 
        ['a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4', 'i4', 'j4'], 
        ['a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5', 'i5', 'j5'], 
        ['a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6', 'i6', 'j6'], 
    ]



@pytest.fixture
def data_with_delimiter():
    return [
        ['a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1', 'i1', 'j,1'], 
        ['a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2', 'i,2', 'j2'], 
        ['a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3', 'i3', 'j3'], 
        ['a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', ',h4', 'i4', 'j4'], 
        ['a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5', 'i5', 'j5'], 
        ['a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6', 'i6', 'j6'], 
    ]

@pytest.fixture
def spec_file_with_header():
    return '/data/spec.json'


@pytest.fixture
def spec_file_without_header():
    specfile_old = '/data/spec.json'
    specfile_new = '/data/spec_new.json'

    # Read old spec file
    with open(specfile_old) as f_json:
        spec = json.load(f_json)
    
    spec['IncludeHeader'] = 'False'

    # Write to new spec file
    with open(specfile_new, 'w') as f_json:
        json.dump(spec, f_json)

    return specfile_new


def test_parse_normal_with_header(spec_file_with_header, normal_data):
    compare_csv(spec_file_with_header, normal_data)


def test_parse_normal_without_header(spec_file_without_header, normal_data):
    compare_csv(spec_file_without_header, normal_data)


def test_parse_delimiter_with_header(spec_file_with_header, data_with_delimiter):
    compare_csv(spec_file_with_header, data_with_delimiter)


def test_parse_delimiter_without_header(spec_file_without_header, data_with_delimiter):
    compare_csv(spec_file_without_header, data_with_delimiter)


def read_csv(csv_filename):
    data_csv = []
    with open(csv_filename, newline='') as f_csv:
        reader_csv = csv.reader(f_csv)
        
        for row in reader_csv:
            data_csv += [row]
    return data_csv


def assert_data(data, data_csv, spec):
    if spec['IncludeHeader'].lower() == 'true':
        assert spec['ColumnNames'] == data_csv[0], "Header should be the same."
        assert data == data_csv[1:], "Data should be the same."
    else:
        assert data == data_csv, "Data should be the same."


def compare_csv(specfile, data):
    fixed_width_filename = '/data/fixed1.data'
    csv_filename = '/data/csv1.csv'

    create_fixed_width_file(specfile, fixed_width_filename, data)
    parse_to_csv(specfile, fixed_width_filename, csv_filename)
    
    # Read spec file
    with open(specfile) as f_json:
        spec = json.load(f_json)

    data_csv = read_csv(csv_filename)

    assert_data(data, data_csv, spec)

