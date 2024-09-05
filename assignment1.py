def time_it(fn, args, repetitons= 1, **kwargs):
    current_time = datetime.now();
    for i in range(repetitons):
        fn(args,**kwargs)
    completed_time = datetime.now();
    time_difference=completed_time-current_time;
    print("total time",time_difference)
    print("average time",time_difference/repetitons)

def squared_power_list(power,args):
    li1=[];
    for i in args:
        li1.append(i**power)
    print(li1)

time_it(squared_power_list, 2, start=0,end= 5,repetitons=5)

