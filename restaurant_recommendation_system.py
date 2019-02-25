def recommend(file, price, cuisines_list):
    #Read the file and build the data structures.
    # - a dict of {restaurant name: rating%}
    # - a dict of {price : list of restaurant names}
    # - a dict of {cuisine: list of restaurant names}
    name_to_rating, price_to_names, cuisine_to_names = read_restaurant(file)
        
    #Look for price or cuisines first?
    #Price: Look up the list of restaurant names for the requested price.
    price_filter = price_to_names[price]
        
    #Now we have a list of restaurants in the right price bracket.
    #Need a new list of restaurants that serve one of the cuisines
    cuisine_filter = filter_by_cuisine(cuisines_list, cuisine_to_names, price_filter)

    #Now we have a list of restaurants that are in the price range
    #and serve the the requested cuisine.
    #Need to lookup ratings and sort this list
    for i in range(1,len(cuisine_filter)-1):
        if name_to_rating[cuisine_filter[i]] > name_to_rating[cuisine_filter[i - 1]]:
            swap(cuisine_filter,i - 1, i)

    print(cuisine_filter)


    #Done, return the sorted list.

def filter_by_cuisine(cuisines_list, cuisine_to_names, price_filter):
    cuisine_filter = []
    for name in cuisines_list:
        for restaurant in cuisine_to_names[name]:
            cuisine_filter.append(restaurant)

    final_recommendations = []

    for restaurant in price_filter:
        if restaurant in cuisine_filter:
            final_recommendations.append(restaurant)

    return final_recommendations

def swap(L, pos1, pos2):
    temp = L[pos1]
    L[pos1] = L[pos2]
    L[pos2] = temp

def read_restaurant(file):
    '''(file) -> (dict,dict,dict)

    '''
    name_to_rating = {}
    price_to_names = {}
    cuisine_to_names = {}

    flag = True
    while flag:
        name = file.readline()
        rating = file.readline()
        price = file.readline()
        cuisines = file.readline()

        name = name.rstrip()
        rating = rating.rstrip()
        price = price.rstrip()
        price = price.rstrip('%')
        cuisines = cuisines.rstrip()

        name_to_rating[name] = rating
        
        if price in price_to_names:
            price_to_names[price].append(name)
        else:
            inner_list = [name]
            price_to_names[price] = inner_list

        cuisine_list = cuisines.split(',')

        for cuisine in cuisine_list:
            if cuisine in cuisine_to_names:
                cuisine_to_names[cuisine].append(name)
            else:
                inner_cuisine_list = [name]
                cuisine_to_names[cuisine] = inner_cuisine_list
            
        if(file.readline() != '\n'):
            flag = False

    if '$' not in price_to_names:
        inner_list = []
        price_to_names['$'] = inner_list
    if '$$' not in price_to_names:
        inner_list = []
        price_to_names['$$'] = inner_list
    if '$$$' not in price_to_names:
        inner_list = []
        price_to_names['$$$'] = inner_list
    if '$$$$' not in price_to_names:
        inner_list = []
        price_to_names['$$$$'] = inner_list
        
    return (name_to_rating, price_to_names, cuisine_to_names)
