class Topic_msg():  # class for topic and its current msg
    
    def __init__(self, topic_name):
        self.instance_topic = topic_name  # making topic as empty
        self.instance_topic_msg= ""

pub_topic_list=[]  # list for storing all the current published topics
top_dict={"topicname":"topic instacne"}

class Publish:
    def __init__(self,topic_name):
        print("topic is ",topic_name)

        self.publishing_on_topic = topic_name
        
        if topic_name not in pub_topic_list:  # checks if published topic is in global list of all the topics being published, if not make a topic_msg instance and append in global published list
            
            topic_Instance = Topic_msg(topic_name)      # creates instance of class Topic_msg 

            pub_topic_list.append(topic_Instance)
            #print("topic name is ",str(topic_name), "its instance value is ", topic_Instance)
            #print pub_topic_list[]  # it will contain a instance of class topic_msg
            #print(pub_topic_list[0].instance_topic)  # it will print topic name of the instance of class topic_msg
            
    def publish(self,msg):
        topic_Instance.instance_topic_msg= msg

class subscribe(object):
       
    def __init__(self, topic_name):
        self.instance_subscribing_on_topic = topic_name     # instance subscribing on topic_name
        self.msg_in_subscribed_topic = ""
        
        if topic_name in pub_topic_list:  # checks if subscribed topic is in global list of all the topics being published,
            self.msg_in_subscribed_topic=""
                
    def sub(self,topic_name):
        pass


