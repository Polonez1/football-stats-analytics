select s.season,
    s.rank as 'rank',
    s.team_name,
    s.all_played as 'match_played',
    s.all_win as 'win',
    s.all_draw as 'draw',
    s.all_lose as 'lose',
    s.all_goals_for as 'GF',
    s.all_goals_against as 'GA',
    s.points,
    if(ls.team_name is null, True, False) as 'from_previous_league',
    s.description as 'standings',
    s.team_id,
    s.league_id,
    s.stats_id
from standings s
    left outer join (
        select team_id,
            team_name
        from standings
        where season = { season } - 1
    ) ls on s.team_id = ls.team_id
where s.season = { season };