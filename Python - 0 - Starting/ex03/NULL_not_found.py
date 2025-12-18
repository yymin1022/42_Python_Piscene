def NULL_not_found(object: any) -> int:
    obj_type = type(object)

    match object:
        case None:
            print(f'Nothing: {object} {obj_type}')
        case bool() if object is False:
            print(f'Fake: {object} {obj_type}')
        case float() if object != object:
            print(f'Cheese: {object} {obj_type}')
        case int() if object == 0:
            print(f'Zero: {object} {obj_type}')
        case str() if not object:
            print(f'Empty: {obj_type}')
        case _:
            print('Type not found')
            return 1

    return 0