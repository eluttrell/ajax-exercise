from flask import Flask, jsonify, request
import pg
app = Flask('app')

db = pg.DB(
    dbname="websites_db"
)

@app.route('/')
def home():
    # this sends the contents of static/index.html
    return app.send_static_file('index.html')


@app.route('/search')
def search():
    # this sends the contents of static/results.json
    # print request.args
    # return app.send_static_file('results.json')
    requested = request.args["search"]
    requested = "%" + requested + "%"
    query = db.query("select * from website where url like $1", requested)
    return jsonify(query.dictresult())


app.run(debug=True)
