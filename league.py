# import python packages
import pandas as pd
from iteround import saferound
# import truncted norm form scipy
from scipy.stats import truncnorm

# truncated norm function https://stackoverflow.com/a/44308018
def get_truncated_normal(mean=0, sd=1, low=0, upp=10):
    return truncnorm(
        (low - mean) / sd, (upp - mean) / sd, loc=mean, scale=sd)

# imported csv 
pl = pd.read_csv("league_table.csv", index_col="Team", names=["Team", "Home(F)", "Home(A)", "Points(H)", "Away(F)", "Away(A)", "Points(A)" ]);

pl_ran = pd.read_csv("league_table_blank.csv", index_col="Team", names=["Team", "Home(F)", "Home(A)", "Away(F)", "Away(A)"]);

def homeGoalsFor():
    pl["Home(Dif)"] = pl["Home(F)"] - pl["Home(A)"]
    # created league table based on home form
    home = pl[["Home(F)", "Home(A)", "Home(Dif)", "Points(H)"]];
    pl_ran = pd.read_csv("league_table_blank.csv", index_col="Team", names=["Team", "Home(F)", "Home(A)", "Away(F)", "Away(A)"]);
    
    home = home.sort_values(by = "Team");
    # array of home team's goals scored 
    home_ac = home["Home(F)"];
    # divided goals by number of games 
    home_ac = np.divide(home_ac, 19);
    # divided by average of goal per game and multiplied by average goals 
    home_ac = (np.divide(home_ac, 1.57))*29.8;
    #generated home values and added to dataset
    pl_ran["Home(F)"] = np.random.poisson(lam=home_ac, size=(20));
    
    # added new column with away goal difference
    pl["Away(Dif)"] = pl["Away(F)"] - pl["Away(A)"];
    away = pl[["Away(F)", "Away(A)", "Away(Dif)", "Points(A)"]];
    
    away = away.sort_values(by = "Team");
    # array containing number of goals each team conceded in the previous season
    away_dc = away["Away(A)"];
    # divided contents of array by number of games played  
    away_dc = np.divide(away_dc, 19);
    # divided contents of array by average goals conceded per match and multiplied by average goals 
    away_dc = (np.divide(away_dc, 1.57))*29.8;
    
    # total home goals scored 
    thf = pl_ran["Home(F)"].sum();
    # generated random goals conceded data for each team
    awa = np.random.poisson(lam=away_dc, size=(20))
    # calculated sum of random array
    awasum = awa.sum();
    # divide array by its sum 
    awa = np.divide(awa, awasum);
    # multiplied by sum of total goals scored at home 
    awa = awa*thf;
    # round floats to integers while maintaining sum
    awa = saferound(awa, places=0);
    # converted list to array 
    awa = np.asarray(awa);
    # converted type from float to array 
    awa = awa.astype(int);
    # added new column to data frame of goals conceded away from home 
    pl_ran["Away(A)"] = awa;
    
    return pl_ran[["Home(F)", "Away(A)"]]

def homeGoalsAgainst():
    # created league table based on home form
    home = pl[["Home(F)", "Home(A)", "Home(Dif)", "Points(H)"]];
    pl_ran = pd.read_csv("league_table_blank.csv", index_col="Team", names=["Team", "Home(F)", "Home(A)", "Away(F)", "Away(A)"]);
    
    # real world values of goals conceded by teams at home
    home = home.sort_values(by = "Team");
    # array of goals conceded by home teams
    home_dc = home["Home(A)"];
    # divided goals by number of games 
    home_dc = np.divide(home_dc, 19);
    # divided by average goals per game and multiplied by average goals conceded at home
    home_dc = (np.divide(home_dc, 1.25))*23.8;
    # added goals conceded at home to dataframe 
    pl_ran["Home(A)"] = np.random.poisson(lam=home_dc, size=(20));
    
     # created league table based on home form
    away = pl[["Away(F)", "Away(A)", "Away(Dif)", "Points(A)"]];
    
    # real world values of goals scored by away teams
    away = away.sort_values(by = "Team");
    
    # away team attacking coefficient in alphabetical order
    away_ac = away["Away(F)"];
    away_ac = np.divide(away_ac, 19);
    away_ac = (np.divide(away_ac, 1.25))*23.8;
    
    # total home goals conceded 
    tha = pl_ran["Home(A)"].sum();
    # generated random goals scored data for each team
    awf = np.random.poisson(lam=away_ac, size=(20));
    # calculated sum of random array
    awfsum = awf.sum();
    # divide array by its sum 
    awf = np.divide(awf, awfsum);
    # multiplied by sum of total goals conceded at home 
    awf = awf*tha;
    # round floats to integers while maintaining sum
    awf = saferound(awf, places=0);
    # converted list to array 
    awf = np.asarray(awf);
    # converted type from float to array 
    awf = awf.astype(int);
    # added new column to array of goals scored away from home
    pl_ran["Away(F)"] = awf;
    
    return pl_ran[["Home(A)", "Away(F)"]]

pl_ran[["Home(F)", "Away(A)"]] = homeGoalsFor();
pl_ran[["Home(A)", "Away(F)"]] = homeGoalsAgainst();
pl_ran["Home(Dif)"] = pl_ran["Home(F)"] - pl_ran["Home(A)"];
pl_ran["Away(Dif)"] = pl_ran["Away(F)"] - pl_ran["Away(A)"];

def homePoints():
    pl_ran = pd.read_csv("league_table_blank.csv", index_col="Team", names=["Team", "Home(F)", "Home(A)", "Away(F)", "Away(A)"]);
    pl_ran["Home(Dif)"] = pl_ran["Home(F)"] - pl_ran["Home(A)"];
    # truncated normal distribution from scipy 
    hp = get_truncated_normal(mean=30.7, sd=11.49, low=0, upp=57)
    hp = hp.rvs(20);
    # rounded results to whole number
    np.rint(hp);
    # converted type to integer
    hp = hp.astype(int);
    # sorted from lowest to highest
    hp.sort();
    # added home points column to data frame

    return hp

pl_ran = pl_ran.sort_values(by = "Home(Dif)");
pl_ran["Points(H)"] = homePoints()

def awayPoints():
    pl_ran = pd.read_csv("league_table_blank.csv", index_col="Team", names=["Team", "Home(F)", "Home(A)", "Away(F)", "Away(A)"]);
    pl_ran["Away(Dif)"] = pl_ran["Away(F)"] - pl_ran["Away(A)"];
    # truncated normal distribution from scipy 
    ap = get_truncated_normal(mean=22.75, sd=10.36, low=0, upp=57)
    ap = ap.rvs(20);
    # rounded results to whole number
    ap = np.rint(ap);
    # converted type to integer
    ap = ap.astype(int);
    ap.sort();
    
    return ap

# added away away goals to dataframe
pl_ran = pl_ran.sort_values(by = "Away(Dif)");
pl_ran["Points(A)"] = awayPoints()

#added total values to datafram
pl_ran["Total(F)"] = pl_ran["Home(F)"] + pl_ran["Away(F)"];
pl_ran["Total(A)"] = pl_ran["Home(A)"] + pl_ran["Away(A)"];
pl_ran["Total(Dif)"] = pl_ran["Total(F)"] - pl_ran["Total(A)"];
pl_ran["Total(P)"] = pl_ran["Points(H)"] + pl_ran["Points(A)"];

# dataframe of total values
total_ran = pl_ran[["Total(F)", "Total(A)", "Total(Dif)", "Total(P)"]];

# sort by highest points
total_ran = total_ran.sort_values(by = "Total(P)", ascending=False);
