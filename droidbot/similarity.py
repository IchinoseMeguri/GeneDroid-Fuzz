import random
import cv2
import numpy as np
from intent import Intent
from intent_process import IntentProcess
import global_config

class IntentSimilarity:
    def __init__(self, intent1:Intent, intent2:Intent):
        intent1.get_cmd()
        intent2.get_cmd()
        self.intent1 = intent1
        self.intent2 = intent2

    def intent_key_jaccard_distance(self):
        """
        calculate the Jaccard distance between two intents
        :return: Jaccard distance
        """
        if self.intent1 is None or self.intent2 is None:
            return 1.0
        if len(self.intent1.to_key_value()) == 0 and len(self.intent2.to_key_value()) == 0:
            return 0.0
        
        # 计算两个Intent的键集合
        keys1 = set(self.intent1.to_key_value().keys())
        print(keys1)
        keys2 = set(self.intent2.to_key_value().keys())
        print(keys2)
        # 计算键的交集和并集
        intersection = keys1.intersection(keys2)
        union = keys1.union(keys2)
        # 计算Jaccard距离
        return len(intersection) / len(union)
    
    def intent_value_jaccard_distance(self):
        """
        calculate the Jaccard distance between two intents
        :return: Jaccard distance
        """
        if self.intent1 is None or self.intent2 is None:
            return 1.0
        if len(self.intent1.to_key_value()) == 0 and len(self.intent2.to_key_value()) == 0:
            return 0.0
        
        # 计算两个Intent的值集合
        values1 = set(self.intent1.to_key_value().values())
        values2 = set(self.intent2.to_key_value().values())
        # 计算值的交集和并集
        intersection = values1.intersection(values2)
        union = values1.union(values2)
        # 计算Jaccard距离
        return len(intersection) / len(union)
    
    def intent_cmd_jaccard_distance(self):
        """
        calculate the Jaccard distance between two intent strings
        :return: Jaccard distance
        """
        if self.intent1 is None or self.intent2 is None:
            return 1.0
        if len(self.intent1.get_cmd()) == 0 and len(self.intent2.get_cmd()) == 0:
            return 0.0
        
        # 计算两个Intent的字符串集合
        cmd1 = set(self.intent1.get_cmd())
        cmd2 = set(self.intent2.get_cmd())
        # 计算字符串的交集和并集
        intersection = cmd1.intersection(cmd2)
        union = cmd1.union(cmd2)
        # 计算Jaccard距离
        return len(intersection) / len(union)
        
        
    def fuzz_intent_with_similarity(self, threshold):
    #将Jaccard距离与fuzz相结合，根据原始Intent生成具有一定相似性的模糊Intent对象

        fuzz_methods_num=9

        # 对原始Intent的每个键值对进行模糊化
        #for key, value in original_intent.items():
            # 在这里实现模糊化逻辑
            # 这里仅作示例：对每个值进行模糊化
            #fuzzy_value = fuzz(value)  # 模糊化每个值
            #fuzzy_intent[key] = fuzzy_value
        import copy
        temp_intent=copy.deepcopy(self.intent1)
        intent_process = IntentProcess(temp_intent)
        # r=random.randint(0,fuzz_methods_num-2)
        # print("random number is: ",r)
        r= 4.5 #Test
        print("weight is: ",r)
        if r < global_config.global_config["mutation_weight_prefix_sum"][0]:
            intent_process.single_char_add()
            print("single_char_add")
        elif r<global_config.global_config["mutation_weight_prefix_sum"][1]:
            intent_process.single_char_del()
            print("single_char_del")
        elif r<global_config.global_config["mutation_weight_prefix_sum"][2]:
            intent_process.single_char_mod()
            print("single_char_mod")
        elif r<global_config.global_config["mutation_weight_prefix_sum"][3]:
            intent_process.multi_char_add()
            print("multi_char_add")
        elif r<global_config.global_config["mutation_weight_prefix_sum"][4]:
            intent_process.multi_char_del()
            print("multi_char_del")
        elif r<global_config.global_config["mutation_weight_prefix_sum"][5]:
            intent_process.multi_char_mod()
            print("multi_char_mod")
        elif r<global_config.global_config["mutation_weight_prefix_sum"][6]:
            intent_process.add_null()
            print("add_null")
        elif r<global_config.global_config["mutation_weight_prefix_sum"][7]:
            intent_process.extreme_length()
            print("havoc")
        
        self.intent2 = intent_process.get_intent()

        print(self.intent1)
        print(self.intent2)

        # 计算原始Intent和模糊Intent之间的Jaccard距离
        distance = self.intent_cmd_jaccard_distance()
        print(distance)

        # 如果Jaccard距离低于阈值，则返回模糊Intent，否则返回None
        if distance < threshold:
            return self.intent2
        else:
            return None

class ImageSimilarity:
    def __init__(self, image1, image2):
        self.image1 = image1
        self.image2 = image2

    def histogram_cosine_similarity(self):
        """
        calculate the cosine similarity between two images
        :return: cosine similarity
        """
        # calculate the histogram of the two images
        hist1 = cv2.calcHist([self.image1], [0], None, [256], [0, 256])
        hist2 = cv2.calcHist([self.image2], [0], None, [256], [0, 256])
        # normalize the histograms
        vector1 = cv2.normalize(hist1, hist1).flatten()
        vector2 = cv2.normalize(hist2, hist2).flatten()
        # calculate the cosine similarity
        similarity = np.dot(vector1, vector2) / (np.linalg.norm(vector1) * np.linalg.norm(vector2))
        return similarity
        


#Test
if __name__ == "__main__":
    intent1 = Intent(action="android.intent.action.TEXT", data_uri="http://www.google.com", mime_type="text/json", component="com.android.text/.TouchActivity", suffix="suffix")
    intent2 = Intent(action="android.intent.action.VIEW", data_uri="http://www.baidu.com", mime_type="text/plain", component="com.android.browser/.BrowserActivity", extra_string={"key1":"value1"}, extra_int={"key2":1})

    intent_similarity = IntentSimilarity(intent1, intent2)
    fuzzy_intent = intent_similarity.fuzz_intent_with_similarity(0.5)
    if(fuzzy_intent):
        print(fuzzy_intent.to_key_value())
    else:
        print("None")
    
    print("-----------------")
    print("cv2 version: ", cv2.__version__)
    print("-----------------")
    
    

    

