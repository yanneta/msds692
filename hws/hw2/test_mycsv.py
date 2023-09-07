import mycsv

def test_readcsv():
    data_str = 'when,a,b\n2016-08-12,1.2,3\n2016-08-13,3.99003,4.3'
    header, data = mycsv.readcsv(data_str)
    assert(header == ['when', 'a', 'b'])
    lines = [['2016-08-12', '1.2', '3'], ['2016-08-13', '3.99003', '4.3']]
    for i in range(len(data)):
        assert(data[i] == lines[i])
    assert(len(data) == len(lines))
