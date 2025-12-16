def all_thing_is_obj(object: any) -> int:
    obj_type = type(object)

    msg = None
    match object:
        case list():
            msg = f"List : {obj_type}"
        case tuple():
            msg = f"Tuple : {obj_type}"
        case set():
            msg = f"Set : {obj_type}"
        case dict():
            msg = f"Dict : {obj_type}"
        case str():
            msg = f"{object} is in the kitchen : {obj_type}"
        case _:
            msg = "Type not found"
    
    print(msg)

    return 42