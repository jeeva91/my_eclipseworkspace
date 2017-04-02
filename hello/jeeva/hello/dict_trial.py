'''
Created on Mar 18, 2017

@author: jee11
'''

dict={0:0}

for i in range(1,10):
    temp_dict={i:i}
    dict.update(temp_dict)
    print(temp_dict)
    
print(dict)


if __name__ == '__main__':
    pass