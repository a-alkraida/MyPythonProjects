import re
read=input('read form file? if yes please directly provide the name of the txt... \n')
input_only=0
if read.upper() == 'N':
    read=input('please provide input \n')
    input_only=1
name=input('file name? \n')
R=input('reset writing file? ')
if R.upper() == 'Y':
    with open(name+'.txt','w') as T:
        T.write('')
divider=input('30 minute per day? if no provide the number \n')
if divider.upper() == 'Y' or divider == '':
    timer=30
else:
    timer=int(divider)
i=''
tasks = []
minutes = 0
seconds = 0 
emp_str = ""
counter = 0
tcount = 0
days=0
if input_only == 0:
    with open(read+'.txt','r') as file:
        for u in file:
            regex = r'[\d]+[m]'
            prefix11 = re.findall(regex,u)
            prefix1 = prefix11[0].replace('m','')
            regex = r'[\d]+[s]'
            prefix22 = re.findall(regex,u)
            prefix2 = prefix22[0].replace('s','')
            minutes += float(prefix1)
            seconds += float(prefix2)
            print("Adding the calculated from: ",u)
            print('current balance total minutes: ',minutes,'Total seconds :',seconds)
            tasks.append(u)
            if seconds > 60.0:
                calculated_minutes = int(seconds) / 60
                minutes += calculated_minutes
                print('calculated_minutes: ',calculated_minutes,'\n')
                seconds = int(seconds) % 60
                print('calculated_seconds: ',seconds,'\n')
            if minutes > timer:
                with open(name+'.txt','a') as T:
                    days+=1
                    print('Adding Task to',name,'.txt')
                    T.write('Day #'+str(days)+' :'+'\n\n\n')
                    for j in tasks:
                        tcount += 1
                        print('Adding: ',tcount,'. ',j,' To the file')
                        T.write(str(tcount)+'.'+j+'\n')
                    T.write('total minutes: '+str(minutes)+'Total seconds :'+str(seconds)+'\n'+'\n'+'\n')
                    tasks = []
                    minutes = 0
                    print('total minutes: ',minutes,'Total seconds :',seconds)
else:
    while read != '-1':
        regex = r'[\d]+[m]'
        prefix11 = re.findall(regex,read)
        if prefix11!= []:
            prefix1 = prefix11[0].replace('m','')
        else:
            prefix1=0
            print('please no spaces. for 10 minutes write is as "10m" that applies for seconds')
        regex = r'[\d]+[s]'
        prefix22 = re.findall(regex,read)
        if prefix22 != []:
            prefix2 = prefix22[0].replace('s','')
        else:
            prefix2 = 0
        minutes += float(prefix1)
        seconds += float(prefix2)
        print("Adding the calculated from: ",read)
        print('current balance total minutes: ',minutes,'Total seconds :',seconds)
        tasks.append(read)
        if seconds > 60.0:
            calculated_minutes = int(seconds) / 60
            minutes += calculated_minutes
            print('calculated_minutes: ',calculated_minutes,'\n')
            seconds = int(seconds) % 60
            print('calculated_seconds: ',seconds,'\n')
        if minutes > timer:
            with open(name+'.txt','a') as T:
                days+=1
                print('Adding Task to',name,'.txt')
                T.write('Day #'+str(days)+' :'+'\n\n\n')
                for j in tasks:
                    tcount += 1
                    print('Adding: ',tcount,'. ',j,' To the file')
                    T.write(str(tcount)+'.'+j+'\n')
                T.write('total minutes: '+str(minutes)+'Total seconds :'+str(seconds)+'\n'+'\n'+'\n')
                tasks = []
                minutes = 0
                print('total minutes: ',minutes,'Total seconds :',seconds)
        read=input('please provide input (-1 to quit) \n')
print('bye!')
    
