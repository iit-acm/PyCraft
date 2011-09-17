from persistent.mapping import PersistentMapping

#base dictionary, use for global-ish
#functions
class PyCraft(PersistentMapping):
  __name__ = None
  __parent__ = None

#set up database on first run and
#return our application root
def appmaker(zodb_root):
  if not 'app_root' in zodb_root:
    app_root = PyCraft()
    zodb_root['app_root'] = app_root
    import transaction
    transaction.commit()
  return zodb_root['app_root']
