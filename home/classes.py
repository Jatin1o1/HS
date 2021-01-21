class sensor(object):
    sensor_count=0
    def __init__(self,name,topic,val_type=analog,update_rate=1):
        self.sensor_name=name # increase sensor count by 1 each time new sensor instance is created
        sensor_count +=1 
        self.topic=topic
        self.value_type= val_type

class relay(object):
    relay_count=0
    def __init__(self,relay_no,device_attached):
        self.relay_no=relay_no
        relay_count += 1 # increase relay count by 1 each time new relay instance is created
        self.device_attached=device_attached
        
class board(object):
    boards_count=0
    def __init__(self,board_number,room_no):
        self.board_no=board_number
        boards_count += 1  # increase boards count by 1 each time new board instance is created
        self.board_serial=serial_no
        self.board_ip=board_ip
        self.room_no=room_no

class room(object):
    room_count=0
    def __init__(self,id):
        self.room_id=id
        room_count  += 1           # increase rooms count by 1 each time new rooms instance is created
        
class house(object):
    def __init__(self,name):
        self.house_name=name
        self.house_address=address
        self.gps=gps_coordinates
        self.house_owner=house_owner
        self.no_residents=no_of_residents
        
        
class users():
    user_count=0
    def __init__(self,name,age):
        self.name=name
        user_count += 1# increase user count by 1 each time new user instance is created
        self.age=age
