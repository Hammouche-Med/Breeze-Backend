from datetime import datetime
import calendar
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from observation.models import Observation
from stations.models import Station
from stations.serializers import StationsSerializer
from .serializers import ReportSerializer
from backend.permissions import IsAdminUser, IsAuthenticated


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def overview(request):
    Report = {
        "List": "/api/report",
    }
    return Response(Report)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def getDayReport(request, pk):
    date = request.data["date"]
    range = datetime.strptime(date, '%Y-%m-%d').date()
    obs_type = request.data["obs_type"]
    obs_key = Observation.objects.filter(
        rec_date__year=range.year,
        rec_date__month=range.month,
        rec_date__day=range.day, station=pk, type=obs_type)
    if obs_key.count() > 0 :#!!!!!!!!!!!!! S_OBS.COUNT????????,, 
        s_obs = ReportSerializer(obs_key, many=True, ).data
        stat = {
            "stat_id": s_obs[0]["id"],
            "stat_name": s_obs[0]["stat"]["name"],
            "stat_oaci": s_obs[0]["stat"]["OACI"],
            "stat_omm": s_obs[0]["stat"]["OMM"],
            "expected_d": s_obs[0]["stat"][obs_type]["expected_d"],
        }
        rec_num = obs_key.count()
        prod = round((rec_num / stat["expected_d"]) * 100, 2)
        prodH1 = []
        prodH2 = []
        rtdH1  = []
        rtdH2  = []
        rtdH3  = []
        for obs in s_obs:
            if obs["type"] == "METAR":
                t1 = datetime.strptime(obs["rec_time"], '%H:%M:%S')
                t2 = datetime.strptime(obs["obs_time"], '%H:%M:%S')
                td = t1-t2
                tf = (td.total_seconds() / 60) - 60  # UTC
                if tf <= 3:
                    prodH1.append(obs)
                if tf <= 5:
                    prodH2.append(obs)
                if 5 < tf <= 33:
                    rtdH1.append(obs)
                if 33 < tf <= 49:
                    rtdH2.append(obs)
                if tf > 49:
                    rtdH3.append(obs)
            elif obs["type"] == "SYNOP":
                t1 = datetime.strptime(obs["rec_time"], '%H:%M:%S')
                t2 = datetime.strptime(obs["obs_time"], '%H:%M:%S')
                td = t2-t1
                tf = (td.total_seconds() / 60) - 60  # UTC
                if tf <= 5:
                    prodH1.append(obs)
                if tf <= 10:
                    prodH2.append(obs)
                if 10<tf <= 120:
                    rtdH1.append(obs)
                if 120<tf <= 360:
                    rtdH2.append(obs)
                if tf>360 :
                    rtdH3.append(obs)
        s_prodH1 = round((len(prodH1) / stat["expected_d"]) * 100, 2)
        s_prodH2 = round((len(prodH2) / stat["expected_d"]) * 100, 2)
        s_rtdH1  = round((len(rtdH1)  / stat["expected_d"]) * 100, 2)
        s_rtdH2  = round((len(rtdH2)  / stat["expected_d"]) * 100, 2)
        s_rtdH3  = round((len(rtdH3)  / stat["expected_d"]) * 100, 2)
        return Response({"obs_": s_obs,
            "stat_info": stat,
            "rec_num": rec_num,
            "day_prod": prod, 
            "s_prodh1": s_prodH1, 
            "s_prodh2": s_prodH2, 
            "s_rtdH1": s_rtdH1,
            "s_rtdH2": s_rtdH2,
            "s_rtdH3": s_rtdH3,
            })
    else :
        return Response({"error": True, "message" : "no records saved on that day"})  



