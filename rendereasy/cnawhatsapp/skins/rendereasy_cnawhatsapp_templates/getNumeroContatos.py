## Script (Python) "getPastasRaiz"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##
path={ "query": "/cna/grupos", 'depth': 1 }
grupos = context.portal_catalog.searchResults(Type=['Grupo'], path=path)

cont = 0
for grupo in grupos:
    cont = cont + int(grupo.getQuantidade)


return "{:0,d}".format(cont).replace(',','.')
