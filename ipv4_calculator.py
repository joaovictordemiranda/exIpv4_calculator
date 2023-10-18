import re


class Ipv4NetworkCalculator():
    def __init__(self, ip='', prefixo='', mascara='', rede='',
    broadcast='', numero_ips=''):

        self.ip = ip
        self.prefixo = prefixo
        self.mascara = mascara
        self.rede = rede
        self.broadcast = broadcast
        self.numero_ips = numero_ips

        if self.ip == '':
            raise ValueError("IP não enviado.")

        self.ip_tem_prefixo()

        if not self.is_ip():
            raise ValueError("IP inavlido.")

        if not self.prefixo and not self.mascara:
            raise ValueError("Ou o Prefixo ou a Mascara devem ser enviados")

        if self.mascara:
            self.mascara_bin = self.ip_decimal_para_binario(ip=self.mascara)
            self.prefixo_da_mascara()

        self.set_numero_ips()
        self.set_rede_broadcast()
        self.mascara_do_prefixo()

    def mascara_do_prefixo(self):
        mascara_bin = ''

        for i in range(32):
            if i < int(self.prefixo):
                mascara_bin += '1'
            else:
                mascara_bin += '0'
            
        mascara_dec = self.ip_binario_para_decimal(mascara_bin)
        self.mascara_bin = mascara_dec

    def set_rede_broadcast(self):
        ip_bin = self.ip_decimal_para_binario(self.ip)
        ip_bin = ip_bin.replace('.', '')
        
        rede = ''
        broadcast = ''
        for conta, bit in enumerate(ip_bin):
            if conta < int(self.prefixo):
                rede += str(bit)
                broadcast += str(bit)
            else:
                rede += '0'
                broadcast += '1' 
        
        self.rede = self.ip_binario_para_decimal(rede)
        self.broadcast = self.ip_binario_para_decimal(broadcast)

    def ip_binario_para_decimal(self, ip=''):
        novo_ip = str(int(ip[0:8], 2)) + '.'
        novo_ip = str(int(ip[8:16], 2)) + '.'
        novo_ip = str(int(ip[16:24], 2)) + '.'
        novo_ip = str(int(ip[24:32], 2))

        return(novo_ip)

    def set_numero_ips(self):
        host_bits = 32 - int(self.prefixo)
        self.numero_ips: int = pow(2, host_bits)

    def prefixo_da_mascara(self, mascara_bin):
        mascara_bin = str = self.mascara_bin.replace('.', '.')
        conta: int = int(mascara_bin.count('1'))

        self.prefixo: int = conta
            
    def ip_decimal_para_binario(self, ip: str = '')-> str:
            if not ip:
                ip = self.ip
            
            bloco_ip: list = ip.split('.')
            ip_bin: list = []

            for bloco in bloco_ip:
                binario: bin = bin(int(bloco))
                binario: bin = binario[2:].zfill(8)
                ip_bin.append(binario)


            ip_bin: str = '.'.join(ip_bin)
            return(ip_bin)
    
    def ip_tem_prefixo(self):
        ip_prefixo_regexp = re.compile('^[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}/[0-9]{1,2}$')

        if not ip_prefixo_regexp.search(self.ip):
            return

        divide_ip = self.ip.split('.')
        self.ip = divide_ip[0]
        self.perfixo = divide_ip[1]


    def is_ip(self):
        ip_regexp =  re.compile('^[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}$')

        if ip_regexp.search(self.ip):
            return True
        return False
    
    def get_all(self):
        return {        
            'ip': self.ip,
            'prefixo': self.prefixo,
            'rede': self.rede,
            'mascara': self.mascara,
            'broadcast': self.broadcast,
            'numero_ips': self.numero_ips, 
        }

if __name__ == '__main__':
    ipv4 = Ipv4NetworkCalculator(ip='192.168.0.104', mascara='255.255.255.0')
    print(ipv4.get_all())