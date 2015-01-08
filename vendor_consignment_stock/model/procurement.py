# -*- coding: utf-8 -*-
#    Author: Leonardo Pistone
#    Copyright 2014 Camptocamp SA
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
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
from openerp import models, api


class Procurement(models.Model):
    _inherit = 'procurement.order'

    @api.model
    def _run(self, procurement):
        if procurement.rule_id and procurement.rule_id.action == 'buy_vci':
            return self.make_vci_po()
        return super(Procurement, self)._run(procurement)

    @api.one
    def make_vci_po(self):
        pass
