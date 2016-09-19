import openerp.http as http
from openerp.http import request

class ProcedureRicalcoloController(http.Controller):

    @http.route('/cogito_procedure/ricalcolo_piano_conti', type="json", auth="public")
    def ricalcolo_piano_conti(self):
        request.env.cr.execute("select fix_parent('account_account', 'parent_id', 'name')")        
        query_out = request.env.cr.fetchone()[0]        

        return {"query_out": query_out}
        
    @http.route('/cogito_procedure/ricalcolo_struttura_albero', type="json", auth="public")
    def ricalcolo_struttura_albero(self):
        request.env.cr.execute("select fix_parent('account_account', 'parent_id', 'name')")        
        query_out = request.env.cr.fetchone()[0]        

        return {"query_out": query_out}