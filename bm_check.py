import struct

filename = raw_input('Filename:')
with open(filename, 'rb') as f:
    s = f.read(30)
    st = struct.unpack('<ccIIIIIIHH', s)
    print 'St=', st
    if s[:2] == 'BM' or s[:2] == 'BA':
        print 'This is a Bitmap file.'
        print '  Size: %d*%d' % (st[6], st[7])
        print '  Color: %d' % (2 ** int(st[9]))
    else:
        print 'This is not a Bitmap file.'