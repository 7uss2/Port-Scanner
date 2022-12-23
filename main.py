from socket import *
def conScan(tgtHost, tgtPort):
    try:
        connskt = socket(AF_INET, SOCK_STREAM)
        connskt.connect((tgtHost, tgtPort))
        print('%d/TCP OPEN'% tgtPort )
        connskt.close()
    except:
        print('%d/TCP closed'% tgtPort)


def portscan(tgtHost, tgtports):
    try:
        tgtip = gethostbyname(tgtHost)
    except:
        print('cannot resolve %s '% tgtHost)
        return
    try:
        tgtName = gethostbyaddr(tgtip)
        print('\n scan result of : %s' % tgtName[0])
    except:
         print('\n scan result of : %s'% tgtip)
    setdefaulttimeout(1)
    for tgtPort in tgtports:
        print('scanning port: %d'% tgtPort)
        conScan(tgtHost, int(tgtPort))


if __name__ == '__main__':

  portscan(input( 'Insert Id: '),[80,20,25,22,179,443])