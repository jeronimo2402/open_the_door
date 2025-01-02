# -*- coding: utf-8 -*-
import datetime

from odoo import models, fields, api


class User(models.Model):
     _name = 'open_the_door.user'
     _description = 'User'

     name = fields.Char(string='Nombre')
     date = fields.Datetime(string='Fecha')
     gender = fields.Selection([('M', 'Masculino'), ('F', 'Femenino')], string='Genero', requiered=True)
     image = fields.Binary(string='Imagen')



     def f_create(self):
          user={
               'name':'Juan David Zuluaga',
               'date': str(datetime.date(2024,10,12)),
               'gender':'M',
               'done':False
          }
          print(user)
          self.env['open_the_door.user'].create(user)

     def f_search_update(self):
          user=self.env['open_the_door.user'].search([('name','=','Juan David Zuluaga')])
          print('search()',user, user.name)

          user_b = self.env['open_the_door.user'].browse([4])
          print('browse()',user_b, user_b.name)

          user.write({
               'name':'Juan Felipe Camargo'
          })

     def f_delete(self):
          user = self.env['open_the_door.user'].browse([4])
          user.unlink()

# class VisitReport(models.AbstractModel):
#
#      _name = 'report.open_the_door.report_user_card'
#
#      @api.model
#      def _get_report_values(self, docids, data=None):
#           report_obj = self.env['ir.actions.report']
#           report = report_obj._get_report_from_name('open_the_door.report_user_card')
#           return {
#                'doc_ids': docids,
#                'doc_model': self.env['open_the_door.user'],
#                'docs': self.env['open_the_door.user'].browse(docids),
#           }