from persistent import Persistent

class Server(Persistent):
  def __init__(self, name, path):
    self.__name__ = name
    self.last_save = None
    self.last_bkup = None
    self.lock = False
    self.make_server(path)

  def make_server(self, path):
    self.get_lock()
    self.path = path
    self.release_lock()

  def get_lock(self):
    pass

  def release_lock(self):
    pass

  def start(self):
    get_lock()
    release_lock()

  def stop(self):
    get_lock()
    release_lock()

  def force_stop(self):
    get_lock()
    release_lock()

  def make_map(self):
    get_lock()
    release_lock()
