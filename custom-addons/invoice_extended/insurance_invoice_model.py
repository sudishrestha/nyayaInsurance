# -*- coding: utf-8 -*-
from odoo import models,osv, fields, api, _
from datetime import datetime, timedelta
from odoo.exceptions import ValidationError
class InsuranceInvoiceTask(models.Model):
	_inherit = 'account.move'
	# create insurance
	
	def create_insurance(self):
		recoo = []
		inv_obj = self.env['insurance.task']
		for rec in self:
			if rec.state != 'posted':
				raise ValidationError("You cannnot claim for Insurance before posting invoice."  )
			elif rec.amount_total <= 0:
				  raise ValidationError("Please fill all the fields before claiming for Insurance." )
			elif rec.partner_id.name == False:
				raise ValidationError("Please fill all the fields before claiming for Insurance.")
			elif rec.invoice_date == False:
				raise ValidationError("Please fill all the fields before claiming for Insurance")	
			else:
				inc = inv_obj.create({
				'name': rec.partner_id.name,
				'age': '0',
				'address': rec.partner_id.city,
				'claim_amount':rec.amount_total,
				'date_of_claim':rec.invoice_date,
				'is_approved':False,
				'remarks':rec.name,
				'claim_type':'health',
				
				})
		return inc

