from controllers.user_controller import UserShow, UserCreateAndList
from controllers.report_controller import UsersWithouLoaded, UsersWithOwnVehicle, TerminalReportController, TravelReportController
from controllers.terminal_controller import TerminalController
from controllers.travel_controller import TravelShow, TravelCreateAndList

def configRoutes(config):
    config.api.add_resource(UserShow, '/api/users/<string:id>')
    config.api.add_resource(UserCreateAndList, '/api/users')
    
    config.api.add_resource(UsersWithouLoaded, '/api/reports/bused-users')
    config.api.add_resource(UsersWithOwnVehicle, '/api/reports/users-has-vehicle')
    config.api.add_resource(TerminalReportController, '/api/reports/terminals')
    config.api.add_resource(TravelReportController, '/api/reports/travels')

    config.api.add_resource(TerminalController, '/api/terminals')
    
    config.api.add_resource(TravelShow, '/api/travels/<string:id>')
    config.api.add_resource(TravelCreateAndList, '/api/travels')