def make_multiset( _list ):
    result = dict()
    for item in _list:
        result[item] = 1 if item not in result.keys() else result[item]+1 
    return result

def ordered_dict( _dict ):
    return [(key, _dict[key]) for key in _dict.keys()]

def reversed_dict( _dict ):
    return { value: key for key, value in zip( _dict.keys(), _dict.values() ) } 

def unique_objects( _list ):
    return len( set( id(item) for item in _list) )
