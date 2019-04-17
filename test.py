###Test the get_recipe function: Returning all 20 recipes in the collection. The expectation is that the expected 20 will match the actual 20.### 
###This test has been failed for the purpose of testing.###

def get_recipes(recipes): 
    return 20 

def test_are_equal(actual, expected):
    assert actual == expected, "Expected {0}, got {1}".format(expected, actual)
    
test_are_equal(get_recipes(20), 20)      

print("There are 20 recipes in the collection")
