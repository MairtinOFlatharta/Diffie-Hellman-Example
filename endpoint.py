class Endpoint:

    def __init__(self, name, private_key, prime, prim_root):
        self.name = name
        self.private_key = private_key
        self.prime = prime
        self.prim_root = prim_root
        self.full_key = None
        self.public_key = None

    def gen_public_key(self):
        self.public_key = pow(self.prim_root, self.private_key, self.prime)
        return self.public_key

    def gen_full_key(self, alt_public_key):
        self.full_key = pow(alt_public_key, self.private_key, self.prime)
        return self.full_key

    def __str__(self):
        string = (f'Endpoint name: {self.name}\n'
                  f'Private key: {self.private_key}\n'
                  f'Prime number: {self.prime}\n'
                  f'Primitive root: {self.prim_root}\n'
                  f'Public key: {self.public_key}\n'
                  f'Full session key: {self.full_key}\n')
        return string


class MitM(Endpoint):

    def crack_private_key(self, Endpoint):
        # Cycle through all possible private keys and generate public keys
        # When matching public key is found, i is a candidate private key
        # Even if found key is not the same as private key, it can still
        # be used to calculate the same full session key
        for i in range(1, Endpoint.prime):
            if pow(Endpoint.prim_root, i, Endpoint.prime) == \
                    Endpoint.public_key:

                print(f'Potential private key for {Endpoint.name}: {i}')
                return i
