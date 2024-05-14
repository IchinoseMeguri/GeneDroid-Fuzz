import random
import string
from .intent import Intent
from .intent_process import IntentProcess
from .global_config import global_config


class IntentGenerator:
    def __init__(self):
        # 定义启发式规则
        self.action_rules = {
            'text/plain': ['ACTION_SEND'],
            'image/jpeg': ['ACTION_SEND', 'ACTION_VIEW'],
            'video/mp4': ['ACTION_SEND', 'ACTION_VIEW']
        }
        self.data_types = list(self.action_rules.keys())
        self.messages = ['这是一条测试消息', 'Hello, World!', '这是一个示例文本', 'Test message']
        self.packages = ['com.whatsapp', 'com.facebook.messaging', 'com.google.android.gm']

    def generate_intent(self, data_type=None):
        # 如果未指定数据类型，则随机选择一个数据类型
        if data_type is None:
            data_type = random.choice(self.data_types)
        
        # 根据数据类型选择操作类型
        actions = self.action_rules.get(data_type, ['ACTION_SEND'])
        action = random.choice(actions)

        # 根据数据类型获取相关消息内容
        message = self.get_relevant_message(data_type)

        # 根据操作类型获取相关应用程序包名
        package = self.get_relevant_package(action)

        # 构建 Intent 代码
        intent = Intent(action=action, mime_type=data_type, \
                            extra_string={'android.intent.extra.TEXT': message}, \
                            component=package)

        intent.cmd=intent.get_cmd()

        return intent

    def get_relevant_message(self, data_type):
        # 如果数据类型为文本，则随机选择一条消息
        if data_type == 'text/plain':
            return random.choice(self.messages)
        # 否则，返回一个默认消息
        else:
            return "这是一条测试消息"

    def get_relevant_package(self, action):
        # 如果操作类型为发送，则随机选择一个应用程序包名
        if action == 'ACTION_SEND':
            return random.choice(self.packages)
        # 否则，返回一个默认包名
        else:
            return 'com.example.default.package'





class HeuristicFuzz:

    def __init__(self):
        self.intents=[]

    def get_intents(self):
        return self.intents

    # 启发式方法生成Intent
    def generate_strings_heuristic(self,num_strings):
        intents_strings = []
        for _ in range(num_strings):
            # 在这里可以根据需求定义不同的启发式方法生成Intent

            option_num= 20
            r_times = random.randint(0,option_num-1)
            print("r_times is: ",r_times)

            for _ in range(r_times):
                intent_generater = IntentGenerator()
                intent_generated = intent_generater.generate_intent()
                print("intent_generated is: ",intent_generated.cmd)
                intents_strings.append(intent_generated)

                '''
                r=random.randint(0,option_num-1)
                
                # 例如随机生成字符串长度
                length = random.randint(5, 15)  
                # 从字母表中随机选择字符生成字符串
                string_generated = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
                print("string_generated is: ",string_generated)
                if r==0:
                    intent_generated.prefix = string_generated
                elif r==1:
                    intent_generated.action = string_generated
                elif r==2:
                    intent_generated.data_uri = string_generated
                elif r==3:
                    intent_generated.mime_type = string_generated
                elif r==4:
                    intent_generated.category = string_generated
                elif r==5:
                    intent_generated.component = string_generated
                elif r==6:
                    intent_generated.flag = string_generated
                elif r==7:
                    intent_generated.extra_keys=[].append(string_generated)
                elif r==8:
                    string_generated = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(5, 15)))
                    intent_generated.extra_string={string_generated:string_generated}
                elif r==9:
                    bool_generated = random.choice([True, False])
                    intent_generated.extra_boolean={string_generated:bool_generated}
                elif r==10:
                    int_generated=random.randint(0,100)
                    intent_generated.extra_int={string_generated:int_generated}
                elif r==11:
                    long_generated=random.randint(0,1000000000)
                    intent_generated.extra_long={string_generated:long_generated}
                elif r==12:
                    float_generated=random.uniform(0,100)
                    intent_generated.extra_float={string_generated:float_generated}
                elif r==13:
                    uri_generated = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(5, 15)))
                    intent_generated.extra_uri={string_generated:uri_generated}
                elif r==14:
                    compoment_generated = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(5, 15)))
                    intent_generated.extra_component={string_generated:compoment_generated}
                elif r==15:
                    array_int_generated = []
                    r=random.randint(0,10)
                    for _ in range(r):
                        array_int_generated.append(random.randint(0,100))
                    intent_generated.extra_array_int={string_generated:array_int_generated}
                elif r==16:
                    array_long_generated = []
                    r=random.randint(0,10)
                    for _ in range(r):
                        array_long_generated.append(random.randint(0,1000000000))
                    intent_generated.extra_array_long={string_generated:array_long_generated}
                elif r==17:
                    array_float_generated = []
                    r=random.randint(0,10)
                    for _ in range(r):
                        array_float_generated.append(random.uniform(0,100))
                    intent_generated.extra_array_float={string_generated:array_float_generated}
                elif r==18:
                    intent_generated.flags=[].append(string_generated)
                elif r==19:
                    intent_generated.suffix = string_generated

            intent_generated.cmd=None
            intent_generated.get_cmd()
            print("intent_generated is: ",intent_generated)
            strings.append(intent_generated)
        '''
                

        self.intents = intents_strings
        return intents_strings

    # 模糊测试对字符串进行扩展
    def fuzz_strings(self, num_fuzzed_intents):
        fuzzed_intents = []
        print("Fuzzing intents")
        for intent_item in self.intents:
            print(intent_item)
        print("-------------------")
        for intent_item in self.intents:
            for _ in range(num_fuzzed_intents):
                intent_process = IntentProcess(intent_item)
                r=random.randint(0,global_config["mutation_weight_prefix_sum"][-1]-1)
                print("random number is: ",r)
                # r= 4.5 #Test
                # print("weight is: ",r)
                if r < global_config["mutation_weight_prefix_sum"][0]:
                    intent_process.single_char_add()
                elif r < global_config["mutation_weight_prefix_sum"][1]:
                    intent_process.single_char_del()
                elif r < global_config["mutation_weight_prefix_sum"][2]:
                    intent_process.single_char_mod()
                elif r < global_config["mutation_weight_prefix_sum"][3]:
                    intent_process.multi_char_add()
                elif r < global_config["mutation_weight_prefix_sum"][4]:
                    intent_process.multi_char_del()
                elif r < global_config["mutation_weight_prefix_sum"][5]:
                    intent_process.multi_char_mod()
                elif r < global_config["mutation_weight_prefix_sum"][6]:
                    intent_to_fragment_swap = self.intents[random.randint(0, len(self.intents) - 1)]
                    intent_process.char_fragment_swap(intent_to_fragment_swap)
                elif r < global_config["mutation_weight_prefix_sum"][7]:
                    intent_process.add_null()
                elif r < global_config["mutation_weight_prefix_sum"][8]:
                    intent_process.extreme_length()
                elif r < global_config["mutation_weight_prefix_sum"][9]:
                    intent_process.havoc()
                fuzzed_intent = intent_process.get_intent()
                fuzzed_intents.append(fuzzed_intent)

        return fuzzed_intents


    # 测试函数
    def run_tests(self):
        basic_strings = self.generate_strings_heuristic(5)
        fuzzed_strings = self.fuzz_strings(num_fuzzed_intents=3)
        all_strings = basic_strings + fuzzed_strings
        print("Generated intents:")
        for string in all_strings:
            print(string)

if __name__ == "__main__":
    heuristic_fuzz = HeuristicFuzz()
    heuristic_fuzz.run_tests()
