#pip install socket
#pip3 install os
import socket,sys,os

if len(sys.argv)==3:
    ip=sys.argv[1]
    rangeOfports=sys.argv[2]
    rangeOfports=rangeOfports.split("-",2)
    print(f"""
          ***********
          IP:{ip}
          ***********
          """
          )
    try:
         for port in range(int(rangeOfports[0]),int(rangeOfports[1])):
             s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
             result=s.connect_ex((ip,port)) 
             if result==0:
                 print(f"Port {port} is open ***")
    except KeyboardInterrupt:
        print("Scan  Cancelled")
    except socket.gaierror:
        print("Server Not Responding")
             
else:
    print("Invalid ammount argument")