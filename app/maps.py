from app import app
from flask import jsonify, request, make_response
from services.addons import generateDict, decodeJwt
import psycopg2
import services.exceptions as  exc

@app.before_request
def before_request():
    conn = psycopg2.connect(dbname = 'obdb', user = 'postgres', password = 'qazwsxedc', host = '172.20.10.3')
    global cursor
    cursor = conn.cursor()

@app.teardown_request
def teardown_request(exception):
    cursor.close()
    print('closed')

@app.route('/map', methods = ['GET', 'POST', 'PUT', 'DELETE'])
def maps():
    if request.method == 'GET':
        cursor.execute("SELECT * FROM spec")
        try:
            specs = generateDict(cursor)
        except exc.NotFound:
            return make_response('Specs not found', 404)
        n_specs = []
        for spec in specs:
            cursor.execute(f"SELECT * FROM courses WHERE id_spec={spec['id']}")
            try:
                dic = generateDict(cursor)
                courses = dic if type(dic) == list else [dic]
            except exc.NotFound:
                return make_response('Specs not found', 404)
            for i in range(len(courses)):
                courses[i].pop('info')
            n_specs.append({'spec' : spec, 'courses' : courses})

        for i in range(len(n_specs)):
            for j in range(len(n_specs[i]['courses'])):
                n_specs[i]['courses'][j]['authors'] = tuple(map(int, n_specs[i]['courses'][j]['authors']))
                if len(n_specs[i]['courses'][j]['authors']) != 1:
                    cursor.execute(f"SELECT first_name, patronymic, last_name FROM people WHERE id in {n_specs[i]['courses'][j]['authors']}")
                else:
                    cursor.execute(f"SELECT first_name, patronymic, last_name FROM people WHERE id={n_specs[i]['courses'][j]['authors'][0]}")
                try:
                    dic = generateDict(cursor)
                    n_specs[i]['courses'][j]['authors'] = dic if type(dic) == list else [dic]
                except exc.NotFound:
                    return make_response('Users not found', 404)

                if n_specs[i]['courses'][j]['curators'] != None:
                    n_specs[i]['courses'][j]['curators'] = tuple(map(int, n_specs[i]['courses'][j]['curators']))
                    if len(n_specs[i]['courses'][j]['curators']) != 1:
                        cursor.execute(f"SELECT first_name, patronymic, last_name FROM people WHERE id in {n_specs[i]['courses'][j]['curators']}")
                    else:
                        cursor.execute(f"SELECT first_name, patronymic, last_name FROM people WHERE id={n_specs[i]['courses'][j]['curators'][0]}")
                    try:
                        dic = generateDict(cursor)
                        n_specs[i]['courses'][j]['curators'] = dic if type(dic) == list else [dic]
                    except exc.NotFound:
                        return make_response('Users not found', 404)
                
                if n_specs[i]['courses'][j]['helpers'] != None:
                    n_specs[i]['courses'][j]['helpers'] = tuple(map(int, n_specs[i]['courses'][j]['helpers']))
                    if len(n_specs[i]['courses'][j]['helpers']) != 1:
                        cursor.execute(f"SELECT first_name, patronymic, last_name FROM people WHERE id in {n_specs[i]['courses'][j]['helpers']}")
                    else:
                        cursor.execute(f"SELECT first_name, patronymic, last_name FROM people WHERE id={n_specs[i]['courses'][j]['helpers'][0]}")
                    try:
                        dic = generateDict(cursor)
                        n_specs[i]['courses'][j]['helpers'] = dic if type(dic) == list else [dic]
                    except exc.NotFound:
                        return make_response('Users not found', 404)
        return make_response(jsonify(n_specs), 200)