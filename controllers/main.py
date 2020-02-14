from odoo import http
from odoo.http import request
from odoo.addons.web.controllers.main import Home


class Home(Home):
    def _login_redirect(self, uid, redirect=None):
        if request.session.uid and request.env['res.users'].sudo().browse(request.session.uid).has_group('lts.group_transporter'):
            return '/web/'
        if request.session.uid and request.env['res.users'].sudo().browse(request.session.uid).has_group('base.group_user'):
            return '/web/'
        if request.session.uid and request.env['res.users'].sudo().browse(request.session.uid).has_group('base.group_portal'):
            return '/home'
        return super(Lts, self)._login_redirect(uid, redirect=redirect)


class Lts(http.Controller):
    @http.route('/home', auth='public', type="http", csrf=False)
    def index(self, **kw):
        return http.request.render('lts.lts_index')

    @http.route('/TransporterRegister/', auth="public", type="http", csrf=False)
    def Transporter_Register(self, **kw):
        currency = http.request.env['res.currency'].sudo().search([])
        return http.request.render('lts.transporteregister', {'currency': currency})

    @http.route('/TransporterRegister/form', auth="public", type="http", csrf=False)
    def Transporter_register_form(self, **post):
        groups_id_name = [(6, 0, [request.env.ref('lts.group_transporter').id])]
        currency_name = post.get('currency')
        currency = request.env['res.currency'].sudo().search([('name', '=', currency_name)], limit=1)
        partner = request.env['res.partner'].sudo().create({
            'name': post.get('name'),
            'email': post.get('email')
        })
        company = request.env['res.company'].sudo().create({
            'name': post.get('companyname'),

            'partner_id': partner.id,
            'currency_id': currency.id,
        })
        request.env['res.users'].sudo().create({
            'partner_id': partner.id,
            'login': post.get('name'),
            'password': post.get('password'),
            'company_id': company.id,
            'company_ids': [(4, company.id)],
            'groups_id': groups_id_name,
        })
        return http.local_redirect('/web/login?redirect=/home')

    @http.route('/customerregister/', auth="public", type="http", csrf=False)
    def Customer_Register(self, **kw):
        currency = http.request.env['res.currency'].sudo().search([])
        return http.request.render('lts.customerregister', {'currency': currency})

    @http.route('/customerregister/form', auth="public", type="http", csrf=False)
    def CustomerRegisterForm(self, **post):

            groups_id_name = [(6, 0, [request.env.ref('base.group_portal').id])]
            currency_name = post.get('Currency')
            request.env['res.currency'].sudo().search([('name', '=', currency_name)], limit=1)
            partner = request.env['res.partner'].sudo().create({
              'name': post.get('name'),
              'email': post.get('email'),
            })
            request.env['res.users'].sudo().create({
              'partner_id': partner.id,
              'login': post.get('name'),
              'password': post.get('password'),
              'groups_id': groups_id_name,
            })
            return http.local_redirect('/web/login?redirect=/home')

    @http.route(['/transporters/'], auth='public', csrf=False)
    def TransporterForm(self, **kw):
        t = http.request.env['transporter.transporter'].sudo().search([])
        return http.request.render('lts.lts_transporters', {
            't': t,
            })

    @http.route(['/vehicles/<int:vid>'], auth='public', csrf=False)
    def VehiclesForm(self, vid=0, **kw):
        v = http.request.env['vehicles.vehicles'].sudo().search([('company_id', '=', vid), ('available', '=', 'available')])
        return http.request.render('lts.lts_vehicles', {'v': v})

    @http.route(['/drivers/<int:did>'], auth='public', csrf=False)
    def DriversForm(self, did=0, **kw):
        d = http.request.env['drivers.drivers'].sudo().search([('company_id', '=', did), ('available', '=', 'available')])
        return http.request.render('lts.lts_drivers', {'d': d})

    @http.route(['/inquirey/<int:tid>'], auth='public', csrf=False)
    def Inquirey(self, tid=0, **kw):
        t = http.request.env['transporter.transporter'].sudo().search([('id', '=', tid)])
        v = http.request.env['vehicles.vehicles'].sudo().search([('company_id', '=', t.company_id.id)])
        d = http.request.env['drivers.drivers'].sudo().search([('company_id', '=', t.company_id.id)])
        return http.request.render('lts.lts_createinquirey', {
                'v': v, 'tid': tid, 'd': d, })

    @http.route(['/yourinquirey/'], auth='public', csrf=False)
    def YourInquirey(self, **kw):
        i = http.request.env['inquirey.inquirey.demo'].sudo().search([('create_uid', '=', request.session.uid)])
        return http.request.render('lts.lts_displayinquires', {
            'i': i,
            })

    @http.route('/createinquirey/<int:tid>', auth='public', csrf=False, method='post')
    def CreateInquirey(self, tid=0, **post):
        if post:
            tp = http.request.env['transporter.transporter'].sudo().browse([(tid)])
            http.request.env['inquirey.inquirey.demo'].sudo().create({
                    'source_add': post.get('source_add'),
                    'desti_add': post.get('desti_add'),
                    'distance': int(post.get('distance')),
                    'duration': float(post.get('duration')),
                    'weight': int(post.get('weight')),
                    'driver_id': post.get('dname'),
                    'vehicle_type': int(post.get('vehicle_type')),
                    'date': post.get('date'),
                    'company_id': tp.company_id.id,
                    })
        return http.local_redirect('/yourinquirey/')
