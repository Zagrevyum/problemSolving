class CIDR():

    def maskToCIDR(self, mask):
        blocks = mask.split(".")
        cidr = 0
        for block in blocks:
            numBlock = int(block)
            n = 128
            while numBlock > 0:
                numBlock -= n
                n //= 2
                cidr += 1
        return "/"+str(cidr)

    def cidrtoMask(self, cidr):
        cidr = cidr.split("/")
        cidr = int(cidr[1])
        cidr_blocks = [0, 0, 0, 0]
        block = 0
        n = 128
        for i in range(cidr, 0, -1):
            cidr_blocks[block] += n
            n //= 2
            if cidr_blocks[block] == 255:
                n = 128
                block += 1
        return str(cidr_blocks[0])+"."+str(cidr_blocks[1])+"."+str(cidr_blocks[2])+"."+str(cidr_blocks[3])


solution = CIDR()

print(solution.maskToCIDR("255.255.192.0"))
print(solution.maskToCIDR("255.255.0.0"))
print(solution.maskToCIDR("255.255.255.254"))

print(solution.cidrtoMask("/18"))
print(solution.cidrtoMask("/16"))
print(solution.cidrtoMask("/31"))
