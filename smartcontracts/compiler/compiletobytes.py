
class CompileToBytes():
    """ Compiles the Contract to Bytes """
    def __init__(self):
        pass

    def encodeContract(Contract: list):
        """ Encodes the contract to turn it into bytes """
        encodedData = ''
        for data in Contract:
            encodedData + data
        encodedData = encodedData.encode()
        return encodedData

    def turnToBytes(encodedData):
        """ Encodes the contract into bytes """
        bytesdata = bytes(encodedData)
        return bytesdata
