def all_thing_is_obj(object: any) -> int:
    obj_type = type(object)

    result = None
    match object:
        case list():
            result = f'List : {obj_type}'
        case tuple():
            result = f'Tuple : {obj_type}'
        case set():
            result = f'Set : {obj_type}'
        case dict():
            result = f'Dict : {obj_type}'
        case str():
            result = f'{object} is in the kitchen : {obj_type}'
        case _:
            result = "Type not found"
    
    if result is not None:
        print(result)

    return 42