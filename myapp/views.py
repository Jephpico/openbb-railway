from django.http import HttpResponse
from openbb_terminal.sdk import openbb


def hello(request):
    return HttpResponse("Hello, World!")

"""
def forex_data(
    from_symbol,
    to_symbol,
    interval,
    resolution = "1 day",
    start_date = None,
    end_date= None,
    source = "YahooFinance",
    verbose= False
):
    data = openbb.forex.load( from_symbol, to_symbol,resolution, interval.value, start_date, end_date, source, verbose)
#    data['time'] = data.index.tolist()
    data_todict = data.to_dict(orient="records")
    return data_todict
"""
from rest_framework.views import APIView
from rest_framework.response import Response
#from .serializers import ForexDataSerializer
from .schemas import ForexInterval

"""

class ForexDataView(APIView):
    def post(self, request):
        serializer = ForexDataSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            open_forex_data = openbb.forex.load(
                from_symbol=data['from_symbol'],
                to_symbol=data['to_symbol'],
                interval=data['interval'],
                resolution=data['resolution'],
                start_date=data['start_date'],
                end_date=data['end_date'],
                source=data['source'],
                verbose=data['verbose']
            )
            forex_data = open_forex_data
            
            return Response(forex_data)
        return Response(serializer.errors, status=400)
"""

class ForexDataView(APIView):
    def post(self, request):
        from_symbol = request.data.get("from_symbol")
        to_symbol = request.data.get("to_symbol")
        interval = request.data.get("interval", ForexInterval.ONE_DAY.value)
        resolution = request.data.get("resolution", "1 day")
        start_date = request.data.get("start_date")
        end_date = request.data.get("end_date")
        source = request.data.get("source", "YahooFinance")
        verbose = request.data.get("verbose", False)

        data = openbb.forex.load(from_symbol, to_symbol, resolution, interval, start_date, end_date, source, verbose)
        data_todict = data.to_dict(orient="records")

        return Response(data_todict)