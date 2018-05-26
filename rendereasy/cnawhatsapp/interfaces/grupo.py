from zope.interface import Interface
# -*- Additional Imports Here -*-
from zope import schema

from rendereasy.cnawhatsapp import cnawhatsappMessageFactory as _



class IGrupo(Interface):
    """Description of the Example Type"""

    # -*- schema definition goes here -*-
    telefones = schema.List(
        title=_(u"Telefones"),
        required=False,
        description=_(u"Field description"),
    )
#
