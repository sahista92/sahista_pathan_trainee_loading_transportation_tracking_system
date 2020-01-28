from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date 
import re

class  transporter(models.Model):
    _name = 'transporter.transporter'
    _description = 'transporter.transporter'

    name = fields.Char(required=True,string="Name")
    email = fields.Char(required=True,string="Email")
    contactnumber = fields.Integer(string="Contact Number")
    gender = fields.Selection([('male','Male'),('female','Female'),('other','Other')])
    address = fields.Text(string="Address")
    city = fields.Char(string="City")
    pincode = fields.Integer(string="Pincode")
    state= fields.Char(string="State")

class vehicles(models.Model):
    _name = 'vehicles.vehicles'
    _description = 'vehicles.vehicle_speed'
    _rec_name = 'vehicle_type'

    vehicle_type = fields.Integer(string="Vehicle Type(Wheeler)")
    vehicle_capacity = fields.Integer(string="Vehicle_Capacity(KG)")
    vehicle_speed = fields.Integer(string="Vehicle Speed(kmph)")
    vehicle_weight = fields.Float(string="Weight(tons)")
    vehicle_length = fields.Integer(string="Vehicle Length(mtr)")
    vehicle_Engine = fields.Char(string="Vehicle Engine")
    vehicle_image = fields.Binary(string="Vehicle Image")
 

class inquirey(models.Model):
    _name = 'inquirey.inquirey.demo'
    _description = 'inquirey.inquirey'

    source_add = fields.Char(required=True,string="Source Address")
    desti_add = fields.Char(string="Destination Address" ,required=True)
    distance = fields.Integer(string="Distance(km)")
    duration =fields.Float(string="Duration (hr)",store=True,compute="find_duration")
    weight = fields.Integer(string="Weight(KG)")
    vehicle_type = fields.Many2one('vehicles.vehicles',string="Vehicle Type",required=True,store=True)
    vehicle_capacity = fields.Integer(related='vehicle_type.vehicle_capacity', store=True,string="Vehicle Capacity")
    vehicle_speed = fields.Integer(related='vehicle_type.vehicle_speed', string="Vehicle Speed(kmph)",store=True)
    from_date=fields.Date(string="From Date")
    to_date=fields.Date(string="To Date")

    @api.onchange('distance','vehicle_speed')
    def find_duration(self):
        print ('\n \n \n distance',self.distance)
        print ('\n vehicle_speed',self.vehicle_speed)
        print ('\n duration',self.duration)
        for data in self:
            if data.distance != 0 and data.vehicle_speed != 0:
                data.duration= data.distance / data.vehicle_speed


    # @api.constrains('source_add', 'desti_add')
    # def _check_add(self):
    # 	for record in self:
    # 		if record.source_add == record.desti_add:
    # 			raise ValidationError("source_add name and destination address must be different")


class drivers(models.Model):
    _name = 'drivers.drivers'
    _description = 'drivers.drivers'

    name = fields.Char(string="Name")
    contactnumber = fields.Integer(string="Contact Number")
    email = fields.Char(string="Email")
    address = fields.Text(required=True,string="Address")
    Date_Of_Birth = fields.Date(string="Date Of Date")
    Licence = fields.Selection(store=True,selection=[('yes','yes'),('no','no')], default="yes",string="Licence")
    Licence_Number = fields.Char(string="Licence Number")
    Valid_Date = fields.Date(string="Due Date")
    city = fields.Char(string="City")
    pincode = fields.Char(string="Pincode")
    state = fields.Char(string="State")
    photo = fields.Binary(attachment=True,string="Image")




# class order(models.Model):
#     _name = 'order.order'
#     _inherit = 'inquirey.inquirey.demo'
#     _description = 'order.order'

#     order_number = fields.Integer(required=True)



# class Wizard(models.TransientModel):
#     _name = 'inquirey.wizard'
#     _description = "Wizard: Quick inquirey of vehicles"

#     order_number = fields.Many2one('order.order',required=True)
# class customer(models.Model):
#     _name = 'customer.customer'
#     _description = 'customer.customer'

#     name = fields.Char(required=True)
#     email = fields.Char(required=True)
#     contactnumber = fields.Integer()
#     gender = fields.Selection([('male','Male'),('female','Female'),('other','Other')])
#     address = fields.Text()
#     city = fields.Char()
#     state= fields.Char()