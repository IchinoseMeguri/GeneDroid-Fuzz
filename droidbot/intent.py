class Intent(object):
    """
    this class describes a intent event
    中文：此类描述一个意图事件
    """

    def __init__(self, 
                 prefix="start", action=None, data_uri=None, mime_type=None, category=None,
                 component=None, flag=None, extra_keys=None, extra_string=None, extra_boolean=None,
                 extra_int=None, extra_long=None, extra_float=None, extra_uri=None, extra_component=None,
                 extra_array_int=None, extra_array_long=None, extra_array_float=None, flags=None, suffix=""):
        self.event_type = 'intent'
        
        self.prefix = prefix
        self.action = action
        self.data_uri = data_uri
        self.mime_type = mime_type
        self.category = category
        self.component = component
        self.flag = flag
        self.extra_keys = extra_keys
        self.extra_string = extra_string
        self.extra_boolean = extra_boolean
        self.extra_int = extra_int
        self.extra_long = extra_long
        self.extra_float = extra_float
        self.extra_uri = extra_uri
        self.extra_component = extra_component
        self.extra_array_int = extra_array_int
        self.extra_array_long = extra_array_long
        self.extra_array_float = extra_array_float
        self.flags = flags
        self.suffix = suffix
        self.cmd = None
        self.get_cmd()

    def get_cmd(self):
        """
        convert this intent to cmd string
        中文：将此意图转换为cmd字符串
        :rtype : object
        :return: str, cmd string
        """

        if self.cmd is not None:
            return self.cmd
        cmd = "am "
        if self.prefix:
            cmd += self.prefix
        if self.action is not None:
            cmd += " -a " + self.action
        if self.data_uri is not None:
            cmd += " -d " + self.data_uri
        if self.mime_type is not None:
            cmd += " -t " + self.mime_type
        if self.category is not None:
            cmd += " -c " + self.category
        if self.component is not None:
            cmd += " -n " + self.component
        if self.flag is not None:
            cmd += " -f " + self.flag
        if self.extra_keys:
            for key in self.extra_keys:
                cmd += " --esn '%s'" % key
        if self.extra_string:
            for key in list(self.extra_string.keys()):
                cmd += " -e '%s' '%s'" % (key, self.extra_string[key])
        if self.extra_boolean:
            for key in list(self.extra_boolean.keys()):
                cmd += " -ez '%s' %s" % (key, self.extra_boolean[key])
        if self.extra_int:
            for key in list(self.extra_int.keys()):
                cmd += " -ei '%s' %s" % (key, self.extra_int[key])
        if self.extra_long:
            for key in list(self.extra_long.keys()):
                cmd += " -el '%s' %s" % (key, self.extra_long[key])
        if self.extra_float:
            for key in list(self.extra_float.keys()):
                cmd += " -ef '%s' %s" % (key, self.extra_float[key])
        if self.extra_uri:
            for key in list(self.extra_uri.keys()):
                cmd += " -eu '%s' '%s'" % (key, self.extra_uri[key])
        if self.extra_component:
            for key in list(self.extra_component.keys()):
                cmd += " -ecn '%s' %s" % (key, self.extra_component[key])
        if self.extra_array_int:
            for key in list(self.extra_array_int.keys()):
                cmd += " -eia '%s' %s" % (key, ",".join(self.extra_array_int[key]))
        if self.extra_array_long:
            for key in list(self.extra_array_long.keys()):
                cmd += " -ela '%s' %s" % (key, ",".join(self.extra_array_long[key]))
        if self.extra_array_float:
            for key in list(self.extra_array_float.keys()):
                cmd += " -efa '%s' %s" % (key, ",".join(self.extra_array_float[key]))
        if self.flags:
            cmd += " " + " ".join(self.flags)
        if self.suffix:
            cmd += " " + self.suffix
        self.cmd = cmd
        return self.cmd

    def __str__(self):
        return self.get_cmd()
    
    def to_key_value(self):
        """
        convert this intent to key-value pairs
        中文：将此意图转换为键值对
        :rtype : object
        :return: dict, key-value pairs
        """
        intent_dict = {}
        if self.action is not None:
            intent_dict["action"] = self.action
        if self.data_uri is not None:
            intent_dict["data_uri"] = self.data_uri
        if self.mime_type is not None:
            intent_dict["mime_type"] = self.mime_type
        if self.category is not None:
            intent_dict["category"] = self.category
        if self.component is not None:
            intent_dict["component"] = self.component
        if self.flag is not None:
            intent_dict["flag"] = self.flag
        if self.extra_keys:
            intent_dict["extra_keys"] = self.extra_keys
        if self.extra_string:
            intent_dict["extra_string"] = self.extra_string
        if self.extra_boolean:
            intent_dict["extra_boolean"] = self.extra_boolean
        if self.extra_int:
            intent_dict["extra_int"] = self.extra_int
        if self.extra_long:
            intent_dict["extra_long"] = self.extra_long
        if self.extra_float:
            intent_dict["extra_float"] = self.extra_float
        if self.extra_uri:
            intent_dict["extra_uri"] = self.extra_uri
        if self.extra_component:
            intent_dict["extra_component"] = self.extra_component
        if self.extra_array_int:
            intent_dict["extra_array_int"] = self.extra_array_int
        if self.extra_array_long:
            intent_dict["extra_array_long"] = self.extra_array_long
        if self.extra_array_float:
            intent_dict["extra_array_float"] = self.extra_array_float
        if self.flags:
            intent_dict["flags"] = self.flags
        if self.suffix:
            intent_dict["suffix"] = self.suffix

        return intent_dict
    
    def write_params_from_cmd(self):
        """
        write parameters from cmd string
        中文：从cmd字符串写入参数
        """
        option_list=self.cmd.split(" ")
        length=len(option_list)
        if length==0:
            return
        
        i=0
        while i < length-1:
            if option_list[i].startswith("-") is False:
                i+=1
                continue
            if option_list[i]=="-a":
                self.action=option_list[i+1]
            elif option_list[i]=="-d":
                self.data_uri=option_list[i+1]
            elif option_list[i]=="-t":
                self.mime_type=option_list[i+1]
            elif option_list[i]=="-c":
                self.category=option_list[i+1]
            elif option_list[i]=="-n":
                self.component=option_list[i+1]
            elif option_list[i]=="-f":
                self.flag=option_list[i+1]
            elif option_list[i]=="--esn":
                self.extra_keys.append(option_list[i+1])

            
            # elif option_list[i]=="-e":
            #     if len(option_list) > i+2:
            #         if option_list[i+1] is not None and option_list[i+2].startswith("-") is False:
            #             self.extra_string[option_list[i+1]]=option_list[i+2]
            

            elif option_list[i]=="-ez":
                print (len(option_list),i)
                if len(option_list) > i+2:
                    if option_list[i+1] is not None and option_list[i+2].startswith("-") is False:
                        self.extra_boolean[option_list[i+1]]=option_list[i+2]
            elif option_list[i]=="-ei":
                if len(option_list) > i+2:
                    if option_list[i+1] is not None and option_list[i+2].startswith("-") is False:
                        self.extra_int[option_list[i+1]]=option_list[i+2]
            elif option_list[i]=="-el":
                if len(option_list) > i+2:
                    if option_list[i+1] is not None and option_list[i+2].startswith("-") is False:
                        self.extra_long[option_list[i+1]]=option_list[i+2]
            elif option_list[i]=="-ef":
                if len(option_list) > i+2:
                    if option_list[i+1] is not None and option_list[i+2].startswith("-") is False:
                        self.extra_float[option_list[i+1]]=option_list[i+2]
            elif option_list[i]=="-eu":
                if len(option_list) > i+2:
                    if option_list[i+1] is not None and option_list[i+2].startswith("-") is False:
                        self.extra_uri[option_list[i+1]]=option_list[i+2]
            elif option_list[i]=="-ecn":
                if len(option_list) > i+2:
                    if option_list[i+1] is not None and option_list[i+2].startswith("-") is False:
                        self.extra_component[option_list[i+1]]=option_list[i+2]
            elif option_list[i]=="-eia":
                if len(option_list) > i+2:
                    if option_list[i+1] is not None and option_list[i+2].startswith("-") is False:
                        self.extra_array_int[option_list[i+1]]=option_list[i+2].split(",")
            elif option_list[i]=="-ela":
                if len(option_list) > i+2:
                    if option_list[i+1] is not None and option_list[i+2].startswith("-") is False:
                        self.extra_array_long[option_list[i+1]]=option_list[i+2].split(",")
            elif option_list[i]=="-efa":
                if len(option_list) > i+2:
                    if option_list[i+1] is not None and option_list[i+2].startswith("-") is False:
                        self.extra_array_float[option_list[i+1]]=option_list[i+2].split(",")
            elif option_list[i].startswith("-"):
                if(self.flags is None):
                    self.flags=[]
                self.flags.append(option_list[i])
            i+=1

        if i<length:
            self.suffix=" ".join(option_list[i:length])

