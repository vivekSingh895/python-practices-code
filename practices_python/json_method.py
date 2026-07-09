import json

data = {  "name": "vivek", 
          "age": 3, 
          "marks": 98
        }
print("type before json file : ",type(data))
json_data = json.dumps(data , indent=4,separators= (",","="))
print(json_data)
print("type convert dict file to JSON : ",type(json_data))

str = """{"hello": "bye" , "marks":65 , "result": "fail"}"""
print("type before string file : ",type(str))
str1 = json.loads(str)
str1 = json.dumps(data , indent=4,separators= (",","="))
print(str1)
print("type after string file :",type(str1))