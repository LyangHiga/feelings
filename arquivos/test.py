import os
import sys
from pyspark import SparkConf, SparkContext
conf = (SparkConf()
         .setMaster("local")
         .setAppName("Analise de Sentimentos")
         .set("spark.executor.memory", "1g"))
sc = SparkContext(conf = conf)


def analiseSentimentos(x):
    return len(x)%5


def geraGrafico(nome,valores):
    for i in xrange(len(valores)):
        valores[i]=list(valores[i])
    valores = [['Valor','Tweets']]+valores
    #for i in xrange(len(valores)): valores[i][1]=str(valores[i][1])
    out = """<html>
  <head>
    <!--Load the AJAX API-->
    <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
    <script type="text/javascript">

      // Load the Visualization API and the corechart package.
      google.charts.load('current', {'packages':['corechart']});

      // Set a callback to run when the Google Visualization API is loaded.
      google.charts.setOnLoadCallback(drawChart);

      // Callback that creates and populates a data table,
      // instantiates the pie chart, passes in the data and
      // draws it.
      function drawChart() {

        // Create the data table.
        var data = new google.visualization.arrayToDataTable("""+"{0});".format(str(valores)) + """

        // Set chart options
        var options = {'title':'Analise de Sentimentos ("""+nome+""")',
                       'width':700,
                       'height':400,
                       'hAxis': {title: 'Valor'},
                       'vAxis': {title: 'Tweets'},
                       'legend':'none'};

        // Instantiate and draw our chart, passing in some options.
        var chart = new google.visualization.ScatterChart(document.getElementById('chart_div'));
        chart.draw(data, options);
      }
    </script>
  </head>

  <body>
    <!--Div that will hold the chart-->
    <div id="chart_div" style="width:700; height:500"></div>
  </body>
</html>
    """
    f = open("./{0}.html".format(nome),"w")
    f.write(out)
    f.close()

def funcaoMain():
    if len(sys.argv)<2:
        return False
    hashtag = sys.argv[1]
    if len(hashtag)==0:
        hashtag = "#"
    arquivo = sc.textFile("./arquivos/{0}.txt".format(hashtag))
    geraGrafico(hashtag, arquivo.map(lambda x: (analiseSentimentos(x.split("|")[0]), 1) ).reduceByKey(lambda x,y: x+y).sortByKey(False).collect())

if __name__ == '__main__':
    funcaoMain()
