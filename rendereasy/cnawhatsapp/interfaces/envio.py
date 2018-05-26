from zope.interface import Interface
# -*- Additional Imports Here -*-
from zope import schema

from rendereasy.cnawhatsapp import cnawhatsappMessageFactory as _



class IEnvio(Interface):
    """Description of the Example Type"""

    # -*- schema definition goes here -*-
    inicio = schema.Date(
        title=_(u"Inicio do envio"),
        required=True,
        description=_(u"Field description"),
    )
#
    mensagem = schema.TextLine(
        title=_(u"Mensagem"),
        required=True,
        description=_(u"Field description"),
    )
#
    grupos = schema.List(
        title=_(u"Grupos"),
        required=True,
        description=_(u"Field description"),
    )
#
    icone = schema.Bytes(
        title=_(u"Icone"),
        required=False,
        description=_(u"Field description"),
    )
#
    arquivo = schema.Bytes(
        title=_(u"Arquivo"),
        required=False,
        description=_(u"Field description"),
    )
#
