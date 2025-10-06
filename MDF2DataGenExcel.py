# The Benot Data Generator can take an Excel file that has column names and possible values
# This will read properties from an MDF model and populate an Excel sheet with the properties
# And add PVs from CDEs where available.

import bento_mdf
import pandas as pd
import requests

def getSTSPVs(cdeid, cdeversion):
    # Returns a list of PVs for teh proivded CDE ID and version.  Returns None if no PVs exist.
    base_url = "https://sts.cancer.gov/v1/terms/"
    headers = {'accept': 'application/json'}
    url =  base_url+f"cde-pvs/{cdeid}/{cdeversion}/pvs"

    try:
        result = requests.get(url = url, headers = headers)
        
        if result.status_code == 200:
            pvlist = []
            # Need to do the parsing here
            cdejson = result.json()
            if type(cdejson['CDECode']) is list:
                for entry in cdejson['permissibleValues']:
                    for pventry in entry:
                        if len(pventry) > 0:
                         pvlist.append(pventry['value'])
            else:
                if len(cdejson['permissibleValues']) > 0:
                    for pv in cdejson['permissibleValues']:
                        print(pv)
                        pvlist.append(pv['value'])

        return pvlist
    except requests.exceptions.HTTPError as e:
        return ("HTTP Error: {e}")
    



def getCDEID(props, prop, verbose= 0):
    if verbose >= 2:
        print(f"getCDEID for Props: {props} and Prop: {prop}")
    if props[prop].concept is not None:
        workingterms = props[prop].concept.terms.values()
        for workingtermobj in workingterms:
            workingterm = workingtermobj.get_attr_dict()
            if verbose >= 3:
                print(f"Starting object: {workingtermobj}")
                print(f"Prop: {prop}\t\tWorkingterm:\n{workingterm}")
                print(f"geCDEID InfoL  Prop: {prop[1]}\tNode: {prop[0]}\tCDE: {workingterm['origin_id']}\t Ver: {workingterm['origin_version']}")
            return workingterm['origin_id'], workingterm['origin_version']
    else:
        return None, None
    





mdffiles = ['https://raw.githubusercontent.com/CBIIT/cds-model/refs/heads/9.0.1/model-desc/cds-model.yml','https://raw.githubusercontent.com/CBIIT/cds-model/refs/heads/9.0.1/model-desc/cds-model-props.yml']

mdf = bento_mdf.MDF(*mdffiles)
props = mdf.model.props

# Easiet thing to do is make a dictionary of properties:[permissible values]
final = {}

#Each prop is (node, property)
for prop in props:
    print(f"Prop: {prop}")
    cdeid, cdeversion = getCDEID(props, prop)
    if cdeid is not None:
        print(f"ID: {cdeid}\t Version: {cdeversion}")
        pvlist = getSTSPVs(cdeid, cdeversion)
        print(f"PVList: {pvlist}")
        if pvlist is None:
            final[prop[1]] = []
        else:
            final[prop[1]] = pvlist

#print(final)
# Once that's done, create a dataframe
df = pd.DataFrame(dict([(k, pd.Series(v)) for k,v in final.items()]))
xlfile = '/media/sf_VMShare/DataGenTest.xlsx'
df.to_excel(xlfile, index=False)