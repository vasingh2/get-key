
class getKey(object):
    def __init__(self,dictObj,path=None):
        self.dictObj = dictObj
        self.path = path

    def get_key_value_at_path(self):
        if not bool(self.path):
            return  self.dictObj
        if type(self.dictObj) is not dict :
            raise ValueError(' object must be a dict')
        if type(self.path) is not str and type(self.path) is not list:
            raise ValueError('path is supposed to be a string')
        if type(self.path) is str:
            self.path = self.path.strip('/').split('/')
        key = self.path[0]
        if key in self.dictObj.keys():
            self.dictObj = self.dictObj[key]
            self.path =  self.path[1:]
            return self.get_key_value_at_path()
        else:
            return "Not Found"

