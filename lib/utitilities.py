import random


class DiceThrower:
    # smiður klasans skilgreinir klasabreyturnar number_of_dice og dice_list.
    # Þar að auki er listinn dice_list frumstilltur með -1 fyrir hvern "tening".
    # Hver teningur er svo bara eitt hólf í listanum.
    # Ástæða þess að listinn er frumstilltur er sú að forrit sem notar klasann
    # getur "séð" hvort búið er að "kasta" teningnum eða ekki!
    # Heildarfjöldi teninga er ákvarðaður af notanda, en sett á 5 gefi notandinn
    # ekki upp hve marga teninga á að nota.
    def __init__(self, how_many=5):
        self.number_of_dice = how_many
        self.dice_list = [-1 for i in range(self.number_of_dice)]

    # throw() fallið í þessum klasa kastar ÖLLUM teningum sem á að nota
    # það er gert í lúppu sem kallar á throw() fallið í klasanum Dice()
    def throw(self):
        for x in range(0, self.number_of_dice):
            self.dice_list[x] = random.randint(1, 6)
        return self.dice_list

    # þetta fall() er notað til að kasta aftur þeim teningum sem spilarinn óskar.
    # fallið þarf að fá index af þeim teningum sem kasta á aftur(rethrow_list)
    # til dæmis ef spilarinn vill kasta aftur teningum 1 og 3 þá setur hann
    # 0 og 2 í rethrow listann og sendir inn sem færibreytu.
    def rethrow(self, rethrow_list=()):
        if 0 < len(rethrow_list) <= self.number_of_dice:
            if min(rethrow_list) >= 0 and max(rethrow_list) <= self.number_of_dice - 1:
                for item in rethrow_list:
                    self.dice_list[item] = random.randint(1, 6)
            return self.dice_list
        else:
            return self.throw()
