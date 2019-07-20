import jwt
import services.exceptions as exc

def generateJwt(id, access_level, level):
    payload = {
            id : id,
            access_level : access_level
        }
    return jwt.encode(payload, 'Makerthone', algorithm = 'HS256').decode('utf-8')

def decodeJwt(jwToken):
    return jwt.decode(jwToken, 'Makerthone', algorithm = 'HS256')

def generateDict(cursor):
    data = cursor.fetchall()
    if data == None:
        raise exc.NotFound
    info = tuple((column[0] for column in cursor.description))
    main_data = []
    for item in data:
        main_data.append({info[i] : item[i] for i in range(len(info))})
    if len(main_data) == 1:
        return main_data[0]
    return main_data