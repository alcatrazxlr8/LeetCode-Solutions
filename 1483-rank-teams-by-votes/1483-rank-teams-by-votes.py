class Solution:
    def rankTeams(self, votes: List[str]) -> str:
            teams = list(votes[0])
            numTeams = len(teams)
            # ranks = [[0 for _ in range(numTeams)] for _ in range(numTeams)] 
            ranks = {team: [0]* numTeams for team in votes[0]}
            
            for vote in votes:
                for rank, team in enumerate(vote):
                    ranks[team][rank] += 1
            sortedTeams = sorted(votes[0], key=lambda team:(ranks[team], -ord(team)), reverse=True)
            return "".join(sortedTeams)