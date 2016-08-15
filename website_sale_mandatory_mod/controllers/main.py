# -*- coding: utf-8 -*-
import werkzeug
from openerp import SUPERUSER_ID
from openerp import http
from openerp.http import request
from openerp.addons import website_sale
import openerp.addons.website_sale.controllers.main as main


class website_sale_mandatory_mod(main.website_sale):
    
    @http.route(['/shop/confirm_order'], type='http', auth="public", website=True)
    def confirm_order(self, **post):
        self.mandatory_billing_fields  = ["name", "email", "street2", "city", "country_id", "zip"]
        self.optional_billing_fields   = ["street", "state_id", "vat"]
        self.mandatory_shipping_fields = ["name", "street", "city", "country_id", "zip"]
        self.optional_shipping_fields  = ["state_id"]
        return super(website_sale_mandatory_mod,self).confirm_order(**post)



# vim:expandtab:tabstop=4:softtabstop=4:shiftwidth=4:

