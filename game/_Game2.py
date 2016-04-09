from goldsberry._masterclass import *
from goldsberry._apiparams import *


class boxscore_advanced(NbaDataProvider):
    def __init__(self, gameid):
        NbaDataProvider.__init__(self)
        self.set_default_api_parameters(GameID=gameid, **p_game_bs)
        self._url_modifier = 'boxscoreadvancedv2'
        self._set_class_data()

    def player_stats(self):
        return self.get_table_from_data(self.data_tables, 0)

    def team_stats(self):
        return self.get_table_from_data(self.data_tables, 1)


class boxscore_fourfactors(NbaDataProvider):
    def __init__(self, gameid):
        NbaDataProvider.__init__(self)
        self.set_default_api_parameters(GameID=gameid, **p_game_bs)
        self._url_modifier = 'boxscorefourfactorsv2'
        self._set_class_data()

    def player_stats(self):
        return self.get_table_from_data(self.data_tables, 0)

    def team_stats(self):
        return self.get_table_from_data(self.data_tables, 1)


class boxscore_miscellaneous(NbaDataProvider):
    def __init__(self, gameid):
        NbaDataProvider.__init__(self)
        self.set_default_api_parameters(GameID=gameid, **p_game_bs)
        self._url_modifier = 'boxscoremiscv2'
        self._set_class_data()

    def player_stats(self):
        return self.get_table_from_data(self.data_tables, 0)

    def team_stats(self):
        return self.get_table_from_data(self.data_tables, 1)


class boxscore_scoring(NbaDataProvider):
    def __init__(self, gameid):
        NbaDataProvider.__init__(self)
        self.set_default_api_parameters(GameID=gameid, **p_base)
        self._url_modifier = 'boxscorescoringv2'
        self._set_class_data()

    def player_stats(self):
        return self.get_table_from_data(self.data_tables, 0)

    def team_stats(self):
        return self.get_table_from_data(self.data_tables, 1)


class boxscore_summary(NbaDataProvider):
    def __init__(self, gameid):
        NbaDataProvider.__init__(self)
        self.set_default_api_parameters(GameID=gameid)
        self._url_modifier = 'boxscoresummaryv2'
        self._set_class_data()

    def game_summary(self):
        return self.get_table_from_data(self.data_tables, 0)

    def other_stats(self):
        return self.get_table_from_data(self.data_tables, 1)

    def officials(self):
        return self.get_table_from_data(self.data_tables, 2)

    def inactive_players(self):
        return self.get_table_from_data(self.data_tables, 3)

    def game_info(self):
        return self.get_table_from_data(self.data_tables, 4)

    def line_score(self):
        return self.get_table_from_data(self.data_tables, 5)

    def last_meeting(self):
        return self.get_table_from_data(self.data_tables, 6)

    def season_series(self):
        return self.get_table_from_data(self.data_tables, 7)

    def _available_video(self):
        return self.get_table_from_data(self.data_tables, 8)


class boxscore_tracking(NbaDataProvider):
    def __init__(self, gameid):
        NbaDataProvider.__init__(self)
        self.set_default_api_parameters(GameID=gameid)
        self._url_modifier = 'boxscoreplayertrackv2'
        self._set_class_data()

    def player_stats(self):
        return self.get_table_from_data(self.data_tables, 0)

    def team_stats(self):
        return self.get_table_from_data(self.data_tables, 1)


class boxscore_traditional(NbaDataProvider):
    def __init__(self, gameid):
        NbaDataProvider.__init__(self)
        self.set_default_api_parameters(GameID=gameid, **p_game_bs)
        self._url_modifier = 'boxscoretraditionalv2'
        self._set_class_data()

    def player_stats(self):
        return self.get_table_from_data(self.data_tables, 0)

    def team_stats(self):
        return self.get_table_from_data(self.data_tables, 1)


class boxscore_usage(NbaDataProvider):
    def __init__(self, gameid):
        NbaDataProvider.__init__(self)
        self.set_default_api_parameters(GameID=gameid, **p_game_bs)
        self._url_modifier = 'boxscoreusagev2'
        self._set_class_data()

    def player_stats(self):
        return self.get_table_from_data(self.data_tables, 0)

    def team_stats(self):
        return self.get_table_from_data(self.data_tables, 1)


class play_by_play(NbaDataProvider):
    def __init__(self, gameid):
        NbaDataProvider.__init__(self)
        self.set_default_api_parameters(GameID=gameid, **p_game_pbp)
        self._url_modifier = 'playbyplayv2'
        self._set_class_data()

    def player_info(self):
        return self.get_table_from_data(self.data_tables, 0)

    def _available_video(self):
        return self.get_table_from_data(self.data_tables, 1)


# Courtesy of daniel.silvis@gmail.com
class GameIDs(NbaDataProvider):
    def __init__(self):
        NbaDataProvider.__init__(self)
        self.set_default_api_parameters(**p_game_ids)
        self._url_modifier = 'leaguegamelog'
        self._set_class_data()

    def game_list(self):
        return self.get_table_from_data(self.data_tables, 0)


__all__ = ['play_by_play', 'boxscore_summary', 'boxscore_traditional',
           'boxscore_advanced', 'boxscore_miscellaneous', 'boxscore_scoring',
           'boxscore_fourfactors', 'boxscore_usage', 'boxscore_tracking']
