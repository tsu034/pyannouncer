class Announcer:
    def __init__(self):
        self.subscribers = Subscribers()

    # use subscribe(when,do) or subscribe(when,send,to)
    def subscribe(self, when=None, do=None, send=None, to=None):
        action = do if do else getattr(to,send)
        self.subscribers.regist(when,action)

    def announce(self, announcement):
        self.subscribers.announce(announcement)

class Subscribers:
    def __init__(self):
        self.arr = []

    def regist(self, announcement_type, action):
        self.arr.append([announcement_type, action])

    def announce(self, announcement):
        for ann_cls, action in self.arr:
            if announcement.is_superclass_instance_of(ann_cls):
                action(announcement)