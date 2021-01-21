class topic_msg():

    def init(self, topic):
        self.topic_name= topic  # making topic as empty
        self.msg= ""


pub_topic_list=[]
class publish:

    def __init__(self,topic_name):
        
        if topic_name not in pub_topic_list:  # checks if publish topic is in global list of all the topics being published
            pub_topic_list.append(topic_name)

        self.pub_topic = topic_name

    def publish(self,msg):
        self.current_msg = msg


sub_topic_name=[]
class subscribe(object):
    """
    docstring
    """
    def __init__(self, topic_name):
        
        if topic_name not in sub_topic_list:  # checks if subscribed topic is in global list of all the topics being subscrbed
            pub_topic_list.append(topic_name)

        self.sub_topic = topic_name
    
    def sub(self,topic_name):
        pass

