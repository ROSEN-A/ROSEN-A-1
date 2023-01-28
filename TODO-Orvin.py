# THIS IS NEEDED FOR FUTURE ORVIN TO DO CODING
# Source: https://stackoverflow.com/questions/48234240/passing-an-array-from-a-flask-view-to-the-javascript-code-of-another-view


# from flask import Flask, render_template
# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     values = [12, 19, 3, 5, 2, 3]
#     labels = ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange']
#     colors = ['#ff0000','#0000ff','#ffffe0','#008000','#800080','#FFA500']
#     return render_template('pie.html', values=values, labels=labels, colors=colors)

# if __name__ == '__main__':
#     app.run()
    
# <body>
#     <canvas id="pie-chart" width="600" height="400"></canvas>
# </body>
# <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.3.0/Chart.js"></script>
# <script>
#     new Chart(document.getElementById("pie-chart"), {
#          type: 'pie',
#           data: {
#             labels: {{labels | tojson}},
#             datasets: [{
#               label: "Pie Chart",
#               backgroundColor: {{colors | tojson}},
#             data: {{values | tojson}}
#             }]
#           },
#           options: {
#             title: {
#               display: true,
#               text: 'Pie Chart Title'
#             }
#           }
#         });
# </script>
