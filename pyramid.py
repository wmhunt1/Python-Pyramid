my_file = open('text.txt', 'r')
data = my_file.read()
text_list = data.split()

for i in range(0, len(text_list)):
    if text_list[i].isdigit():
      text_list[i] = int(text_list[i])
    
int_list = [x for x in text_list if isinstance(x, int)]
string_list = [x for x in text_list if isinstance(x, str)]

dict_list = {}
for key in int_list:
    for value in string_list:
        dict_list[key] = value
        string_list.remove(value)
        break
      
myKeys = list(dict_list.keys())
myKeys.sort()
sorted_dict = {i: dict_list[i] for i in myKeys}

subsets = []

def create_staircase(nums):
  step = 1
  while len(nums) != 0:
    if len(nums) >= step:
      subsets.append(nums[0:step])
      nums = nums[step:]
      step += 1
    else:
      return False
      
  return subsets

staircase = create_staircase(myKeys)

last_item_list = []

for step in staircase:
    last_item = step[-1]
    last_item_list.append(last_item)
    

word_list = []
for key in last_item_list:
  word = sorted_dict.get(key)
  word_list.append(word)

phrase = " ".join(word_list)

print(phrase)
