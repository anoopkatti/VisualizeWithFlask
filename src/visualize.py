import threading
import flask
import time

from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import file_html

app = flask.Flask(__name__)
somelist = []


@app.route('/')
def return_somelist():
    # create a new plot with a title and axis labels
    plot = figure(title="simple line example", x_axis_label='x',
                  y_axis_label='y', x_range=[0, 100], y_range=[0, 100])

    # add a line renderer with legend and line thickness
    plot.line(range(len(somelist)), somelist, legend="Temp.", line_width=2)
    html = file_html(plot, CDN, "my plot")

    return html


def print_time(threadName, delay, counter):
    while counter:
        somelist.append(counter)
        time.sleep(delay)
        print "%s: %s" % (threadName, time.ctime(time.time()))
        counter -= 1


if __name__ == '__main__':
    thread = threading.Thread(target=print_time, args=("th-1", 1, 100))
    thread.start()
    app.run(debug=True)
