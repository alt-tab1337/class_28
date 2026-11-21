# Findings: Student Scores
## Question
What is the final result for the season
## Data
An imperfect comma seperated value spreadsheet containing the 20 Premier League teams for this season and their final results
mean.
## Cleaning
Arsenal was duplicated, some values in the played, games_won and games_drew fields were missing, and some teams were stated to have played more than 38 games
I removed the duplicate, made all games_played totals 38, and fixed the NaN values since they can be calculated with the existing values (since games played will always be 38 at the start of the season, so the games won, drew and lost can be calculated as long as 2 of the 3 are known.)
## Findings
1. Arsenal has won the Title.
2. Leicester, Ipswich, and Coventry have been relegated
3. Arsenal, Manchester City, Liverpool and Newcastle have achieved Champions League spots.
4. Chelsea qualified for the Europa League
5. Tottenham qualified for the Conference League
## Limits
Some of the games played, won, drew and lost values may be innacurate.
## Next steps
None.