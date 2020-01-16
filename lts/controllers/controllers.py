from odoo import http


class Lts(http.Controller):
    @http.route('/lts/lts/', auth='public')
    def index(self, **kw):
        return "Hello, world"


    @http.route('/lts/lts/agent/', auth='public', website=True,csrf=False)
    def agentdata(self, **kw):
    	agents = http.request.env['agent.agent'].search([])
    	return http.request.render('lts.agentdata', {
    			'agents' : agents,
    			})
    


    @http.route(['/lts/lts/createform/', '/lts/lts/editform/<model("agent.agent"):editid>'],auth='public',website=True,csrf=False)
    def createform(self, editid=None):
        agent = None
        if editid:
            agent = http.request.env['agent.agent'].browse([editid.id])
        return http.request.render('lts.createdata',{
            'agent' : agent,
            })

    @http.route(['/lts/lts/data/', '/lts/lts/data/<int:editid>'],auth='public',website=True,csrf=False, method='post')
    def create(self, editid=None, **post):
        if post:
            if editid:
                http.request.env['agent.agent'].browse([editid]).write({
                    'name' : post.get('name'),
                    'email': post.get('email'),
                    'c_number' : post.get('c_number'),
                    'gender': post.get('gender'),
                    'address' : post.get('address'),
                    'city': post.get('city'),
                    'state' : post.get('state'),                
                    })
            else:
                http.request.env['agent.agent'].create({
                    'name' : post.get('name'),
                    'email': post.get('email'),
                    'c_number' : post.get('c_number'),
                    'gender': post.get('gender'),
                    'address' : post.get('address'),
                    'city': post.get('city'),
                    'state' : post.get('state'),                
                    })
        return http.request.redirect('/lts/lts/agent/')


    @http.route('/lts/lts/delete/<model("agent.agent"):deleteid>',auth='public',website=True,csrf=False)
    def delete(self, deleteid=None):
        if deleteid:
            deleteid.unlink()
        #c = http.request.env['agent.agent'].create([])
        return http.request.redirect('/lts/lts/agent/')


    #     class Academy(http.Controller):
    # @http.route('/academy/academy/', auth='public')
    # def index(self, **kw):
    #     Teachers = http.request.env['academy.teachers']
    #     return http.request.render('academy.index', {
    #         'teachers': Teachers.search([])s
    #     })

#     @http.route('/lts/lts/objects/<model("lts.lts"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('lts.object', {
#             'object': obj
#         })
