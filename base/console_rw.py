'''
Functions for console read and write
'''

def default_data_str(user_input:str,default_input:str):
    return default_input if user_input == '' else user_input

def user_input(message:str,default_input:str=''):
    if(default_input!=''):
        user_input = input( message.strip() + ' (default : ' + str(default_input) + ') ') 
    else:
        user_input = input(message.strip()) 

    return default_data_str(user_input,default_input)
    
def get_int(input:str,default_value:int):
    try : 
        return int(input)
    except:
        print('Invalid input')
        return default_value
    
def print_console(data):
    dataX_index = 1
    for dataX in data : 
        print(str(dataX_index) + '. ' + dataX)
        dataX_index = dataX_index + 1