
# -*- encoding: utf-8 -*-

#=====================================================
# @file  : views.py
# @brief : トップページview定義
#=====================================================

#--------- import ---------
from django import template
register = template.Library()
@register.simple_tag

#------------------------------------------------
# @brief :
#------------------------------------------------
def do_upper(parser, *token):
    nodelist = parser.parse(('endupper',))
    parser.delete_first_token()
    return UpperNode(nodelist)

#------------------------------------------------
# @brief :
#------------------------------------------------
class UpperNode(template.Node):

    def __init__(self, nodelist):
        self.nodelist = nodelist

    def render(self, context):
        output = self.nodelist.render(context)
        return output.upper()

register.tag('upper', do_upper)
