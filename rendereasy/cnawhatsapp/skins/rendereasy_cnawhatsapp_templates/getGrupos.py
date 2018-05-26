## Script (Python) "getTVBrNCP"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##

folder_path = '/'.join(context.getPhysicalPath())

solicitacoes = context.portal_catalog.searchResults(meta_type=['Grupo'], sort_on="modified", sort_order="reverse", path={'query': folder_path})

return solicitacoes
