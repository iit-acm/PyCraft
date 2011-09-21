from persistent.mapping import PersistentMapping

#base dictionary, use for global-ish
#functions
class PyCraft(PersistentMapping):
  __name__ = None
  __parent__ = None
  base_path = './pycraft_store'

class Servers(PersistentMapping):
  __acl__ = None
  __name__ = 'servers'
  #paths
  servers_path = __parent__.base_path + '/servers'
  backups_path = None

  def __init__(self):
    #list of running servers
    self.running = list()

  def start_all(self):
    for server in self.values():
      server.lock().acquire()
      server.start()
      server.lock().release()

  def start_list(self, svr_list):
    for server in svr_list:
      server.lock().acquire()
      server.start()
      server.lock().release()

  #stop all running servers gracefully
  def stop_all(self):
    for server in self.running:
      server.lock().acquire()
      server.stop()
      server.lock().release()

  def restart_all_running(self):
    start = self.running
    self.stop_all()
    self.start_list(running)

  #force stop all servers
  def force_stop_all(self):
    for server in self.running:
      server.force_stop()

  def save_all(self):
    for server in self.running:
      server.lock().acquire()
      server.save()
      server.lock().release()

  def backup_all(self):
    for server in self.values():
      server.lock().acquire()
      server.backup()
      server.lock().release()

  #map all servers with a mapping command
  #check that a mapper is defined
  def map_all(self):
    #if not self.map_command:
      #raise MapError(MapError.cmd_undef)
    for server in self.values():
      server.lock().acquire()
      server.make_map()
      server.lock().release()

#set up database on first run and
#return our application root
def appmaker(zodb_root):
  if not 'app_root' in zodb_root:
    app_root = PyCraft()
    zodb_root['app_root'] = app_root
    import transaction
    transaction.commit()
  return zodb_root['app_root']
