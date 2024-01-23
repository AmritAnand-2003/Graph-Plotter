from django.shortcuts import render
from django.http import HttpResponse
from .models import matches, school
# Create your views here.

def front(request):
    return render(request, "match/front.html")

def matchq1(request):
    mlist = matches.objects.all()
    matchCount = {}
    for  match in mlist:
        if match.season not in matchCount:
            matchCount[match.season] = 1
        else:
            matchCount[match.season] += 1
    # print(matchCount)
    season = list(matchCount.keys())
    count = list(matchCount.values())
    new_var = {"matchCount": matchCount, "season": season, "count": count}
    return render(request, "match/q2plot1.html", new_var)
    # output = ", ".join([(q.season, q.winner) for q in list])
    # return HttpResponse(output)
    # return HttpResponse("Hello guys, You are going to see IPL statistics.")

def schoolq1(request):
    tempData = school.objects.values('district')
    print(tempData)
    schoolCount = {}
    for x in tempData:
        t = x['district']
        if t not in schoolCount:
            schoolCount[t] = 1
        else:
            schoolCount[t] += 1
    dist = list(schoolCount.keys())
    count = list(schoolCount.values())
    new_var = {"dist": dist, "count": count}
    return render(request, "match/q1plot1.html", new_var)

def schoolq2(request):
    distCatCount = {}
    tempData = school.objects.values('district', 'category')
    for x in tempData:
        d = x['district']
        c = x['category']
        if d not in distCatCount:
            distCatCount[d] = {}
        if c not in distCatCount[d]:
            distCatCount[d][c] = 1
        else:
            distCatCount[d][c] += 1
    return render(request, "match/q1plot2.html", {"distCatCount": distCatCount})

def schoolq3(request):
        distLanCount = {}
        tempData = school.objects.values('district', 'language')
        for x in tempData:
            d = x['district']
            l = x['language']
            if d not in distLanCount:
                distLanCount[d] = {}
            if l not in distLanCount[d]:
                distLanCount[d][l] = 1
            else:
                distLanCount[d][l] += 1
        return render(request, "match/q1plot3.html", {"distLanCount": distLanCount})

def matchq2(request):
    sessTeamWon = {}
    tempData = matches.objects.values('season', 'winner')
    for x in tempData:
        s = x['season']
        w = x['winner']
        if s not in sessTeamWon:
            sessTeamWon[s] = {}
        if w not in sessTeamWon[s]:
            sessTeamWon[s][w] = 1
        else:
            sessTeamWon[s][w] += 1
    return render(request, "match/q2plot2.html", {"sessTeamWon": sessTeamWon})
