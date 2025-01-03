# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import Response
import json


class UserController(http.Controller):
    @http.route('/api/users', auth='public', method=['GET'], csrf=False, )
    def get_users(self, **kw):
        try:
            users = http.request.env['open_the_door.user'].sudo().search_read([], ['id', 'name', 'gender'])
            res = json.dumps(users, ensure_ascii=False).encode('utf8')
            return Response(res, content_type='application/json; charset=UTF-8', status=200)
        except Exception as e:
            return Response(json.dumps({'error': str(e)}), content_type='application/json; charset=UTF-8', status=505)
