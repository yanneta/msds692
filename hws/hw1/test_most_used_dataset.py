from most_used_dataset import *


def test_list_of_pairs():
    for i in [5, 25, 41]:
        assert len(list_of_pairs(i)) == i
    info = list_of_pairs(43)
    assert info[-1][0] == 'Harmonized Tariff Schedule of the United States (2023)'
