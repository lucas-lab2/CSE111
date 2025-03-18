from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    """Verify that the make_full_name function works correctly.
    Parameters: none
    Return: nothing
    """
    # Call the make_full_name function and verify that it returns a string.
    full_name = make_full_name("Sally", "Brown")
    assert isinstance(full_name, str), "make_full_name function must return a string"

    # Call the make_full_name function ten times and use an assert
    # statement to verify that the string returned by the
    # make_full_name function is correct each time.
    assert make_full_name("Sally", "Brown") == "Brown; Sally"
    assert make_full_name("John", "Smith") == "Smith; John"
    assert make_full_name("Mary", "Jones") == "Jones; Mary"
    assert make_full_name("Joe", "Black") == "Black; Joe"
    assert make_full_name("Jane", "White") == "White; Jane"
    assert make_full_name("Bill", "Green") == "Green; Bill"
    assert make_full_name("Jill", "Red") == "Red; Jill"
    assert make_full_name("Jack", "Blue") == "Blue; Jack"
    assert make_full_name("Jill", "Purple") == "Purple; Jill"
    assert make_full_name("John", "Orange") == "Orange; John"
   
def test_extract_family_name():
    """Verify that the extract_family_name function works correctly.
    Parameters: none
    Return: nothing
    """
    # Call the extract_family_name function and verify that it returns a string.
    family_name = extract_family_name("Brown; Sally")
    assert isinstance(family_name, str), "extract_family_name function must return a string"

    # Call the extract_family_name function ten times and use an assert
    # statement to verify that the string returned by the
    # extract_family_name function is correct each time.
    assert extract_family_name("Brown; Sally") == "Brown"
    assert extract_family_name("Smith; John") == "Smith"
    assert extract_family_name("Jones; Mary") == "Jones"
    assert extract_family_name("Black; Joe") == "Black"
    assert extract_family_name("White; Jane") == "White"
    assert extract_family_name("Green; Bill") == "Green"
    assert extract_family_name("Red; Jill") == "Red"
    assert extract_family_name("Blue; Jack") == "Blue"
    assert extract_family_name("Purple; Jill") == "Purple"
    assert extract_family_name("Orange; John") == "Orange"

def test_extract_given_name():
    """Verify that the extract_given_name function works correctly.
    Parameters: none
    Return: nothing
    """
    # Call the extract_given_name function and verify that it returns a string.
    given_name = extract_given_name("Brown; Sally")
    assert isinstance(given_name, str), "extract_given_name function must return a string"

    # Call the extract_given_name function ten times and use an assert
    # statement to verify that the string returned by the
    # extract_given_name function is correct each time.
    assert extract_given_name("Brown; Sally") == "Sally"
    assert extract_given_name("Smith; John") == "John"
    assert extract_given_name("Jones; Mary") == "Mary"
    assert extract_given_name("Black; Joe") == "Joe"
    assert extract_given_name("White; Jane") == "Jane"
    assert extract_given_name("Green; Bill") == "Bill"
    assert extract_given_name("Red; Jill") == "Jill"
    assert extract_given_name("Blue; Jack") == "Jack"
    assert extract_given_name("Purple; Jill") == "Jill"
    assert extract_given_name("Orange; John") == "John"


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])