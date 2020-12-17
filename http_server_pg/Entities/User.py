class User:
    def __init__(self, id, firstName, lastName, age, address):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.address = address

    @property
    def id(self):
        ''' I'm the 'id' property. '''
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @id.deleter
    def id(self):
        del self._id
#
    @property
    def firstName(self):
        '''I'm the 'firstName' property.'''
        return self._firstName

    @firstName.setter
    def firstName(self, value):
        self._firstName = value

    @firstName.deleter
    def firstName(self):
        del self._firstName
#
    @property
    def lastName(self):
        '''I'm the 'lastName' property.'''
        return self._lastName

    @lastName.setter
    def lastName(self, value):
        self._lastName = value

    @lastName.deleter
    def lastName(self):
        del self._lastName
#
    @property
    def age(self):
        '''I'm the 'age' property.'''
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

    @age.deleter
    def age(self):
        del self._age
#
    @property
    def address(self):
        '''I'm the 'address' property.'''
        return self._address

    @address.setter
    def address(self, value):
        self._address = value

    @address.deleter
    def address(self):
        del self._address
