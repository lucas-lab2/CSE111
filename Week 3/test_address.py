from address import extract_city, extract_state, extract_zipcode
import pytest

def test_extract_city():
    """Verify that the extract_city function works correctly.
    Parameters: none
    Return: nothing
    """
    # Call the extract_city function and verify that it returns a string.
    city = extract_city("123 Main St., Rexburg, ID 83440")
    assert isinstance(city, str), "extract_city function must return a string"

    # Call the extract_city function ten times and use an assert
    # statement to verify that the string returned by the
    # extract_city function is correct each time.
    assert extract_city("123 Main St., Rexburg, ID 83440") == "Rexburg"
    assert extract_city("123 Elm St., Provo, UT 84601") == "Provo"
    assert extract_city("123 Oak St., Boise, ID 83701") == "Boise"
    assert extract_city("123 Pine St., Pocatello, ID 83201") == "Pocatello"
    assert extract_city("123 Cedar St., Idaho Falls, ID 83401") == "Idaho Falls"
    assert extract_city("123 Birch St., Logan, UT 84321") == "Logan"
    assert extract_city("123 Maple St., Salt Lake City, UT 84101") == "Salt Lake City"
    assert extract_city("123 Spruce St., Ogden, UT 84401") == "Ogden"
    assert extract_city("123 Walnut St., St. George, UT 84770") == "St. George"
    assert extract_city("123 Ash St., Twin Falls, ID 83301") == "Twin Falls"

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])