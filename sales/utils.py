#all helper functions
import uuid #UUID, Universal Unique Identifier, is a python library that helps in generating random objects of 128 bits as ids. 
def generate_code():
    code=uuid.uuid4() #uuid4() creates a random UUID.
    code_mod=str(code).replace('-','').upper()[:12]
    return code_mod