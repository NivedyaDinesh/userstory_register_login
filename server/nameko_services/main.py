from nameko.runners import ServiceRunner
from auth_service.auth_service import AuthService

config = {'AMQP_URI': 'pyamqp://guest:guest@localhost'}

runner = ServiceRunner(config=config)
runner.add_service(AuthService)

if __name__ == '__main__':
    runner.run()
    