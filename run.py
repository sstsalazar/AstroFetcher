from flask import Flask
from flask_restful import Api, Resource, reqparse
from astrofetch.AstroFetch import AstroFetch

app = Flask(__name__)
api = Api(app)


class DataAcquisitionApi(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("config",
                                   required=True,
                                   type=dict,
                                   help="No config dictionary provided.")
        self.reqparse.add_argument("log",
                                   type=str,
                                   default="/tmp/astrofetcher/")
        self.reqparse.add_argument("data",
                                   type=str,
                                   default="/tmp/astrofetcher/data")
        super(DataAcquisitionApi, self).__init__()

    def post(self):
        args = self.reqparse.parse_args()



if __name__ == "__main__":
    app.run(debug=True)