@api_view(["POST"])
@permission_classes([IsAuthenticated])
def getTotalDayReport(request):
    date = request.data["date"]
    range = datetime.strptime(date, '%Y-%m-%d').date()
    obs_type = request.data["obs_type"]
    stat_data = Station.objects.all()
    stat_list = StationsSerializer(stat_data, many=True)
    result = []
    for stat_obj in stat_list.data : 
        obs_key = Observation.objects.filter(
        rec_date__year=range.year,
        rec_date__month=range.month,
        rec_date__day=range.day, station=stat_obj["id"], type=obs_type)
        if obs_key.count() > 0 :
            s_obs = ReportSerializer(obs_key, many=True, ).data
            stat = {
                "stat_id": s_obs[0]["id"],
                "stat_name": s_obs[0]["stat"]["name"],
                "stat_oaci": s_obs[0]["stat"]["OACI"],
                "stat_omm": s_obs[0]["stat"]["OMM"],
                "expected_d": s_obs[0]["stat"][obs_type]["expected_d"],
            }
            rec_num = obs_key.count()
            prod = round((rec_num / stat["expected_d"]) * 100, 2)
            prodH1 = []
            prodH2 = []
            rtdH1  = []
            rtdH2  = []
            rtdH3  = []
            for obs in s_obs:
                if obs["type"] == "METAR":
                    t1 = datetime.strptime(obs["rec_time"], '%H:%M:%S')
                    t2 = datetime.strptime(obs["obs_time"], '%H:%M:%S')
                    td = t1-t2
                    tf = (td.total_seconds() / 60) - 60  # UTC
                    if tf <= 3:
                        prodH1.append(obs)
                    if tf <= 5:
                        prodH2.append(obs)
                    if 5 < tf <= 33:
                        rtdH1.append(obs)
                    if 33 < tf <= 49:
                        rtdH2.append(obs)
                    if tf > 49:
                        rtdH3.append(obs)
                elif obs["type"] == "SYNOP":
                    t1 = datetime.strptime(obs["rec_time"], '%H:%M:%S')
                    t2 = datetime.strptime(obs["obs_time"], '%H:%M:%S')
                    td = t2-t1
                    tf = (td.total_seconds() / 60) - 60  # UTC
                    if tf <= 5:
                        prodH1.append(obs)
                    if tf <= 10:
                        prodH2.append(obs)
                    if 10<tf <= 120:
                        rtdH1.append(obs)
                    if 120<tf <= 360:
                        rtdH2.append(obs)
                    if tf>360 :
                        rtdH3.append(obs)
            s_prodH1 = round((len(prodH1) / stat["expected_d"]) * 100, 2)
            s_prodH2 = round((len(prodH2) / stat["expected_d"]) * 100, 2)
            s_rtdH1  = round((len(rtdH1)  / stat["expected_d"]) * 100, 2)
            s_rtdH2  = round((len(rtdH2)  / stat["expected_d"]) * 100, 2)
            s_rtdH3  = round((len(rtdH3)  / stat["expected_d"]) * 100, 2)
            result.append({
                "stat_info": stat,
                "rec_num": rec_num,
                "day_prod": prod, 
                "s_prodh1": s_prodH1, 
                "s_prodh2": s_prodH2, 
                "s_rtdH1": s_rtdH1,
                "s_rtdH2": s_rtdH2,
                "s_rtdH3": s_rtdH3,
                })
        else: 
            stat = {
                "stat_id": stat_obj["id"],
                "stat_name": stat_obj["name"],
                "stat_oaci": stat_obj["OACI"] ,
                "stat_omm": stat_obj["OMM"],
                "expected_d": stat_obj[obs_type]["expected_d"] ,

                "taux": stat_obj[obs_type]
            }
            result.append({
                "stat_info": stat,
                "rec_num": 0,
                "day_prod": 0, 
                "s_prodh1": 0, 
                "s_prodh2": 0, 
                "s_rtdH1": 0,
                "s_rtdH2": 0,
                "s_rtdH3": 0,
                })
    return Response( result)  



