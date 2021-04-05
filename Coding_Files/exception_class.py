class DataError(Exception):
    """Raises exceptions for errors during data configuration """
    def __init__(self, message):
        Exception.__init__(self)
        if description is not None:
            self.description = description
        self.response = response

class DataConfigurationError(DataError)
    if not os.path.isfile ('/"""Need JSON FILE NAME HERE"""')
        """We can specify individual types of files if you want"""
        raise DataConfigurationError ('The data you requested could not be found')
    else:
        pass

class UnauthorizedAccess(DataError):
#raise UnauthorizedAccess Error if incorrect DODID or PIN are entered
class DataConfigErr(DataError):
#raise DataConfigErr is data is corrupted

#need to know if we are raising exceptions as e
""" example:
try:
    with open(JSONFILE) as f:
        data = json.load(f)
    print("Data: {}".format(data['data']))
except KeyError:
    pass
except FileNotFoundError:
    raise DataConfigurationError
except json.decoder.JSONDecodeError:
    raise DataConfigErr"""

userInput = input("What is your username?\n")

if DODID == DODID:
    a=input("Password?\n")
    if a == password:
        print("Welcome!")
    else:
        print("Incorrect pwd")
        raise DataConfigErr
else:
   raise DataConfigErr