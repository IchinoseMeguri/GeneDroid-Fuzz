

from intent import Intent

import string

'''
单字符的增删改
多字符的增删改
字符片段的交换
加空值
灾变形变异好长好长的
'''


import random

import time
import eventlet


class IntentProcess:
    def __init__(self, intent: Intent):
        self.intent = intent
        self.intent.get_cmd()


    # 单字符的增删改
    def single_char_add(self):
        cmd_len=len(self.intent.cmd)
        if cmd_len==0:
            return
        add_index=random.randint(0,cmd_len-1)
        print("single_char_add index: ",add_index)
        add_char=random.choice(string.ascii_letters+string.digits)
        self.intent.cmd=self.intent.cmd[:add_index]+add_char+self.intent.cmd[add_index:]
        self.intent.write_params_from_cmd()

    def single_char_del(self):
        cmd_len=len(self.intent.cmd)
        if cmd_len==0:
            return
        del_index=random.randint(0,cmd_len-1)
        print("single_char_del index: ",del_index)
        self.intent.cmd=self.intent.cmd[:del_index]+self.intent.cmd[del_index+1:]
        self.intent.write_params_from_cmd()

    def single_char_mod(self):
        cmd_len=len(self.intent.cmd)
        if cmd_len==0:
            return
        mod_index=random.randint(0,cmd_len-1)
        print("single_char_mod index: ",mod_index)
        mod_char=random.choice(string.ascii_letters+string.digits)
        self.intent.cmd=self.intent.cmd[:mod_index]+mod_char+self.intent.cmd[mod_index+1:]
        self.intent.write_params_from_cmd()

    # 多字符的增删改
    def multi_char_add(self):
        cmd_len=len(self.intent.cmd)
        if cmd_len==0:
            return
        add_index=random.randint(0,cmd_len-1)
        add_len=random.randint(1,cmd_len)
        add_str=""
        print("multi_char_add index: ",add_index," add_len: ",add_len)
        for _ in range(add_len):
            add_str+=random.choice(string.ascii_letters+string.digits)
        self.intent.cmd=self.intent.cmd[:add_index]+add_str+self.intent.cmd[add_index:]
        self.intent.write_params_from_cmd()

    def multi_char_del(self):
        cmd_len=len(self.intent.cmd)
        if cmd_len==0:
            return
        del_index=random.randint(0,cmd_len-1)
        del_len=random.randint(1,cmd_len-del_index)
        print("multi_char_del index: ",del_index," del_len: ",del_len)
        self.intent.cmd=self.intent.cmd[:del_index]+self.intent.cmd[del_index+del_len:]
        self.intent.write_params_from_cmd()

    def multi_char_mod(self):
        cmd_len=len(self.intent.cmd)
        if cmd_len==0:
            return
        mod_index=random.randint(0,cmd_len-1)
        mod_len=random.randint(1,cmd_len-mod_index)
        mod_str=""
        print("multi_char_mod index: ",mod_index," mod_len: ",mod_len)
        for _ in range(mod_len):
            mod_str+=random.choice(string.ascii_letters+string.digits)
        self.intent.cmd=self.intent.cmd[:mod_index]+mod_str+self.intent.cmd[mod_index+mod_len:]
        self.intent.write_params_from_cmd()

    # 字符片段的交换
    def char_fragment_swap(self,intent2: Intent):
        option_num=20
        max_cnt=100
        print("char_fragment_swap")
        while max_cnt > 0:
            swap_option=random.randint(0,option_num-1)

            if swap_option==0:
                if self.intent.prefix is not None and intent2.prefix is not None:
                    self.intent.prefix=intent2.prefix
                    break
            elif swap_option==1:
                if self.intent.action is not None and intent2.action is not None:
                    self.intent.action=intent2.action
                    break
            elif swap_option==2:
                if self.intent.data_uri is not None and intent2.data_uri is not None:
                    self.intent.data_uri=intent2.data_uri
                    break
            elif swap_option==3:
                if self.intent.mime_type is not None and intent2.mime_type is not None:
                    self.intent.mime_type=intent2.mime_type
                    break
            elif swap_option==4:
                if self.intent.category is not None and intent2.category is not None:
                    self.intent.category=intent2.category
                    break
            elif swap_option==5:
                if self.intent.component is not None and intent2.component is not None:
                    self.intent.component=intent2.component
                    break
            elif swap_option==6:
                if self.intent.flag is not None and intent2.flag is not None:
                    self.intent.flag=intent2.flag
                    break
            elif swap_option==7:
                if self.intent.extra_keys is not None and intent2.extra_keys is not None:
                    self.intent.extra_keys=intent2.extra_keys
                    break
            elif swap_option==8:
                if self.intent.extra_string is not None and intent2.extra_string is not None:
                    self.intent.extra_string=intent2.extra_string
                    break
            elif swap_option==9:
                if self.intent.extra_boolean is not None and intent2.extra_boolean is not None:
                    self.intent.extra_boolean=intent2.extra_boolean
                    break
            elif swap_option==10:
                if self.intent.extra_int is not None and intent2.extra_int is not None:
                    self.intent.extra_int=intent2.extra_int
                    break
            elif swap_option==11:
                if self.intent.extra_long is not None and intent2.extra_long is not None:
                    self.intent.extra_long=intent2.extra_long
                    break
            elif swap_option==12:
                if self.intent.extra_float is not None and intent2.extra_float is not None:
                    self.intent.extra_float=intent2.extra_float
                    break
            elif swap_option==13:
                if self.intent.extra_uri is not None and intent2.extra_uri is not None:
                    self.intent.extra_uri=intent2.extra_uri
                    break
            elif swap_option==14:
                if self.intent.extra_component is not None and intent2.extra_component is not None:
                    self.intent.extra_component=intent2.extra_component
                    break
            elif swap_option==15:
                if self.intent.extra_array_int is not None and intent2.extra_array_int is not None:
                    self.intent.extra_array_int=intent2.extra_array_int
                    break
            elif swap_option==16:
                if self.intent.extra_array_long is not None and intent2.extra_array_long is not None:
                    self.intent.extra_array_long=intent2.extra_array_long
                    break
            elif swap_option==17:
                if self.intent.extra_array_float is not None and intent2.extra_array_float is not None:
                    self.intent.extra_array_float=intent2.extra_array_float
                    break
            elif swap_option==18:
                if self.intent.flags is not None and intent2.flags is not None:
                    self.intent.flags=intent2.flags
                    break
            elif swap_option==19:
                if self.intent.suffix is not None and intent2.suffix is not None:
                    self.intent.suffix=intent2.suffix
                    break
            max_cnt-=1

        self.intent.cmd=None
        self.intent.get_cmd()
            

    # 加空值
    def add_null(self):
        option_num=20
        max_cnt=100
        print("add_null")
        while max_cnt > 0:
            add_option=random.randint(0,option_num-1)

            if add_option==0:
                if self.intent.prefix is not None:
                    self.intent.prefix=None
                    break
            elif add_option==1:
                if self.intent.action is not None:
                    self.intent.action=None
                    break
            elif add_option==2:
                if self.intent.data_uri is not None:
                    self.intent.data_uri=None
                    break
            elif add_option==3:
                if self.intent.mime_type is not None:
                    self.intent.mime_type=None
                    break
            elif add_option==4:
                if self.intent.category is not None:
                    self.intent.category=None
                    break
            elif add_option==5:
                if self.intent.component is not None:
                    self.intent.component=None
                    break
            elif add_option==6:
                if self.intent.flag is not None:
                    self.intent.flag=None
                    break
            elif add_option==7:
                if self.intent.extra_keys is not None:
                    self.intent.extra_keys=None
                    break
            elif add_option==8:
                if self.intent.extra_string is not None:
                    self.intent.extra_string=None
                    break
            elif add_option==9:
                if self.intent.extra_boolean is not None:
                    self.intent.extra_boolean=None
                    break
            elif add_option==10:
                if self.intent.extra_int is not None:
                    self.intent.extra_int=None
                    break
            elif add_option==11:
                if self.intent.extra_long is not None:
                    self.intent.extra_long=None
                    break
            elif add_option==12:
                if self.intent.extra_float is not None:
                    self.intent.extra_float=None
                    break
            elif add_option==13:
                if self.intent.extra_uri is not None:
                    self.intent.extra_uri=None
                    break
            elif add_option==14:
                if self.intent.extra_component is not None:
                    self.intent.extra_component=None
                    break
            elif add_option==15:
                if self.intent.extra_array_int is not None:
                    self.intent.extra_array_int=None
                    break
            elif add_option==16:
                if self.intent.extra_array_long is not None:
                    self.intent.extra_array_long=None
                    break
            elif add_option==17:
                if self.intent.extra_array_float is not None:
                    self.intent.extra_array_float=None
                    break
            elif add_option==18:
                if self.intent.flags is not None:
                    self.intent.flags=None
                    break
            elif add_option==19:
                if self.intent.suffix is not None:
                    self.intent.suffix=None
                    break
            max_cnt-=1

        self.intent.cmd=None
        self.intent.get_cmd()

    # 灾变形变异好长好长的
    def extreme_length(self):
        length_limit=2047
        option_list=self.intent.cmd.split(" ")
        list_len=len(option_list)
        cmd_len=len(self.intent.cmd)
        print("extreme_length")
        while cmd_len <= length_limit and list_len > 4:
            option=int(random.randint(2,list_len-2))
            self.intent.cmd+=" "+option_list[option]
            self.intent.cmd+=" "+option_list[option+1]
            cmd_len=len(self.intent.cmd)

        self.intent.cmd=self.intent.cmd[:length_limit]
        
        self.intent.write_params_from_cmd()
            
    # Havoc
    def havoc(self):
        times=random.randint(10,100)
        print("havoc times: ",times)
        import copy
        temp_intent=copy.deepcopy(self.intent)

        
        
        while times > 0:
            if times%50==0:
                print(self.intent)
            times-=1
            eventlet.monkey_patch()
            try:
                with eventlet.Timeout(10):
                    havoc_method=random.randint(0,8)
                    if havoc_method==0:
                        self.single_char_add()
                    elif havoc_method==1:
                        self.single_char_del()
                    elif havoc_method==2:
                        self.single_char_mod()
                    elif havoc_method==3:
                        self.multi_char_add()
                    elif havoc_method==4:
                        self.multi_char_del()
                    elif havoc_method==5:
                        self.multi_char_mod()
                    elif havoc_method==6:
                        self.char_fragment_swap(temp_intent)
                    elif havoc_method==7:
                        self.add_null()
                    elif havoc_method==8:
                        self.extreme_length()
            except eventlet.timeout.Timeout:
                print("havoc timeout!")
                break
            except:
                print("havoc error break!")
                break

    
    def __str__(self) -> str:
        return self.intent.__str__()
    
    def get_intent(self):
        return self.intent
    

