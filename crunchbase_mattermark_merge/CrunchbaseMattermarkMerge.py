"""
Merging Crunchbase and Mattermark Data
While both crunchbase and mattermark each have a wealth of data, there are discrepencies in the information they hold. Particularly, crunchbase has more information pertaining to founders and investors. We are able to merge the two datasets by pattern matching on the urls and names of the companies, merging into a single CSV of 70+ cols. This is with the current free/limited crunchbase access we have, with increased access, we can have additional cols and more information. These features should allow us to perform a complex regression.
"""


import pandas as pd

mm = pd.read_csv('Mattermark.csv')
cb = pd.read_csv('crunchbase/organizations.csv')
ppl = pd.read_csv('crunchbase/people.csv')
url2name = dict()

for i in cb.iterrows():
    url2name[i[1][5]] = [i[1][4][i[1][4].rfind('/')+1:i[1][4].find('?')], i[1].values, []]

for i in ppl.iterrows():
    if i[1][12] == i[1][12] and i[1][14] == i[1][14]:
        if i[1][14] in url2name:
            url2name[i[1][14]][2].append(i[1][2] + " " + i[1][3] + " - " + i[1][12])
    
rows = [["CrunchBase Name","Name","Website","Description","Growth Score","Mindshare Score","Weekly Momentum","Employee Count","Employee Count Last Month","Employees Added This Month","Employee Growth Last Mo","Employee Count 6 Months Ago","Employees Added Last 6 Months","Employee Growth Last 6 Months","Est. Monthly Uniques","Est. Monthly Uniques Week Ago","Monthly Uniques Week Over Week Growth","Est. Monthly Uniques Month Ago","Monthly Uniques Month Over Month Growth","Est. Mobile Downloads","Est. Monthly Mobile Downloads Week Ago","Monthly Mobile Downloads Week Over Week Growth","Est. Monthly Mobile Downloads Month Ago","Monthly Mobile Downloads Month Over Month Growth","Months Since Last Funding","Employees Added Since Last Funding","New Person Months Since Last Funding","New Funding Employee Growth","Founded","Stage","Investors","Total Funding","Last Funding","Last Funding Amount","Location","City","Region","State","Country","Continent","Business Models","Industries","Interested","Alert","Custom List","Public List","Keywords","Has Mobile App","Has Google Play App","Has iTunes App","Date Added", "crunchbase_uuid","type","primary_role","name","crunchbase_url","homepage_domain","homepage_url","profile_image_url","facebook_url","twitter_url","linkedin_url","stock_symbol","location_city","location_region","location_country_code","short_description", "people"]]

for i in mm.iterrows():
    if i[1][1] in url2name:
        rows.append([url2name[i[1][1]][0]] + i[1].tolist() + url2name[i[1][1]][1].tolist() + [", ".join(url2name[i[1][1]][2])])

out = pd.DataFrame.from_records(rows)
out.to_csv('CrunchbaseMattermarkMerge.csv')
