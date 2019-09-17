class File(object):

   FILE_PERMISSIONS = "rwx"

   def __init__(self, name, owner, size=0, permissions=""):
      self.name = name
      self.owner = owner
      self.size = size
      self.permissions = permissions

   def has_access(self, person, op):
      if self.owner == person:
         return True
      else:
         if op in self.permissions:
            return True
         else:
            return False

   def enable_permission(self, person, op):
      if self.owner == person:
         if op not in self.permissions:
            self.permissions = self.permissions + op
            self.permissions = "".join(sorted(list(self.permissions)))
            return True
         else:
            return True
      else:
         return False

   def disable_permission(self, person, op):
      if self.owner == person:
         if op in self.permissions:
            self.permissions = list(self.permissions)
            self.permissions.remove(op)
            self.permissions = "".join(self.permissions)
            self.permissions = "".join(sorted(list(self.permissions)))
            return True
         else:
            return True
      else:
         return False

   def __str__(self):
      if self.permissions == "" or self.permissions == "null":
         self.permissions = "null"
         return "File: {}\nOwner: {}\nPermissions: {}\nSize: {} bytes".format(self.name, self.owner, self.permissions, self.size)
      else:
         return "File: {}\nOwner: {}\nPermissions: {}\nSize: {} bytes".format(self.name, self.owner, "".join(sorted(list(self.permissions))), self.size)

class Folder(object):

   def __init__(self, folder=None):
      if folder == None:
         folder = []
      self.folder = folder

   def add_file(self, f):
      self.folder.append(f)
      return self

   def __str__(self):
      slist = []
      total = 0
      slist.append("Folder contents")
      slist.append("=" * len("Folder contents"))
      for f in self.folder:
         total = total + f.size
         slist.append(f.__str__())
      folder_size = "Folder size: {} bytes".format(total)
      slist.append(folder_size)
      return "\n".join(slist)

def main():

    # Create some files
    f1 = File('poem.txt', 'joe')
    f2 = File('gedit', 'fred', 200, 'wxr')
    f3 = File('readme.txt', 'max', 100, 'wr')

    # Create an empty folder
    folder = Folder()

    # Add files to the folder
    folder.add_file(f1)
    folder.add_file(f2)
    folder.add_file(f3)

    # Display folder contents
    print(folder)

if __name__ == '__main__':
    main()



