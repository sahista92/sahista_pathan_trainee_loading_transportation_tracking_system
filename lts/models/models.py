from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date 


class agent(models.Model):
    _name = 'agent.agent'
    _description = 'Agent.Agent'

    name = fields.Char(required=True)
    email = fields.Char(required=True)
    c_number = fields.Integer()
    gender = fields.Selection([('male','Male'),('female','Female'),('other','Other')])
    address = fields.Text()
    city = fields.Char()
    state= fields.Selection([('draft','draft'),('done','done'),('cancel','cancel')], default='draft')

    
    def button_done(self):
        self.write({'state': 'done'})
        return True
    
    def button_reset(self):
        self.write({'state': 'draft'})
        return True
    
    def button_cancel(self):
        self.write({'state': 'cancel'})
        return True
                





class inquirey(models.Model):
    _name = 'inquirey.inquirey.demo'
    _description = 'inquirey.inquirey'
    _rec_name = 'source_add'
    source_add = fields.Char(required=True)
    desti_add = fields.Char(required=True)
    KM = fields.Integer()
    duration =fields.Float()
    vehicle_type = fields.Selection(store='True',selection=[('2','2 wheeler'),('3','3 wheeler'),('4','4 wheeler')])
    vehicle_capacity = fields.Selection(store='True',selection=[('250','250 kg'),('550','550 kg'),('1000','1000 kg')])
    vehicle_speed = fields.Selection(store='True',selection=[('70','70 kmph'),('50','50 kmph '),('60','60 kmph')])
    date_start=fields.Date()
    date_stop=fields.Date()


    @api.onchange('vehicle_type','vehicle_capacity')
    def _value_pc(self):
        	if self.vehicle_type == '2':
        		self.vehicle_capacity = '250'
        		self.vehicle_speed = '70'

        	elif self.vehicle_type == '3':
        		self.vehicle_capacity = '550'
        		self.vehicle_speed = '50'

        	elif self.vehicle_type == '4':
        		self.vehicle_capacity = '1000'
        		self.vehicle_speed = '60'
	


    @api.model
    def create(self, vals):
        print(vals['source_add'])
        return super(inquirey, self).create(vals)

    def write(self, vals):
        print(vals['KM'])
        return super(inquirey, self).write(vals)


    @api.constrains('source_add', 'desti_add')
    def _check_add(self):
    	for record in self:
    		if record.source_add == record.desti_add:
    			raise ValidationError("source_add name and destination address must be different")

class order(models.Model):
    _name = 'order.order'
    _inherit = 'inquirey.inquirey.demo'
    _description = 'order.order'

    order_number = fields.Integer(required=True)

class  transporter(models.Model):
    _name = 'transporter.transporter'
    _inherit = 'agent.agent'
    _description = 'transporter.transporter'

    
class Wizard(models.TransientModel):
    _name = 'inquirey.wizard'
    _description = "Wizard: Quick inquirey of vehicles"

    order_number = fields.Many2one('order.order',required=True)
