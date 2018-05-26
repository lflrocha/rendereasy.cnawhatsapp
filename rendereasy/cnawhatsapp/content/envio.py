# -*- coding: utf-8 -*-
"""Definition of the Envio content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-
from rendereasy.cnawhatsapp import cnawhatsappMessageFactory as _

from rendereasy.cnawhatsapp.interfaces import IEnvio
from rendereasy.cnawhatsapp.config import PROJECTNAME

from Products.CMFCore.utils import getToolByName
from string import join
from Products.Archetypes.public import DisplayList
from DateTime.DateTime import *


EnvioSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

    atapi.DateTimeField(
        'inicio',
        storage=atapi.AnnotationStorage(),
        widget=atapi.CalendarWidget(
            label=_(u"Início do envio"),
            description=_(u"Informe a data para envio da campanha."),
        ),
        required=True,
        validators=('isValidDate'),
        default_method = 'getDefaultTime',
    ),


    atapi.TextField(
        'mensagem',
        storage=atapi.AnnotationStorage(),
        widget=atapi.TextAreaWidget(
            label=_(u"Mensagem"),
            description=_(u"Digite a mensagem a ser enviada."),
        ),
        default_content_type="text/plain",
        allowable_content_types=("text/plain"),
        default_output_type="text/plain",
        required=True,
    ),

    atapi.FileField(
        'arquivo',
        storage=atapi.AnnotationStorage(),
        widget=atapi.FileWidget(
            label=_(u"Arquivo"),
            description=_(u"Selecione o arquivo da arte a ser enviada."),
        ),
        validators=('isNonEmptyFile'),
    ),

    atapi.FileField(
        'icone',
        storage=atapi.AnnotationStorage(),
        widget=atapi.FileWidget(
            label=_(u"Icone"),
            description=_(u"Selecione a imagem do perfil."),
        ),
        validators=('isNonEmptyFile'),
    ),

    atapi.LinesField(
        'grupos',
        storage=atapi.AnnotationStorage(),
        widget=atapi.InAndOutWidget(
            label=_(u"Grupos"),
            description=_(u"Selecione um ou mais grupos."),
        ),
        vocabulary='getListaGrupos',
        required=True,
    ),

))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

EnvioSchema['title'].storage = atapi.AnnotationStorage()
EnvioSchema['description'].storage = atapi.AnnotationStorage()
EnvioSchema['description'].widget.visible = {"edit": "invisible", "view": "invisible"}
EnvioSchema['location'].widget.visible = {"edit": "invisible", "view": "invisible"}
EnvioSchema['language'].widget.visible = {"edit": "invisible", "view": "invisible"}
EnvioSchema['effectiveDate'].widget.visible = {"edit": "invisible", "view": "invisible"}
EnvioSchema['expirationDate'].widget.visible = {"edit": "invisible", "view": "invisible"}
EnvioSchema['creators'].widget.visible = {"edit": "invisible", "view": "invisible"}
EnvioSchema['contributors'].widget.visible = {"edit": "invisible", "view": "invisible"}
EnvioSchema['rights'].widget.visible = {"edit": "invisible", "view": "invisible"}
EnvioSchema['allowDiscussion'].widget.visible = {"edit": "invisible", "view": "invisible"}
EnvioSchema['excludeFromNav'].widget.visible = {"edit": "invisible", "view": "invisible"}
EnvioSchema['subject'].widget.visible = {"edit": "invisible", "view": "invisible"}
EnvioSchema['relatedItems'].widget.visible = {"edit": "invisible", "view": "invisible"}


schemata.finalizeATCTSchema(EnvioSchema, moveDiscussion=False)


class Envio(base.ATCTContent):
    """Description of the Example Type"""
    implements(IEnvio)

    meta_type = "Envio"
    schema = EnvioSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    inicio = atapi.ATFieldProperty('inicio')

    mensagem = atapi.ATFieldProperty('mensagem')
    arquivo = atapi.ATFieldProperty('arquivo')
    icone = atapi.ATFieldProperty('icone')
    grupos = atapi.ATFieldProperty('grupos')

    def getDefaultTime(self):
        return DateTime()

    def getListaGrupos(self):
        pc = getToolByName(self, 'portal_catalog')
        path = '/cna/grupos/'
        grupos = pc.searchResults(path=path,Type="Grupo",sort_on='sortable_title')
        vet = DisplayList()
        for grupo in grupos:
            nome = grupo.Title
            cod = grupo.id
            vet.add(cod, nome)
        return vet

    def getCampanha(self):
        novoProjeto =  DateTime().strftime("%Y%m%d%H%M%S") + '_' + self.meta_type
        inicio = self.getInicio()
        mensagem = self.getMensagem()
        grupos = self.getGrupos()

        arquivoFilename = self.getFilename('arquivo')
        iconeFilename = self.getFilename('icone')

        telefones = ''
        for grupo in grupos:
            telefones = telefones + ', '  + grupo


        endereco = self.absolute_url()

        aux = 'var ext_novoProjeto = "%s";\n' % novoProjeto
        aux = aux + 'var dados = [{\n'
        aux = aux + 'inicio: "%s",\n' % inicio
        aux = aux + 'mensagem: "%s",\n' % mensagem.strip()
        if arquivoFilename:
            aux = aux + 'arquivo: "%s/at_download/arquivo/%s",\n' % (endereco, arquivoFilename)
        else:
            aux = aux + 'arquivo: "",\n'
        if iconeFilename:
            aux = aux + 'icone: "%s/at_download/icone/%s",\n' % (endereco, iconeFilename)
        else:
            aux = aux + 'icone: "",\n'
        aux = aux + 'grupos: "%s",\n' % telefones.strip()
        aux = aux + '}];\n'


        return aux








atapi.registerType(Envio, PROJECTNAME)
