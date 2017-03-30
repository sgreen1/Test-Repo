def reformat_mac(mac):
    mac0 = mac.split()[0][0]
    mac1 = mac.split()[0][1]
    mac2 = mac.split()[0][2]
    mac3 = mac.split()[0][3]
    mac4 = mac.split()[0][5]
    mac5 = mac.split()[0][6]
    newmac = mac0 + mac1 + ":" + mac2 + mac3 + ":" + mac4 + mac5
    return newmac.upper()

asdfasdf
