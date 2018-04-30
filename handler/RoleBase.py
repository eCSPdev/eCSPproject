from flask import jsonify, request
import os, sys

class RoleBase:

    def splitall(self, path):
        allparts = []
        while 1:
            parts = os.path.split(path)
            if parts[0] == path:  # sentinel for absolute paths
                allparts.insert(0, parts[0])
                break
            elif parts[1] == path:  # sentinel for relative paths
                allparts.insert(0, parts[1])
                break
            else:
                path = parts[0]
                allparts.insert(0, parts[1])
        return allparts

    def validate(self, path, form):
        print ('estoy en el validate')
        p = self.splitall(path)
        validate = False
        if p[3] == 'Login':
            print ('User : ', p[1])
            print ('Action : ', p[3])
            validate = True
        #else:


        return validate