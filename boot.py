import server
from constants import ip
print("Please go to http://" + ip + ":3333/" + " to use the interface")
print("KEY_IP=" + ip)
server.run()
