# -*- encoding: utf-8 -*-
##############################################################################
#
#    Avanzosc - Avanced Open Source Consulting
#    Copyright (C) 2011 - 2012 Avanzosc <http://www.avanzosc.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses/.
#
##############################################################################

import time

from crm import crm
from osv import fields, osv
from tools.translate import _

class crm_opportunity(osv.osv):
    _inherit = 'crm.lead'
    _columns = {
        'session_id':fields.many2one('training.session', 'Session'),
        'subscription_id': fields.many2one('training.subscription', 'Subscription'),
    }

crm_opportunity()

class crm_lead(osv.osv):
    _name='crm.lead'
    _inherit='crm.lead'
    
    #---------------------------------------------
    #--.TRIGGER.--
    #---------------------------------------------
    def _check_contact(self,cr,uid,ids):
        """ 
        Trigger que mira cuales si el campo del contacto existe.
        Sí no es así, los datos del contact los coge de la pestaña
        de oportunidades.
        """
        for con in self.browse(cr,uid,ids):
            if con.contact_id:
                return True
            else:
                if not con.contact_name and not con.contact_surname:
                    return False
                if not con.contact_name:
                    return False
                if not con.contact_surname:
                    return False
                else:
                    return True
                        
    #ON CHANGANGE                
    def onchange_contact(self, cr, uid, ids, contact_name,contact_surname):
        """
        Metodo que automaticamnete coge el nombre del contacto en la pestaña
        oportunidades partiendo de un nombre y un apellido. Lo hace
        automaticamnetepartiendo de un punto. 
        """
        value={}
        dev=""
        if  contact_surname:
            dev = dev+" "+contact_surname
        if contact_name:
            dev = dev+" "+contact_name
        value.update({
                      'contact_resum':dev
        })
        return {
                'value':value
        }          
                 
    _columns = {
                'contact_name':fields.char('Contact name',size=64),
                'contact_surname':fields.char('Contact surname',size=64),
                'contact_resum': fields.char('Contact resum',size=64),
            
    }
    _constraints=[
                 (_check_contact,'Error:contact data is missed',['contact_name','contact_surname']),
                 
    ]
    '''
    Sequencia creada, en un fichero *.xml para la creacion del campo name
    automaticamente.
    '''
    _defaults = {  
        'name': lambda self,cr,uid,context={}: self.pool.get('ir.sequence').get(cr, uid, 'crm.lead'),
        }
crm_lead()