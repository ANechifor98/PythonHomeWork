class File(object):

    FILE_PERMISSIONS = "rwx"
    
    def __init__(self, name, owner, size=0, permissions="null"):
        self.name = name
        self.owner = owner
        self.size = size
        self.permissions = permissions

    def __str__(self):
        if self.permissions == "null":
            self.permissions = "null"
        else:
            new_l = list(self.permissions)
            new_l = sorted(new_l)
            self.permissions = "".join(new_l)
        output = "File: {}\nOwner: {}\nPermissions: {}\nSize: {} bytes".format(self.name, self.owner, self.permissions,self.size)
        return output

    def has_access(self, person, op):
        if person == self.owner:
            return True
        else:
            if op in self.permissions:
                return True
            else:
                return False

    def enable_permission(self, person, op):
        if person == self.owner:
            if self.permissions == "null":
                self.permissions = ""
                self.permissions += op
            elif op in self.permissions:
                self.permissions = self.permissions
            else:
                self.permissions += op
        else:
            return False

    def disable_permission(self, person, op):
        if self.owner == person:
            if op in self.permissions:
                self.permissions = list(self.permissions)
                self.permissions.remove(op)
                self.permissions = "".join(self.permissions)
            else:
                self.permissions = self.permissions
        else:
            return False

def main():

    # Create some files
    f1 = File('poem.txt', 'joe')
    f2 = File('readme.txt', 'max', 100, 'wr')
    f3 = File('gedit', 'fred', 200, 'wxr')

    # Joe enables permissions
    print('Joe enables permissions...')
    f1.enable_permission('joe', 'r')
    f1.enable_permission('joe', 'x')
    print(f1)
    
    # Joe enables permissions
    print('Joe enables permissions...')
    f1.enable_permission('joe', 'r')
    print(f1)

    # Joe disables permissions
    print('Joe disables permissions...')
    f1.disable_permission('joe', 'x')
    print(f1)
    
    # Joe disables permissions
    print('Joe disables permissions...')
    f1.disable_permission('joe', 'x')
    print(f1)

    # Max enables permissions
    print('Max enables permissions...')
    print(f1.enable_permission('max', 'x'))
    print(f1)

    # Max disables permissions
    print('Max disbles permissions...')
    print(f1.disable_permission('max', 'r'))
    print(f1)

if __name__ == '__main__':
    main()

