from most_used_dataset import list_of_pairs


def test_list_of_pairs():
    for i in [5, 25, 41]:
        assert len(list_of_pairs(i)) == i
    info = list_of_pairs(43)
    assert info[3][0] == 'Crime Data from 2020 to Present'
