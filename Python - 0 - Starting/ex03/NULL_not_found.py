def NULL_not_found(object: any) -> int:
    msg = None
    match object:
        case None:
            msg = 'Nothing: '
        case bool() if object is False:
            msg = 'Fake: '
        case float() if object != object:
            msg = 'Cheese: '
        case int() if object == 0:
            msg = 'Zero: '
        case str() if not object:
            msg = 'Empty:'
        case _:
            print('Type not found')
            return 1
    
    obj_type = type(object)
    msg += f'{object} {obj_type}'

    print(msg)

    return 0