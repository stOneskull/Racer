class U:
    '''the player'''

    def __repr__(self):
        return self.name

    def __init__(self, playername):

        self.name = playername

        self.D = {}         # dict of horsenum: horseinstance
        self.lanes = {}     # dict of lanenum: horseinstance
        self.racing = {}    # dict of lanenum: horsenum

        self.gamehorses = []    # list of horses in game
        self.possy = []         # list of racers in order of race position

        self.wait = 1       # 1 is normal speed or 0.5 is double speed
        self.money = 23     # starting dollars
        self.bets = 2

        self.numhorses, self.horses_per = 0, 0
        self.day, self.laps, self.betyet = 0, 0, 0
        self.clued, self.seggy, self.clues = 0, 0, 0
        self.met, self.bye, self.nexts = 0, 0, 0
        self.checker, self.ends, self.loadnum = 0, 0, 0

        self.horse_multi = 3 # multiplyer (* horses_per) for total horses

        self.doors = {
            1: 'bag', 2: 'guide', 3: 'bookie',
            4: 'garden', 5: 'track', 6: 'sleep',
            9: 'options'}
        self.flags = {
            'guide': 1, 'bookie': 1, 'garden': 0,
            'track': 0, 'sleep': 1, 'options': 1}
        self.meet = {
            1: ['May Lee', 0], 2: ['Wong', 0],
            3: ['Travis', 0], 4: ['Pauly', 0],
            5: ['Chang', 0]}
        self.bag = {
            'pillow': 1, 'comb': 1}

        self.someone = 'Hmm'
        self.meetnext = []
        self.ticket = {}
        self.today = 'Now'

    def saybag(self):
        '''prints out inventory'''
        print("\n        You own..\n")

        for thing, amount in self.bag.items():
            if amount < 1: continue
            amount = '' if amount == 1 else f'({amount})'
            print('                ', thing, amount)
        print('                              ',
            f'and ${self.money:.2f} cash')

    def saymoney(self):
        '''prints out player wallet value'''

        self.money = round(self.money, 2)
        print(f'\nYou have ${self.money:0.2f}')