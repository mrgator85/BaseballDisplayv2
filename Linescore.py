import BaseballData

class Linescore(object):
    def __init__(self, gamePk):
        self.baseball = BaseballData()
        self.gamePk = gamePk
        self.line_dict = self.baseball.get_linescore_data(gamePk)
        self.game_dict = self.baseball.get_game_data(gamePk)[0]
        self.status = self.game_dict['status']
    def getGameStatus(self):
        return self.status

    def getSnippet(sefl):
        """Snippet is either the WP and LP or the Probables if
        game is either complete or hasnt started.  In progress would be 
        current batter and current pitcher"""
        if(self.status == "Final"):
            return f"WP: {self.game_dict['winning_pitcher']}, LP: {self.game_dict['losing_pitcher']}"
        elif(self.status == "Preview"):
            return f"{self.game_dict['away_probable_pitcher']} @ {self.game_dict['home_probable_pitcher']}"
        elif(self.status == "In Progress"):
            return f"Pitching: {self.line_dict['defense']['pitcher']['fullName']} -- Batting: {self.line_dict['offense']['batting']['fullName']}"
        else:
            return f"{self.status} not handled"
    def getNumInnings(self):
        return len(self.line_dict['innings'].keys())

    def getVisitingHits(self):
        return [x['away']['runs'] for x in self.line_dict['innings']]
    
    def getHomeHits(self):
        return [x['home']['runs'] for x in self.line_dict['innings']]
    
    def getHomeSummary(self):
        h = self.line_dict['teams']['home']
        return (h['runs'], h['hits'], h['errors'])

    def getVisitingSummary(self):
        h = self.line_dict['teams']['away']
        return (h['runs'], h['hits'], h['errors'])