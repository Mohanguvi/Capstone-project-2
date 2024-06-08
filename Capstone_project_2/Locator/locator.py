class WebSource:

    def __init__(self):
        """
        The __init__() method initializes the class instance with the following attributes:
            - Username: Locator for the username input field.
            - Password: Locator for the password input field.
            - loginButton: Locator for the login button.
            - userMenu: Locator for the user menu.
            - logout: Locator for the logout button.
        """
        # login element
        self.Username = "username"
        self.Password = "password"
        self.login_button = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'
        self.forget_password = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[4]/p'
        self.reset_button = '//*[@id="app"]/div[1]/div[1]/div/form/div[2]/button[2]'
        self.title = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a'

        # logout elements
        self.userMenu = '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li'
        self.logout = '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a'

        # admin access
        self.access = '//*[@id="app"]/div[1]/div[1]/form/h6'
        self.SubmitAccess = '//*[@id="app"]/div[1]/div[1]/form/div[4]/button[2]'

        # Dashboard home
        self.dashboard = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[8]/a'

        # Admin options
        self.user_Management = '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]'
        self.users = '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li'
        self.Job = '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]'
        self.Job_titles = '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[1]'
        self.Organization = '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]'
        self.General_information = '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]/ul/li[1]'
        self.Qualifications = '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[4]'
        self.Skills = '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[4]/ul/li[1]'
        self.Nationalities = '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[5]'
        self.Corporate_Banking = '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[6]'
        self.Configuration = '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[7]/span'
        self.Email_configuration = '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[7]/ul/li[1]'

        # Main menu options
        self.Admin = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a'
        self.PIM = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a'
        self.Leave = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[3]/a'
        self.Time = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[4]/a'
        self.Recruitment = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[5]/a'
        self.My_Info = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a'
        self.Performance = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[7]/a'
        self.Dashboard = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[8]/a'
        self.Directory = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[9]/a'
        self.Maintenance = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[10]/a'
        self.Buzz = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[12]/a'
