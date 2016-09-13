import openerp.http as http
from openerp.http import request

class ProcedureRicalcoloController(http.Controller):

    @http.route('/cogito/procedurericalcolo', type="json", auth="public")
    def ricalcolo(self):
        request.env.cr.execute("select fix_parent('account_account', 'parent_id', 'name')")        
        query_out = request.env.cr.fetchone()[0]        

        return {"query_out": query_out}