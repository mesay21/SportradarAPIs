# Sportradar APIs
# Copyright 2018 John W. Miller
# See LICENSE for details.

from sportradar.api import API


class NHL(API):

    def __init__(self,
                 api_key,
                 access_level='trial',
                 language='en',
                 version=7,
                 format_='json',
                 timeout=5,
                 sleep_time=1.5):
        super().__init__(api_key, format_, timeout, sleep_time)
        self.access_level = access_level
        self.language = language
        self.version = version
        self.prefix = f"nhl/{self.access_level}/v{self.version}/{self.language}"

    def get_daily_change_log(self, year, month, day):
        """provides information on any changes made to teams, players, game statistics,
            and standings
        """
        path = "{prefix}/league/{year:4d}/{month:02d}/{day:02d}/changes".format(
            prefix=self.prefix, year=year, month=month, day=day)
        print(path)
        return self._make_request(path)

    def get_daily_schedule(self, year, month, day):
        """provides the schedule for a given day"""
        path = "{prefix}/games/{year:4d}/{month:02d}/{day:02d}/schedule".format(
            prefix=self.prefix, year=year, month=month, day=day)
        print(path)
        return self._make_request(path)

    def get_daily_transfers(self, year, month, day):
        """provides information on player transfers for a given day"""
        path = "{prefix}/league/{year:4d}/{month:02d}/{day:02d}/transfers".format(
            prefix=self.prefix, year=year, month=month, day=day)
        print(path)
        return self._make_request(path)

    def get_game_boxscore(self, game_id):
        """Get boxscore data for NHL Games"""
        path = f"{self.prefix}/games/{game_id}/boxscore"
        print(path)
        return self._make_request(path)

    def get_game_faceoffs(self, game_id):
        """Get faceoff data for an NHL Game"""
        path = f"{self.prefix}/games/{game_id}/faceoffs"
        print(path)
        return self._make_request(path)

    def get_game_play_by_play(self, game_id):
        """Get the Play-by-Play data for an NHL Game"""
        path = f"{self.prefix}/games/{game_id}/pbp"
        print(path)
        return self._make_request(path)

    def get_game_summary(self, game_id):
        """Get the Summary data for an NHL Game"""
        path = f"{self.prefix}/games/{game_id}/summary"
        print(path)
        return self._make_request(path)

    def get_game_time_on_ice(self, game_id):
        """Get the time on ice data for an NHL Game"""
        path = f"{self.prefix}/games/{game_id}/time_on_ice"
        print(path)
        return self._make_request(path)

    def get_injuries(self):
        """Provides updated injuries for the NHL"""
        path = f"{self.prefix}/league/injuries".format()
        print(path)
        return self._make_request(path)

    def get_league_hierarchy(self):
        """Provides list of all NHL teams"""
        path = f"{self.prefix}/league/hierarchy".format()
        print(path)
        return self._make_request(path)

    def get_league_leaders___goaltending(self, season_year, season_type):
        """Provides the leaders for Goaltending"""
        path = f"{self.prefix}/seasons/{season_year}/{season_type}/leaders/goaltending"
        print(path)
        return self._make_request(path)

    def get_league_leaders___skaters(self, season_year, season_type):
        """Provides the leaders for Defense and Offense skaters"""
        path = f"{self.prefix}/seasons/{season_year}/{season_type}/leaders/offense"
        print(path)
        return self._make_request(path)

    def get_league_leaders___daily(self, year1, nhl_season, year2, month, day):
        """Provides the leaders for a given day. Please note that this feed will not
            return data until the regular season begins
        """
        path = f"{self.prefix}/seasons/{year1}/{nhl_season}/{year2}/{month:02d}/{day:02d}/leaders".format(
            year1=year1, nhl_season=nhl_season, year2=year2, month=month, day=day)
        print(path)
        return self._make_request(path)

    def get_league_leaders___seasonal(self, season_year, season_type):
        """Provides the seasonal leaders. Please note that this feed will not return data
            until the regular season begins
        """
        path = f"{self.prefix}/seasons/{season_year}/{season_type}/leaders"
        print(path)
        return self._make_request(path)

    def get_player_profile(self, player_id):
        """Player information for the NHL"""
        path = f"{self.prefix}/players/{player_id}/profile".format(
            player_id=player_id)
        print(path)
        return self._make_request(path)

    def get_rankings(self, season_year, season_type):
        """Get ranking information for the NHL"""
        path = f"{self.prefix}/seasons/{season_year}/{season_type}/rankings"
        print(path)
        return self._make_request(path)

    def get_schedule(self, season_year, season_type):
        """Get the schedule for a given NHL Season"""
        path = f"{self.prefix}/games/{season_year}/{season_type}/schedule"
        print(path)
        return self._make_request(path)

    def get_seasonal_faceoffs(self, season, nhl_season, team_id):
        """Get faceoff information on a team level"""
        path = f"{self.prefix}/seasons/{season}/{nhl_season}/teams/{team_id}/faceoffs".format(
            season=season, nhl_season=nhl_season, team_id=team_id)
        print(path)
        return self._make_request(path)

    def get_seasonal_statistics___season_to_date(self, season, nhl_season, team_id):
        """Get statistics on a team level"""
        path = f"{self.prefix}/seasons/{season}/{nhl_season}/teams/{team_id}/statistics".format(
            season=season, nhl_season=nhl_season, team_id=team_id)
        print(path)
        return self._make_request(path)

    def get_series_faceoffs(self, series_id, team_id):
        """Get faceoff information for a playoff series"""
        path = f"{self.prefix}/series/{series_id}/teams/{team_id}/faceoffs".format(
            series_id=series_id, team_id=team_id)
        print(path)
        return self._make_request(path)

    def get_series_schedule(self, season, nhl_season):
        """Get faceoff information for a playoff series"""
        path = f"{self.prefix}/series/{season}/{nhl_season}/schedule".format(
            season=season, nhl_season=nhl_season)
        print(path)
        return self._make_request(path)

    def get_series_statistics(self, series_id, team_id):
        """Get the statistics for a playoff series"""
        path = f"{self.prefix}/series/{series_id}/teams/{team_id}/statistics".format(
            series_id=series_id, team_id=team_id)
        print(path)
        return self._make_request(path)

    def get_standings(self, season, nhl_season):
        """Get the standings for the NHL"""
        path = f"{self.prefix}/seasons/{season}/{nhl_season}/standings".format(
            season=season, nhl_season=nhl_season)
        print(path)
        return self._make_request(path)

    def get_team_leaders_daily(self, year1, nhl_season, year2, month, day, team_id):
        """Provides the leaders for a given day. Please note that this feed will not
            return data until the regular season begins
        """
        path = f"{self.prefix}/seasons/{year1}/{nhl_season}/{year2}/{month:02d}/{day:02d}/teams/{team_id}/leaders".format(
            year1=year1, nhl_season=nhl_season, year2=year2, month=month, day=day, team_id=team_id)
        print(path)
        return self._make_request(path)

    def get_team_leaders_seasonal(self, season, nhl_season, team_id):
        """Get leaders on a team level. Please note that this feed will not return data
            until the regular season begins
        """
        path = f"{self.prefix}/seasons/{season}/{nhl_season}/teams/{team_id}/leaders".format(
            season=season, nhl_season=nhl_season, team_id=team_id)
        print(path)
        return self._make_request(path)

    def get_team_profile_roster(self, team_id):
        """Get the roster information for a NHL team"""
        path = f"{self.prefix}/teams/{team_id}/profile".format(team_id=team_id)
        print(path)
        return self._make_request(path)

    def get_teams(self):
        """
        NHL Teams provides a complete list of active teams in the NHL API database..
        """
        path = f"{self.prefix}/league/teams"
        return self._make_request(path)
