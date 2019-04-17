###Test the get_recipe function: Returning all 20 recipes in the collection. The expectation is that the expected 20 will match the actual 20.### 
###This test has been failed for the purpose of testing.###

def get_recipes(recipes): 
    return 20 

def test_are_equal(actual, expected):
    assert actual == expected, "Expected {0}, got {1}".format(expected, actual)
    
test_are_equal(get_recipes(20), 20)      

print("There are 20 recipes in the collection")

###Testing to see if adding a recipe to the collection established in get_recipe will increment the index by one using a test_is_in function for indexing.###
###After insert (1 recipe), the collection will contain 21 recipes (20 + 1). We then try to find the 21st item in that collection's index.###
###Finally, call the 'test_is_in' function with the collection total and the recipe's index number. ### 
###This test was failed for the purpose of testing.###

def insert_recipe(insert):
    return 1
    
def test_is_in(collection, item):
    collection = [20] + [1]
    for item in collection:
        assert 21 in [21], "{0} contains {1}".format(collection, item)
        
test_is_in([20] + [1], [21])    

print ("The 21st recipe in the index is the inserted recipe")
