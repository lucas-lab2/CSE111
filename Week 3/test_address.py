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

def test_extract_state():
    """Verify that the extract_state function works correctly.
    Parameters: none
    Return: nothing
    """
    # Call the extract_state function and verify that it returns a string.
    state = extract_state("123 Main St., Rexburg, ID 83440")
    assert isinstance(state, str), "extract_state function must return a string"

    # Call the extract_state function ten times and use an assert
    # statement to verify that the string returned by the
    # extract_state function is correct each time.
    assert extract_state("123 Main St., Rexburg, ID 83440") == "ID"
    assert extract_state("123 Elm St., Provo, UT 84601") == "UT"
    assert extract_state("123 Oak St., Boise, ID 83701") == "ID"
    assert extract_state("123 Pine St., Pocatello, ID 83201") == "ID"
    assert extract_state("123 Cedar St., Idaho Falls, ID 83401") == "ID"
    assert extract_state("123 Birch St., Logan, UT 84321") == "UT"
    assert extract_state("123 Maple St., Salt Lake City, UT 84101") == "UT"
    assert extract_state("123 Spruce St., Ogden, UT 84401") == "UT"
    assert extract_state("123 Walnut St., St. George, UT 84770") == "UT"
    assert extract_state("123 Ash St., Twin Falls, ID 83301") == "ID"

def test_extract_zipcode():
    """Verify that the extract_zipcode function works correctly.
    Parameters: none
    Return: nothing
    """
    # Call the extract_zipcode function and verify that it returns a string.
    zipcode = extract_zipcode("123 Main St., Rexburg, ID 83440")
    assert isinstance(zipcode, str), "extract_zipcode function must return a string"

    # Call the extract_zipcode function ten times and use an assert
    # statement to verify that the string returned by the
    # extract_zipcode function is correct each time.
    assert extract_zipcode("123 Main St., Rexburg, ID 83440") == "83440"
    assert extract_zipcode("123 Elm St., Provo, UT 84601") == "84601"
    assert extract_zipcode("123 Oak St., Boise, ID 83701") == "83701"
    assert extract_zipcode("123 Pine St., Pocatello, ID 83201") == "83201"
    assert extract_zipcode("123 Cedar St., Idaho Falls, ID 83401") == "83401"
    assert extract_zipcode("123 Birch St., Logan, UT 84321") == "84321"
    assert extract_zipcode("123 Maple St., Salt Lake City, UT 84101") == "84101"
    assert extract_zipcode("123 Spruce St., Ogden, UT 84401") == "84401"
    assert extract_zipcode("123 Walnut St., St. George, UT 84770") == "84770"
    assert extract_zipcode("123 Ash St., Twin Falls, ID 83301") == "83301"

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])