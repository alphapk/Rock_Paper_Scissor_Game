import random
print("---------ROCK, PAPER, SCISSORS GAME-----------")
choice =['1','2','3']
l=[]
t_machine=0
t_human=0
     

while True:
    try:
        human_ip = input("Enter any one option (1 or 2 or 3 or 4) " + "1. Rock, 2. Paper,3. Scissor, 4. Exit\n")
        human_ip=str(human_ip)
        if(human_ip== '4'):
            print('                                                      ')
            print('          ***************************************************')
            print('                             SCORE BOARD                 ')            
            print('          ***************************************************')
            print('                    Machine      Human      Ties')
            n = max(len(str(x)) for j in l for x in j)

            for row in l:
                print('                       ',''.join(str(x).ljust(n + 10) for x in row))
                print('                                                      ')
               
            if t_machine > t_human:
                print('Machine wins with the point :',t_machine)
            else:
                print('Human wins with the point : ',t_human)
            break
       
       
        #print(human_ip)
        comp_ip = random.sample(choice,k=1)
        comp_ip=str(comp_ip[0])
        vals=['','Rock','Paper','Scissor','Exit']
        print('Human input is : ', vals[int(human_ip)])
        print('Computer input is : ', vals[int(comp_ip)])
        h_scr=0
        m_scr=0
        ties=0

        print('Result: ')
        if(human_ip == comp_ip):
            print("Tie")
            ties=ties+1
        if(human_ip == '1' and comp_ip == '2'):
            m_scr=m_scr+1
            print("Computer Won")
        elif(human_ip == '2' and comp_ip == '3'):
            m_scr=m_scr+1
            print("Computer Won")
        elif(human_ip == '3' and comp_ip == '1'):
            m_scr=m_scr+1
            print("Computer Won")
        elif(human_ip == '2' and comp_ip == '1'):
            h_scr=h_scr+1
            print("You won")
        elif(human_ip == '3' and comp_ip == '2'):
            h_scr=h_scr+1
            print("You Won")
        elif(human_ip == '1' and comp_ip == '3'):
            h_scr=h_scr+1
            print("You Won")
        l.append([m_scr, h_scr, ties])
        t_machine=t_machine+m_scr
        t_human=t_human+h_scr
        print('Machine Score = ',m_scr,' : ', 'Your Score = ',h_scr)
           
       
    except (ValueError, IndexError) as e:
        print('Enter only 1 or 2 or 3 or 4')
