from persistent import Persistent, PersistentList
from threading import RLock
from subprocess import Popen, PIPE

"""

"""

class Server(Persistent):
    def __init__(self, name, path):
        self.__name__ = name
        self.__acl__ = None
        self.last_save = None
        self.last_bkup = None
        self.path = None
        self.cmd_args = None
        self.userlist = PersistentList()
        #connection to the minecraft shell
        #self._v_shell = None
        #lock to allow our multithreaded app
        #to block on multiple requests
        #self.lock = RLock()
        self.make_server(path)

#VOLITILE ATTRIBUTES
    def lock(self):
        if hasattr(self, '_v_lock'):
            return self._v_lock
        lock = RLock(False)
        self._v_lock=lock
        return lock

    def proc(self):
        if hasattr(self, '_v_proc'):
            return self._v_proc

    def connected_userlist(self):
        if hasattr(self, '_v_conn_userlist'):
            return self._v_conn_userlist

#END VOLITILE ATTRIBUTES

#LOCK METHODS
    def acquire_lock(self, t):
        if not t:
            return self.lock().acquire()
        #convert t to a time
        now = time()
        end = now + t
        while(not self.lock().acquire() and now<end):
            sleep(.3)
            now = time()
    return self.lock().acquire()

  def release_lock(self):
    self.lock().release()
#END LOCK METHODS

    def make_server(self, path):
        if self.acquire_lock():
            try:
                self.path = path
            finally:
                self.release_lock()

    def start(self):
        if self.acquire_lock():
            try:
                if not self.proc() and not self.world_locked():
                    self._v_proc = Popen(self.cmd_args, stdin=PIPE, stdout=PIPE, stderr=PIPE, cwd=self.path)
                    #wait for server to start
                    #start a timer tick function that consumes PIPEs (very bad if not done)
                else:
                    pass #return error
            finally:
                self.release_lock()

    def stop(self):
        if self.acquire_lock():
            try:
                if self.proc():
        
                proc.communicate('say SERVER SHUTTING DOWN')
                self.save()
                #check for save complete
                proc.communicate('stop')
        self.release_lock()

    def force_stop(self):
        #force release lock/stop server
        if (proc = self.proc()):
            proc.kill

    def save(self):
        if self.acquire_lock():
        try:
            if (proc = self.proc()):
                proc.communicate('save-on')
                proc.communicate('save-all')
                #wait for save to complete
                proc.communicate('save-off')
        finally:
            self.release_lock()

    def make_map(self):
        if self.acquire_lock():
            try:
                pass
            finally:
                self.release_lock()
    
    def backup(self):
        if self.lock().acquire():
            try:
                pass
            finally:
                self.lock().release()

    def tick(self):
        if self.lock().acquire():
            try:
                #consume process pipes, check for errors
                #use pipe data to fill userlist and log actions
                pass
            finally:
                self.lock().release()