# Test
if __name__ == "__main__":
    
    intent = Intent(action="android.intent.action.VIEW", data_uri="http://www.baidu.com", mime_type="text/plain", component="com.android.browser/.BrowserActivity")
    print(intent)
    print("-----------------")
    intent_process = IntentProcess(intent)
    print(intent_process)

    print("-----------------")
    intent_process.single_char_add()
    print("single_char_add:")
    print(intent_process)
    print("-----------------")
    intent_process.single_char_del()
    print("single_char_del:")
    print(intent_process)
    print("-----------------")
    intent_process.single_char_mod()
    print("single_char_mod:")
    print(intent_process)
    print("-----------------")
    intent_process.multi_char_add()
    print("multi_char_add:")
    print(intent_process)
    print("-----------------")
    intent_process.multi_char_del()
    print("multi_char_del:")
    print(intent_process)
    print("-----------------")
    intent_process.multi_char_mod()
    print("multi_char_mod:")
    print(intent_process)
    print("-----------------")
    intent_process.add_null()
    print("add_null:")
    print(intent_process)
    print("-----------------")
    intent_process.extreme_length()
    print("havoc:")
    print(intent_process)
    print("-----------------")
    intent2 = Intent(action="android.intent.action.TEXT", data_uri="http://www.google.com", mime_type="text/json", component="com.android.text/.TouchActivity")
    intent_process.char_fragment_swap(intent2)
    print("char_fragment_swap:")
    print(intent_process)
    print("-----------------")
    print("-----------------")


    intent3 = Intent(action="android.intent.action.VIEW", data_uri="http://www.baidu.com", mime_type="text/plain", component="com.android.browser/.BrowserActivity")
    intent_process2 = IntentProcess(intent3)
    print(intent_process2)
    intent_process2.extreme_length()
    print(intent_process2)




    print("-----------------")
    print("-----------------")
    print("-----------------")
    print(intent_process.get_intent().to_key_value())
    print("-----------------")
    print(intent3.to_key_value())

    

    intent4 = Intent(action="android.intent.action.VIEW", data_uri="http://www.baidu.com", mime_type="text/plain", component="com.android.browser/.BrowserActivity")
    intent_process3 = IntentProcess(intent4)
    print(intent_process3)
    intent_process3.havoc()
    print("-----------------")
    print(intent_process3)
