from robinhood.authentication import login
import configparser



def read_config(config_path='config.ini'):
    config = configparser.ConfigParser()
    config.read(config_path)
    settings = {}
    for key, value in config.items("SETTINGS"):
        settings[key] = value
    return settings


def rh_login(settings):
    """
    Robinhood Login:
    username: "Your Username" - Most likely your email
    password: "Your Robinhood password to login"

    """
<<<<<<< HEAD
    logins = login(username=settings.get('username'), password=settings.get('password'), expiresIn=None, scope='internal', by_sms=True, store_session=True, mfa_code=None, pickle_name='')

=======
    logins = login(username='your_username', password='your_password', expiresIn=None, scope='internal', by_sms=True, store_session=True, mfa_code=None, pickle_name='')
    
>>>>>>> e082c8c7b9088abffe69823655f07be220b52239
    if logins.get('access_token'):
        print("Good to go! Logged into Robinhood")
        pass

if __name__ == '__main__':
    rh_login()