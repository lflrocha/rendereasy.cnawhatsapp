# -*- coding: utf-8 -*-
"""Definition of the Grupo content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-
from rendereasy.cnawhatsapp import cnawhatsappMessageFactory as _

from rendereasy.cnawhatsapp.interfaces import IGrupo
from rendereasy.cnawhatsapp.config import PROJECTNAME

GrupoSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

    atapi.ComputedField(
        'quantidade',
        storage=atapi.AnnotationStorage(),
        widget=atapi.ComputedWidget(
            label=_(u"Quantidade"),
            description=_(u"Quantidade de telefones cadastrados."),
        ),
        expression="context.numTelefones()"
    ),


    atapi.LinesField(
        'telefones',
        storage=atapi.AnnotationStorage(),
        widget=atapi.LinesWidget(
            label=_(u"Telefones"),
            description=_(u"Um por linha, no formato 6199999999."),
        ),
    ),



))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

GrupoSchema['title'].widget.label = _(u"Nome do grupo")
GrupoSchema['title'].storage = atapi.AnnotationStorage()
GrupoSchema['description'].storage = atapi.AnnotationStorage()
GrupoSchema['location'].widget.visible = {"edit": "invisible", "view": "invisible"}
GrupoSchema['language'].widget.visible = {"edit": "invisible", "view": "invisible"}
GrupoSchema['effectiveDate'].widget.visible = {"edit": "invisible", "view": "invisible"}
GrupoSchema['expirationDate'].widget.visible = {"edit": "invisible", "view": "invisible"}
GrupoSchema['creators'].widget.visible = {"edit": "invisible", "view": "invisible"}
GrupoSchema['contributors'].widget.visible = {"edit": "invisible", "view": "invisible"}
GrupoSchema['rights'].widget.visible = {"edit": "invisible", "view": "invisible"}
GrupoSchema['allowDiscussion'].widget.visible = {"edit": "invisible", "view": "invisible"}
GrupoSchema['excludeFromNav'].widget.visible = {"edit": "invisible", "view": "invisible"}
GrupoSchema['subject'].widget.visible = {"edit": "invisible", "view": "invisible"}
GrupoSchema['relatedItems'].widget.visible = {"edit": "invisible", "view": "invisible"}


schemata.finalizeATCTSchema(GrupoSchema, moveDiscussion=False)


class Grupo(base.ATCTContent):
    """ """
    implements(IGrupo)

    meta_type = "Grupo"
    schema = GrupoSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    telefones = atapi.ATFieldProperty('telefones')


    def numTelefones(self):
        return len(self.getTelefones())

atapi.registerType(Grupo, PROJECTNAME)
