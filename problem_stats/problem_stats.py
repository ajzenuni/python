import requests, json, io
import pandas as pd
import constant as const
import sys

def problemStats(url, token, relativeTime, tags):
    param = {"Api-Token": token, "relativeTime":relativeTime, "tag":tags}
    finalList = {"Entity Name":[],const.MTTR:[],const.MTBF:[], "Number of Problems": []}
    
    tagStr = " "
    tagStr = tagStr.join(tags).replace(":","_").replace(" ","_")

    problemResponse = requests.get('{url}/api/v1/problem/feed'.format(url=url), params=param)
    problemList = problemResponse.json()
    
    organizedProblemList = organizeProblemList(problemList["result"]["problems"])
    meanTimeToResolveProblem(organizedProblemList, finalList)
    meanTimeBetweenProblems(organizedProblemList, finalList)


    df = pd.DataFrame.from_dict(finalList)
    df.to_csv('{tag}_stats.csv'.format(tag=tagStr), index=False)

def getTime(e):
    return e["startTime"]

def organizeProblemList(problemList):
    organizedProblemList = {}
    problemList.sort(key=getTime)

    for problem in problemList:
        name = problem["rankedImpacts"][0]["entityName"]
        if(problem["status"] == "CLOSED"):
            try:
                organizedProblemList[name]["startTime"].append(problem["startTime"])
                organizedProblemList[name]["endTime"].append(problem["endTime"])
                organizedProblemList[name]["problemTime"].append((problem["endTime"] - problem["startTime"])/60000)
            except:
                organizedProblemList[name] = {}
                organizedProblemList[name]["startTime"] = []
                organizedProblemList[name]["startTime"].append(problem["startTime"])
                organizedProblemList[name]["endTime"] = []
                organizedProblemList[name]["endTime"].append(problem["endTime"])
                organizedProblemList[name]["problemTime"] = []
                organizedProblemList[name]["problemTime"].append((problem["endTime"] - problem["startTime"])/60000)
    
    return organizedProblemList

def meanTimeBetweenProblems(plist, finalList):
    for entity in plist:
        count = len(plist[entity]["problemTime"])
        if(count == 1):
            finalList[const.MTBF].append(0)
            finalList["Number of Problems"].append(1)
        else:
            x = 0
            temp = []
            while(x < count - 1):
                temp.append((plist[entity]["startTime"][x+1] - plist[entity]["endTime"][x])/60000)
                x += 1
            finalList[const.MTBF].append('{mean}'.format(mean = pd.DataFrame(temp).mean(axis=0)[0].round(2)))
            finalList["Number of Problems"].append(count)
def meanTimeToResolveProblem(plist, finalList):
    for entity in plist:
        finalList["Entity Name"].append(entity)
        finalList[const.MTTR].append('{mean}'.format(mean = pd.DataFrame(plist[entity]["problemTime"]).mean(axis=0)[0].round(2)))

def getFileJSON(fileName):
    fileObj = io.open(fileName, mode="r", encoding="utf-8")
    fileJSON = json.loads(fileObj.read())
    fileObj.close()
    return fileJSON

if __name__ == "__main__":
    params = getFileJSON("params.json")
    if (params["url"]=="" or params["token"]=="" ):
        print("Please fill out the required details in the params.json", file=sys.stderr)
    else:
        problemStats(params["url"], params["token"], params["relativeTime"], params["tags"])
