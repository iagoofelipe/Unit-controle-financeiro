from cryptography.fernet import Fernet 

class Crypto:
    def __init__(self, key=None):
        "Criptografando e descriptografando strings a partir da chave simétrica"
        if key != None:
            self.key = key

    @property
    def key(self):
        return self._key
    
    @key.setter
    def key(self, value):
        self._key = value.encode()

    def decode(self, text: str | bytes):
        
        if type(text) == str:
            text = text.encode()
        
        self.fernet = Fernet(self._key)
        return self.fernet.decrypt(text).decode()
    
    def encode(self, text: str, typeReturn="bytes"):
        self.fernet = Fernet(self._key)
        text_crypt = self.fernet.encrypt(text.encode())

        match typeReturn:
            case 'str':
                return text_crypt.decode()
            case 'bytes':
                return text_crypt