@api_view(["POST"])
@permission_classes([IsAuthenticated])
def getMonthReport(request, pk):
    date = request.data["date"]
    range = datetime.strptime(date, '%Y-%m-%d').date()
    obs_type = request.data["obs_type"]
    days_in_current_month = calendar.monthrange(range.year, range.month)[1]
    obs_key = Observation.objects.filter(
        rec_date__year=range.year,
        rec_date__month=range.month,
        station=pk, type=obs_type)
    if obs_key.count() > 0 :
        s_obs = ReportSerializer(obs_key, many=True, ).data
        stat = {
            "stat_id": s_obs[0]["id"],
            "stat_name": s_obs[0]["stat"]["name"],
            "stat_oaci": s_obs[0]["stat"]["OACI"],
            "stat_omm": s_obs[0]["stat"]["OMM"],
            "expected_d": s_obs[0]["stat"][obs_type]["expected_d"],
            "expected_m": s_obs[0]["stat"][obs_type]["expected_m"],
        }
        rec_num = obs_key.count()
        prod = round((rec_num / (stat["expected_d"] * days_in_current_month) ) * 100, 2)
        prodH1 = []
        prodH2 = []
        rtdH1  = []
        rtdH2  = []
        rtdH3  = []
        for obs in s_obs:
            if obs["type"] == "METAR":
                t1 = datetime.strptime(obs["rec_time"], '%H:%M:%S')
                t2 = datetime.strptime(obs["obs_time"], '%H:%M:%S')
                td = t1-t2
                tf = (td.total_seconds() / 60) - 60  # UTC
                if tf <= 3:
                    prodH1.append(obs)
                if tf <= 5:
                    prodH2.append(obs)
                if 5 < tf <= 33:
                    rtdH1.append(obs)
                if 33 < tf <= 49:
                    rtdH2.append(obs)
                if tf > 49:
                    rtdH3.append(obs)
            elif obs["type"] == "SYNOP":
                t1 = datetime.strptime(obs["rec_time"], '%H:%M:%S')
                t2 = datetime.strptime(obs["obs_time"], '%H:%M:%S')
                td = t2-t1
                tf = (td.total_seconds() / 60) - 60  # UTC
                if tf <= 5:
                    prodH1.append(obs)
                if tf <= 10:
                    prodH2.append(obs)
                if 10<tf <= 120:
                    rtdH1.append(obs)
                if 120<tf <= 360:
                    rtdH2.append(obs)
                if tf>360 :
                    rtdH3.append(obs)
        s_prodH1 = round((len(prodH1) / (stat["expected_d"] * days_in_current_month)) * 100, 2)
        s_prodH2 = round((len(prodH2) / (stat["expected_d"] * days_in_current_month)) * 100, 2)
        s_rtdH1  = round((len(rtdH1)  / (stat["expected_d"] * days_in_current_month)) * 100, 2)
        s_rtdH2  = round((len(rtdH2)  / (stat["expected_d"] * days_in_current_month)) * 100, 2)
        s_rtdH3  = round((len(rtdH3)  / (stat["expected_d"] * days_in_current_month)) * 100, 2)
        return Response({"obs_": s_obs,
            "stat_info": stat,
            "rec_num": rec_num,
            "month_prod": prod, 
            "s_prodh1": s_prodH1, 
            "s_prodh2": s_prodH2, 
            "s_rtdH1": s_rtdH1,
            "s_rtdH2": s_rtdH2,
            "s_rtdH3": s_rtdH3,
            })
    else :
        return Response({"error": True, "message" : "no records saved on that month"})  



