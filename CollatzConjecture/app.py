from flask import Flask,send_file,session,render_template,request
import pandas as pd
import plotly.express as px

app=Flask(__name__)

def func(input,empty):
    empty.append(input)
    if input==1:
        graph= px.line(empty)
        plot_html = graph.to_html(full_html=False)
        return plot_html
    if input%2==0:
        return func(input//2,empty)
    else:
        return func((3*input)+1,empty)

@app.route('/',methods=['POST','GET'])
def index():
        if request.method=='POST':
            value=request.form.get('value')
            emptylist=[]
            graph=func(int(value),emptylist)
            return render_template('index.html',graph=graph )
        return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)
