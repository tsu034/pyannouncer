from unittest import TestCase

from announcer import Announcer
from announcement import Announcement

# A
# + B1
#   + C
# + B2
class A(Announcement): 
    def __init__(self):
        super().__init__()
        self.holder = 0

class B1(A): pass
class B2(A): pass

class AnnouncerTestCase(TestCase):
    def setUp(self):
        self.announcer = Announcer()

    def test_subscribe_do_with_announcement(self):
        a = A()
        a.holder = 10
        self.holder = 0
        
        def func(announcement):
            self.holder = announcement.holder
  
        self.announcer.subscribe(
            when=A,
            do=func
        )

        self.assertEqual(self.holder,0)
        self.announcer.announce(a)
        self.assertEqual(self.holder,10)

    def test_subscribe_send_to(self):
        a = A()
        a.holder = 10
        self.holder = 0

        self.announcer.subscribe(
            when=A,
            send='setHolder',
            to=self
        )

        self.assertEqual(self.holder,0)
        self.announcer.announce(a)
        self.assertEqual(self.holder,10)

    def setHolder(self, announcement):
        self.holder = announcement.holder

    def test_subscribe_send_to_with_multi_subscriber(self):
        a = A()
        a.holder = 5
        self.holder = 0

        for i in range(2):
            self.announcer.subscribe(
                when=A,
                send='addHolder',
                to=self
            )

        self.assertEqual(self.holder,0)
        self.announcer.announce(a)
        self.assertEqual(self.holder,10)


    def addHolder(self, announcement):
        self.holder += announcement.holder

    def test_subscribe_send_to_with_inherited_announcement(self):
        a = A()
        b1 = B1()
        b2 = B2()

        def makeAppendHolderOf(s):
            def appendHolder(ann):
                self.holder.add(s)
            return appendHolder

        self.announcer.subscribe(
            when=A, do=makeAppendHolderOf('A')
        )

        self.announcer.subscribe(
            when=B1, do=makeAppendHolderOf('B1')
        )

        self.announcer.subscribe(
            when=B2, do=makeAppendHolderOf('B2')
        )

        self.holder = set()
        self.announcer.announce(b1)
        self.assertTrue({'B1'} == self.holder)

        self.holder = set()
        self.announcer.announce(b2)
        self.assertTrue({'B2'} == self.holder)

        self.holder = set()
        self.announcer.announce(a)
        self.assertTrue({'A', 'B1', 'B2'} == self.holder)

    def appendHolder(self,announcement):
        self.holder.add(announcement.value())

        
        




    
    
