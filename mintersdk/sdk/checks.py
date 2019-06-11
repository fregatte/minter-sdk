import rlp
from mintersdk import MinterConvertor, MinterPrefix


class MinterCheck(object):
    minter_address = ''
    passphrase = ''
    structure = {
        'nonce': '',
        'chain_id': '',
        'due_block': '',
        'coin': '',
        'value': '',
        'lock': '',
        'v': '',
        'r': '',
        's': ''
        }

    def __init__(self, check_or_address, passphrase=None):
        if isinstance(check_or_address, dict):
            self.structure = self.defineProperties(check_or_address)

        if isinstance(check_or_address, str) and not passphrase:
            self.structure = self.decode(check_or_address)
        elif isinstance(check_or_address, str):
            self.minter_address = check_or_address

        self.passphrase = passphrase

    def getBody(self):
        return self.structure

    def getOwnerAddress(self):
        return self.minter_address

    def sign(self, private_key):
        # TODO
        pass

    def createProof(self):
        # TODO
        pass

    def decode(self, check):
        # TODO
        # prepare check string and convert to hex array
        check = MinterPrefix.remove_prefix(check, MinterPrefix.CHECK)
        check = rlp.decode('0x' + check)
        # $check = Helper::rlpArrayToHexArray($check);

        return {}

    def setOwnerAddress(self, body, signature):
        # TODO
        pass

    def defineProperties(self, check):
        if not self.validateFields(check):
            raise ValueError('Invalid fields')
        return {**self.structure, **self.encode(check)}

    def encode(self, check):
        return {
            'nonce': format(check['nonce'], 'x'),
            'chain_id': format(check['chain_id'], 'x'),
            'due_block': check['dueBlock'],
            'coin': MinterConvertor.encode_coin_name(check['coin']),
            'value': MinterConvertor.convert_value(check['value'], 'pip'),
            }

    def serialize(self, data):
        # TODO
        pass

    def validateFields(self, fields):
        return set(fields.keys()).issubset(self.structure.keys())

    def formatLockFromSignature(self, signature):
        # TODO
        pass
