import pytest
import ProductionCode

def test_good_data():
    test_data = ["Hi Hi Hi$#%!#$, There",
                 "There %$^Hi, No"]
    results = ProductionCode.count_words(test_data)
    assert "Hi" in results
    assert results["Hi"] ==4