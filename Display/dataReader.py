import struct

def bin2float(filepath, length) -> tuple:
    with open(filepath, 'rb') as f:
        ans = struct.unpack(str(length) + "f", f.read())

    return ans
