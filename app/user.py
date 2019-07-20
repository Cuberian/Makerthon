from app import app
from flask import jsonify, request, make_response
from services.addons import generateDict, decodeJwt
import psycopg2
import services.exceptions as  exc
from datetime import datetime as dt

@app.before_request
def before_request():
    conn = psycopg2.connect(dbname = 'obdb', user = 'postgres', password = 'qazwsxedc', host = '172.20.10.3')
    global cursor
    cursor = conn.cursor()

@app.teardown_request
def teardown_request(exception):
    cursor.close()
    print('closed')

@app.route('/user/<id>', methods = ['GET', 'POST', 'PUT', 'DELETE'])
def userIds(id):
    if request.method == 'GET':
        cursor.execute(f"SELECT * FROM people LEFT JOIN people_access ON people.id=people_access.id_people WHERE people.id={id}")
        try:
            data = generateDict(cursor)
        except exc.NotFound:
            return make_response('User not found', 404)
        return make_response(jsonify(data), 200)

@app.route('/user/courses', methods = ['GET', 'POST'])
def userCourses():
    if request.method == 'GET':
        info = decodeJwt(request.args.get('token'))
        id = int(request.args.get('id'))
        if info['access_level'] > 1:
            return make_response("Access denied", 403)
        if id != info['id']:
            cursor.execute(f"SELECT people_rel.id_сhild FROM people_rel WHERE id_parent={info['id']}")
            ids = list(i[0] for i in cursor.fetchall())
            if id not in ids:
                return make_response("Access denied", 403)
        cursor.execute(f"SELECT people_groups.id_group FROM people_groups WHERE id_people={id}")
        groups = tuple(i[0] for i in cursor.fetchall())
        if len(groups) != 1:
            cursor.execute(f"SELECT * FROM groups WHERE id IN {groups}")
        else:
            cursor.execute(f"SELECT * FROM groups WHERE id={groups[0]}")
        try:
            groups_info = generateDict(cursor)
        except exc.NotFound:
            return make_response('Groups not found', 404)
        if len(groups) != 1:
            cursor.execute(f"SELECT * FROM quests WHERE id_group IN {groups}")
        else:
            cursor.execute(f"SELECT * FROM quests WHERE id_group={groups[0]}")
        lessons = generateDict(cursor)
        for i in range(len(lessons)):
            lessons[i]['date'] = dt.strftime( lessons[i]['date'], "%d/%m/%Y")
        data = {'groups' : groups_info if type(groups_info) != dict else [groups_info], 'lessons' : lessons if type(lessons) != dict else [lessons]}
        return make_response(jsonify(data),200)