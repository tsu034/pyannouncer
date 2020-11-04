class Announcement:
   def is_superclass_instance_of(self,ann_cls):
       return issubclass(ann_cls, type(self))
    