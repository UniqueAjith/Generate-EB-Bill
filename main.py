class ebill:
    def __init__(self,name,type,con_num,pre_read,curr_read):
        self.name = name
        self.type = type
        self.con_num = con_num
        self.pre_read = pre_read
        self.curr_read = curr_read
        
    def display(self):
        print("--------------------------------")
        print('TNEB Bill Receipt')
        print("--------------------------------")
        print('Consumer Number: {}'.format(self.con_num))
        print('Consumer Name: {}'.format(self.name))
        print('Type Of Connection: {}'.format(self.type))
        print('Current Reading: {}'.format(self.curr_read))
        print('Previous Reading: {}'.format(self.pre_read))
        print('Units Consumed: {}'.format(self.curr_read - self.pre_read))
        print('Bill Amount: {}'.format(self.calc_bill()))
    
    def calc_bill(self):
        units = self.curr_read - self.pre_read
        if self.type == "D" or self.type == "d":
            if(units<=100):
                bill = units * 0
            elif(units>100 and units<=200):
                bill = (units-100) * 2
            elif(units>200 and units<500):
                bill = ((units-400) * 2) + ((units-200) * 3)
            else:
                bill = (units - 100) * 7
        elif(self.type == 'C' or self.type == 'c'):
            if(units<=100):
                bill = units * 1
            elif(units>100 and units<=200):
                bill = (units-100) * 3
            elif(units>200 and units<500):
                bill = ((units-400) * 3) + ((units-200) * 4)
            else:
                bill = (units - 100) * 10
        else:
            print("Invalid type")
        return bill
    
         
if __name__ == '__main__':
    print('Enter Consumer Name:')
    name = input()
    print('Enter Type Of Connection (D for Domestic Or C for Commercial):')
    type = input()
    print('Enter Consumer Number:')
    con_num = int(input())
    print('Enter Previous Reading:')
    pre_read = float(input())     
    print('Enter Current Reading:')
    curr_read = float(input()) 
    
    ebill_obj = ebill(name,type,con_num,pre_read,curr_read)
    ebill_obj.display()
    