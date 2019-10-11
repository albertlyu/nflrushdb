# Game constants
GAME_ID = 'GameId' # a unique game identifier
SEASON = 'Season' # year of the season
HOME_TEAM_ABBR = 'HomeTeamAbbr' # home team abbreviation
AWAY_TEAM_ABBR = 'VisitorTeamAbbr' # visitor team abbreviation
WEEK = 'Week' # week into the season
STADIUM = 'Stadium' # stadium where the game is being played
LOCATION = 'Location' # city where the game is being player
STADIUM_TYPE = 'StadiumType' # description of the stadium environment
TURF_DESCRIPTION = 'Turf' # description of the field surface
GAME_WEATHER = 'GameWeather' # description of the game weather
GAME_TEMPERATURE = 'Temperature' # temperature (deg F)
GAME_HUMIDITY = 'Humidity' # humidity
GAME_WIND_SPEED = 'WindSpeed' # wind speed in miles/hour
GAME_WIND_DIRECTION = 'WindDirection' # wind direction

GAME_CONSTANTS = [
    GAME_ID,
    SEASON,
    HOME_TEAM_ABBR,
    AWAY_TEAM_ABBR,
    WEEK,
    STADIUM,
    LOCATION,
    STADIUM_TYPE,
    TURF_DESCRIPTION,
    GAME_WEATHER,
    GAME_TEMPERATURE,
    GAME_HUMIDITY,
    GAME_WIND_SPEED,
    GAME_WIND_DIRECTION,
]

# Play constants
PLAY_ID = 'PlayId' # a unique play identifier
TEAM = 'Team' # home or away
YARD_LINE = 'YardLine' # the yard line of the line of scrimmage
QUARTER = 'Quarter' # game quarter (1-5, 5 == overtime)
GAME_CLOCK = 'GameClock' # time on the game clock
POSSESSION_TEAM = 'PossessionTeam' # team with possession
DOWN = 'Down' # the down (1-4)
DISTANCE_UNTIL_FIRST_DOWN = 'Distance' # yards needed for a first down
FIELD_POSITION = 'FieldPosition' # which side of the field the play is happening on
HOME_SCORE_BEFORE_PLAY = 'HomeScoreBeforePlay' # home team score before play started
AWAY_SCORE_BEFORE_PLAY = 'VisitorScoreBeforePlay' # visitor team score before play started
RUSHER_PLAYER_ID = 'NflIdRusher' # the NflId of the rushing player
OFFENSIVE_FORMATION = 'OffenseFormation' # offense formation
OFFENSE_PERSONNEL = 'OffensePersonnel' # offensive team positional grouping
DEFENDERS_IN_THE_BOX = 'DefendersInTheBox' # number of defenders lined up near the line of scrimmage, spanning the width of the offensive line
DEFENSE_PERSONNEL = 'DefensePersonnel' # defensive team positional grouping
PLAY_DIRECTION = 'PlayDirection' # direction the play is headed
TIME_HANDOFF = 'TimeHandoff' # UTC time of the handoff
TIME_SNAP = 'TimeSnap' # UTC time of the snap
YARDS_GAINED = 'Yards' # the yardage gained on the play (you are predicting this)

PLAY_CONSTANTS = [
    GAME_ID,
    PLAY_ID,
    TEAM,
    YARD_LINE,
    QUARTER,
    GAME_CLOCK,
    POSSESSION_TEAM,
    DOWN,
    DISTANCE_UNTIL_FIRST_DOWN,
    FIELD_POSITION,
    HOME_SCORE_BEFORE_PLAY,
    AWAY_SCORE_BEFORE_PLAY,
    RUSHER_PLAYER_ID,
    OFFENSIVE_FORMATION,
    OFFENSE_PERSONNEL,
    DEFENDERS_IN_THE_BOX,
    DEFENSE_PERSONNEL,
    PLAY_DIRECTION,
    TIME_HANDOFF,
    TIME_SNAP,
    YARDS_GAINED,
]

# Positional constants
POSITIONAL_X = 'X' # player position along the long axis of the field. See figure below.
POSITIONAL_Y = 'Y' # player position along the short axis of the field. See figure below.
POSITIONAL_SPEED = 'S' # speed in yards/second
POSITIONAL_ACCELERATION = 'A' # acceleration in yards/second^2
POSITIONAL_DISTANCE = 'Dis' # distance traveled from prior time point, in yards
POSITIONAL_ORIENTATION = 'Orientation' # orientation of player (deg)
POSITIONAL_ANGLE = 'Dir' # angle of player motion (deg)
PLAYER_ID = 'NflId' # a unique identifier of the player
PLAYER_NAME = 'DisplayName' # player's name
PLAYER_JERSEY_NUMBER = 'JerseyNumber' # jersey number
PLAYER_HEIGHT = 'PlayerHeight' # player height (ft-in)
PLAYER_WEIGHT = 'PlayerWeight' # player weight (lbs)
PLAYER_BIRTH_DATE = 'PlayerBirthDate' # birth date (mm/dd/yyyy)
PLAYER_COLLEGE_NAME = 'PlayerCollegeName' # where the player attended college
PLAYER_POSITION = 'Position' # player's position

POSITIONAL_CONSTANTS = [
    POSITIONAL_X,
    POSITIONAL_Y,
    POSITIONAL_SPEED,
    POSITIONAL_ACCELERATION,
    POSITIONAL_DISTANCE,
    POSITIONAL_ORIENTATION,
    POSITIONAL_ANGLE,
    PLAYER_ID,
    PLAYER_NAME,
    PLAYER_JERSEY_NUMBER,
    PLAYER_HEIGHT,
    PLAYER_WEIGHT,
    PLAYER_BIRTH_DATE,
    PLAYER_COLLEGE_NAME,
    PLAYER_POSITION,
]