@api_view(["POST"])
@permission_classes([IsAuthenticated])
def getTotalMonthReport(request):
    date = request.data["date"]
    range = datetime.strptime(date, '%Y-%m-%d').date()
    days_in_current_month = calendar.monthrange(range.year, range.month)[1]
    obs_type = request.data["obs_type"]
    stat_data = Station.objects.all()
    stat_list = StationsSerializer(stat_data, many=True)
    result = []
    for stat_obj in stat_list.data : 
        obs_key = Observation.objects.filter(
        rec_date__year=range.year,
        rec_date__month=range.month,
        station=stat_obj["id"], type=obs_type)
        if obs_key.count() > 0 :
            s_obs = ReportSerializer(obs_key, many=True, ).data
            stat = {
                "stat_id": s_obs[0]["id"],
                "stat_name": s_obs[0]["stat"]["name"],
                "stat_oaci": s_obs[0]["stat"]["OACI"],
                "stat_omm": s_obs[0]["stat"]["OMM"],
                "expected_d": s_obs[0]["stat"][obs_type]["expected_d"],
                "expected_m": s_obs[0]["stat"][obs_type]["expected_m"],
            }
            rec_num = obs_key.count()
            prod = round((rec_num / (stat["expected_d"] * days_in_current_month) ) * 100, 2)
            prodH1 = []
            prodH2 = []
            rtdH1  = []
            rtdH2  = []
            rtdH3  = []
            for obs in s_obs:
                if obs["type"] == "METAR":
                    t1 = datetime.strptime(obs["rec_time"], '%H:%M:%S')
                    t2 = datetime.strptime(obs["obs_time"], '%H:%M:%S')
                    td = t1-t2
                    tf = (td.total_seconds() / 60) - 60  # UTC
                    if tf <= 3:
                        prodH1.append(obs)
                    if tf <= 5:
                        prodH2.append(obs)
                    if 5 < tf <= 33:
                        rtdH1.append(obs)
                    if 33 < tf <= 49:
                        rtdH2.append(obs)
                    if tf > 49:
                        rtdH3.append(obs)
                elif obs["type"] == "SYNOP":
                    t1 = datetime.strptime(obs["rec_time"], '%H:%M:%S')
                    t2 = datetime.strptime(obs["obs_time"], '%H:%M:%S')
                    td = t2-t1
                    tf = (td.total_seconds() / 60) - 60  # UTC
                    if tf <= 5:
                        prodH1.append(obs)
                    if tf <= 10:
                        prodH2.append(obs)
                    if 10<tf <= 120:
                        rtdH1.append(obs)
                    if 120<tf <= 360:
                        rtdH2.append(obs)
                    if tf>360 :
                        rtdH3.append(obs)
            s_prodH1 = round((len(prodH1) / (stat["expected_d"] * days_in_current_month)) * 100, 2)
            s_prodH2 = round((len(prodH2) / (stat["expected_d"] * days_in_current_month)) * 100, 2)
            s_rtdH1  = round((len(rtdH1)  / (stat["expected_d"] * days_in_current_month)) * 100, 2)
            s_rtdH2  = round((len(rtdH2)  / (stat["expected_d"] * days_in_current_month)) * 100, 2)
            s_rtdH3  = round((len(rtdH3)  / (stat["expected_d"] * days_in_current_month)) * 100, 2)
            result.append({
                "stat_info": stat,
                "rec_num": rec_num,
                "month_prod": prod, 
                "s_prodh1": s_prodH1, 
                "s_prodh2": s_prodH2, 
                "s_rtdH1": s_rtdH1,
                "s_rtdH2": s_rtdH2,
                "s_rtdH3": s_rtdH3,
                })
        else: 
            stat = {
                "stat_id": stat_obj["id"],
                "stat_name": stat_obj["name"],
                "stat_oaci": stat_obj["OACI"] ,
                "stat_omm": stat_obj["OMM"],
                "expected_m": stat_obj[obs_type]["expected_m"] ,
                "taux": stat_obj[obs_type]
            }
            result.append({
                "stat_info": stat,
                "rec_num": 0,
                "month_prod": 0, 
                "s_prodh1": 0, 
                "s_prodh2": 0, 
                "s_rtdH1": 0,
                "s_rtdH2": 0,
                "s_rtdH3": 0,
                })
    return Response( result)  



