## SAVESTS TECHNICAL ASSESSMENT ON DJANGO WEB FRAMEWORK

The Link to the deployed assessment is https://chidibede-djangoadmin-extended.herokuapp.com/

Your task is to extend the Django-admin user interface doing the following:
Create a superuser with credentials username: root password: password
Extend the Django admin dashboard page to show user metrics, example is the number of users created over the past 24hours, past week and past month. (You can add additional metrics to the admin dashboard at your discretion). 
Add a custom action button to the users list page that enables staff to set a user to active or inactive with the click of a button. (You can add additional useful functionalities to the admin users list page at your discretion).
Add a functionality page that allows staff to send an email to all existing users. You can/should use Django's console.EmailBackend to send the emails.


### To Test it Locally
```
pip3 install pipenv
pipenv install
pipenv shell
cd technical_assessment/
python3 manage.py runserver
```
### Screenshots of the admin dashboards

Custom users list with change active status button attached
<img src="https://res.cloudinary.com/chidibede/image/upload/v1598537350/savests/search_user.png"></img>

Daily User Metrics
<img src= "https://res.cloudinary.com/chidibede/image/upload/v1598537350/savests/daily_metrics_slider.png"></img>

Weekly User Metrics
<img src= "https://res.cloudinary.com/chidibede/image/upload/v1598537350/savests/weekly_metrics_slider.png"></img>

Weekly User Metrics
<img src= "https://res.cloudinary.com/chidibede/image/upload/v1598537350/savests/monthly_metrics_slider.png"></img>

Customized Django Admin Actions
<img src= "https://res.cloudinary.com/chidibede/image/upload/v1598537350/savests/actions.png"></img>
