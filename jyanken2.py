import numpy as np

win=0
drow=0
lose=0

try:
    count=input('何回戦しますか？')
    for n in range(int(count)):
        player=int(input('じゃんけんぽん！\n グー＝0,チョキ＝1,パー＝2'))

        NPC=np.random.randint(2)
        if NPC==0:
            NPChand='グー'
        elif NPC==1:
            NPChand='チョキ'
        elif NPC==2:
            NPChand='パー'
        print('相手の手は',NPChand,'でした')

        if player==NPC:
            print('あいこ')
            point=1
        elif player==0:
            if NPC==1:
                print('勝ち！')
                point=2
            elif NPC==2:
                print('負け…')
                point=0
        elif player==1:
            if NPC==0:
                print('負け…')
                point=0
            elif NPC==2:
                print('勝ち！')
                point=2
        elif player==2:
            if NPC==0:
                print('勝ち！')
                point=2
            elif NPC==1:
                print('負け…')
                point=0

        if point==2:
            win=win+1
        elif point==1:
            drow=drow+1
        elif point==0:
            lose=lose+1

    print(str((count)+'回戦中'))
    print(str(win)+'回勝利！')

    per=int(win)/int(count)*100
    print('勝率は'+str(int(per))+'％')

except ValueError:
    print('入力ミスかな…？')
