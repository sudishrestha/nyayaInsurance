# -*- coding: utf-8 -*-
from odoo import models, fields
class InsuranceTask(models.Model):
	_name = 'insurance.task'
	_description = 'Insurance Task'
	name = fields.Char('Name', required=True)
	age  = fields.Integer('Age', required=True)
	address = fields.Char('Address', required=True)
	claim_amount =  fields.Float('Claimed amount',digits=(2,1))
	date_of_claim = fields.Date('Claimed date', required= True)
	is_approved = fields.Boolean('Is approved?')
	remarks= fields.Text('Remarks')
	claim_value = [('health', 'Health Insurance'), ('death','Death Insurance')]
	claim_type= fields.Selection(claim_value,'Claim Type', required=True,default='health')