@api_view(["POST"])
@permission_classes([IsAuthenticated])
def getYearReport(request, pk):
    date = request.data["date"]
    range = datetime.strptime(date, '%Y-%m-%d').date()
    obs_type = request.data["obs_type"]
    if calendar.isleap(range.year):
        days_in_current_year = 366
    else:
        days_in_current_year = 365
    obs_key = Observation.objects.filter(
        rec_date__year=range.year,
        station=pk, type=obs_type)
    if obs_key.count() > 0 :
        s_obs = ReportSerializer(obs_key, many=True, ).data
        stat = {
            "stat_id": s_obs[0]["id"],
            "stat_name": s_obs[0]["stat"]["name"],
            "stat_oaci": s_obs[0]["stat"]["OACI"],
            "stat_omm": s_obs[0]["stat"]["OMM"],
            "expected_y": s_obs[0]["stat"][obs_type]["expected_d"] * days_in_current_year,
        }
        rec_num = obs_key.count()
        prod = round((rec_num / (stat["expected_d"] * days_in_current_year) ) * 100, 2)
        prodH1 = []
        prodH2 = []
        rtdH1  = []
        rtdH2  = []
        rtdH3  = []
        for obs in s_obs:
            if obs["type"] == "METAR":
                t1 = datetime.strptime(obs["rec_time"], '%H:%M:%S')
                t2 = datetime.strptime(obs["obs_time"], '%H:%M:%S')
                td = t1-t2
                tf = (td.total_seconds() / 60) - 60  # UTC
                if tf <= 3:
                    prodH1.append(obs)
                if tf <= 5:
                    prodH2.append(obs)
                if 5 < tf <= 33:
                    rtdH1.append(obs)
                if 33 < tf <= 49:
                    rtdH2.append(obs)
                if tf > 49:
                    rtdH3.append(obs)
            elif obs["type"] == "SYNOP":
                t1 = datetime.strptime(obs["rec_time"], '%H:%M:%S')
                t2 = datetime.strptime(obs["obs_time"], '%H:%M:%S')
                td = t2-t1
                tf = (td.total_seconds() / 60) - 60  # UTC
                if tf <= 5:
                    prodH1.append(obs)
                if tf <= 10:
                    prodH2.append(obs)
                if 10<tf <= 120:
                    rtdH1.append(obs)
                if 120<tf <= 360:
                    rtdH2.append(obs)
                if tf>360 :
                    rtdH3.append(obs)
        s_prodH1 = round((len(prodH1) / (stat["expected_d"] * days_in_current_year)) * 100, 2)
        s_prodH2 = round((len(prodH2) / (stat["expected_d"] * days_in_current_year)) * 100, 2)
        s_rtdH1  = round((len(rtdH1)  / (stat["expected_d"] * days_in_current_year)) * 100, 2)
        s_rtdH2  = round((len(rtdH2)  / (stat["expected_d"] * days_in_current_year)) * 100, 2)
        s_rtdH3  = round((len(rtdH3)  / (stat["expected_d"] * days_in_current_year)) * 100, 2)
        return Response({"obs_": s_obs,
            "stat_info": stat,
            "rec_num": rec_num,
            "year_prod": prod, 
            "s_prodh1": s_prodH1, 
            "s_prodh2": s_prodH2, 
            "s_rtdH1": s_rtdH1,
            "s_rtdH2": s_rtdH2,
            "s_rtdH3": s_rtdH3,
            })
    else :
        return Response({"error": True, "message" : "no records saved on that year"})  


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def getTotalYearReport(request):
    date = request.data["date"]
    range = datetime.strptime(date, '%Y-%m-%d').date()
    if calendar.isleap(range.year):
        days_in_current_year = 366
    else:
        days_in_current_year = 365
    obs_type = request.data["obs_type"]
    stat_data = Station.objects.all()
    stat_list = StationsSerializer(stat_data, many=True)
    result = []
    for stat_obj in stat_list.data : 
        obs_key = Observation.objects.filter(
        rec_date__year=range.year,
        station=stat_obj["id"], type=obs_type)
        if obs_key.count() > 0 :
            s_obs = ReportSerializer(obs_key, many=True, ).data
            stat = {
                "stat_id": s_obs[0]["id"],
                "stat_name": s_obs[0]["stat"]["name"],
                "stat_oaci": s_obs[0]["stat"]["OACI"],
                "stat_omm": s_obs[0]["stat"]["OMM"],
                "expected_d": s_obs[0]["stat"][obs_type]["expected_d"],
                "expected_y": s_obs[0]["stat"][obs_type]["expected_d"] * days_in_current_year,
            }
            rec_num = obs_key.count()
            prod = round((rec_num / (stat["expected_d"] * days_in_current_year) ) * 100, 2)
            prodH1 = []
            prodH2 = []
            rtdH1  = []
            rtdH2  = []
            rtdH3  = []
            for obs in s_obs:
                if obs["type"] == "METAR":
                    t1 = datetime.strptime(obs["rec_time"], '%H:%M:%S')
                    t2 = datetime.strptime(obs["obs_time"], '%H:%M:%S')
                    td = t1-t2
                    tf = (td.total_seconds() / 60) - 60  # UTC
                    if tf <= 3:
                        prodH1.append(obs)
                    if tf <= 5:
                        prodH2.append(obs)
                    if 5 < tf <= 33:
                        rtdH1.append(obs)
                    if 33 < tf <= 49:
                        rtdH2.append(obs)
                    if tf > 49:
                        rtdH3.append(obs)
                elif obs["type"] == "SYNOP":
                    t1 = datetime.strptime(obs["rec_time"], '%H:%M:%S')
                    t2 = datetime.strptime(obs["obs_time"], '%H:%M:%S')
                    td = t2-t1
                    tf = (td.total_seconds() / 60) - 60  # UTC
                    if tf <= 5:
                        prodH1.append(obs)
                    if tf <= 10:
                        prodH2.append(obs)
                    if 10<tf <= 120:
                        rtdH1.append(obs)
                    if 120<tf <= 360:
                        rtdH2.append(obs)
                    if tf>360 :
                        rtdH3.append(obs)
            s_prodH1 = round((len(prodH1) / (stat["expected_d"] * days_in_current_year)) * 100, 2)
            s_prodH2 = round((len(prodH2) / (stat["expected_d"] * days_in_current_year)) * 100, 2)
            s_rtdH1  = round((len(rtdH1)  / (stat["expected_d"] * days_in_current_year)) * 100, 2)
            s_rtdH2  = round((len(rtdH2)  / (stat["expected_d"] * days_in_current_year)) * 100, 2)
            s_rtdH3  = round((len(rtdH3)  / (stat["expected_d"] * days_in_current_year)) * 100, 2)
            result.append({
                "stat_info": stat,
                "rec_num": rec_num,
                "year_prod": prod, 
                "s_prodh1": s_prodH1, 
                "s_prodh2": s_prodH2, 
                "s_rtdH1": s_rtdH1,
                "s_rtdH2": s_rtdH2,
                "s_rtdH3": s_rtdH3,
                })
        else: 
            stat = {
                "stat_id": stat_obj["id"],
                "stat_name": stat_obj["name"],
                "stat_oaci": stat_obj["OACI"] ,
                "stat_omm": stat_obj["OMM"],
                "expected_y": stat_obj[obs_type]["expected_d"] * days_in_current_year ,
                "taux": stat_obj[obs_type]
            }
            result.append({
                "stat_info": stat,
                "rec_num": 0,
                "year_prod": 0, 
                "s_prodh1": 0, 
                "s_prodh2": 0, 
                "s_rtdH1": 0,
                "s_rtdH2": 0,
                "s_rtdH3": 0,
                })
    return Response( result)  

