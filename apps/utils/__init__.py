import re


class django_choices(tuple):
    '''
    Creates a choices data type like what django needs for models.
    Based on http://www.djangosnippets.org/snippets/667/
    '''

    def __init__(self, *args, **kwargs):
        # create an attribute for each key so it can be referenced as  django_choices_object.my_choice
        for t in self:
            key = t[1].lower().replace(' ', '_').replace('.', '_').replace('-', '_')   # make lowercase and replace periods and spaces to underscores when creating the attribute
            setattr(self, key, t[0])

    def __new__(self, *args, **kwargs):
        self.choices = []
        if kwargs:
            for val in kwargs.values():
                for key in kwargs.keys():
                    if kwargs[key] == val:
                        self.choices.append((val, key.replace('_', ' ')))
            self.choices.sort()
        return tuple.__new__(self, self.choices or args)

    def to_dict(self, to_lower=True):
        '''
        Automatically converts the choices to a dictionary. Useful for type lookups.
        '''
        d = {}
        if to_lower == True:
            for choice in self:
                #d[choice[1].lower().replace(' ','_')] = choice[0]
                d[choice[1].lower()] = choice[0]
        else:
            for choice in self:
                #d[choice[1].replace(' ','_')] = choice[0]
                d[choice[1]] = choice[0]
        return d

    def get_key(self, value):
        '''return the value of dictionary dic given the key from http://www.daniweb.com/code/snippet806.html'''
        try:
            return [k for k, v in self.to_dict().iteritems() if v == value][0]
        except IndexError:
            return None

    def get_value(self, key):  # expects a key and returns the value
        #print self.to_dict()
        try:
            if type(key) == type('str'):
                ret = self.to_dict()[key.replace('-', '_')]
            else:
                ret = self.to_dict()[key]
        except KeyError:
                ret = None
        return ret

    def keys(self):  # returns a list of all keys
        return self.to_dict().values()

    def values(self):  # returns a list of all values
        return self.to_dict().keys()

