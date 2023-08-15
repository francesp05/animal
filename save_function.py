import datetime

def save_stuff(data):
    current_datetime = datetime.datetime.now()
    filename = 'output-'+current_datetime.strftime("%m-%d-%y-%H-%M")+'.txt'
    data = str(data)
    with open(filename,'w') as file:
        file.write(data)

    return filename