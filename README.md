# trailers_app

This project is a web application which allows users to store and play the trailers of their favorite movies. The application is powered by the Django Web Framework and Django's third party applications. It uses the Bootstrap Frontend Framework to nicely render the UI.

---

# Application features

Following are some of the major feratures of the application:

1. User Authentication feature - signup(through django-registration's 2-step verification), login and logout
2. Reset password feature - The reset password link is send to email
3. Change password feature - The password can be changed when the user is logged in
4. Authorization and Permission feature - Only logged users can store and play trailers.
5. Feature to store movie trailer url, movie poster and movie plot.
6. Feature to edit movie trailer url, movie poster and movie plot.
7. Feature to delete movie trailer.
8. Feature to list a user's stored trailers.


# Screenshots

1. Landing Page

![LandingPage](/screenshots/LandingPage.jpg)

2. Sign Up Page

![Signup](/screenshots/SignUp.jpg)

3. Reset Password Page

![ResetPassword](/screenshots/ResetPassword.jpg)

3. Login Page

![LoginPage](/screenshots/SignIn.jpg)

4. Change Password Page

![ChangePassword](/screenshots/ChangePassword.jpg)

5. Home Page of Logged in User

![UserHomePage](/screenshots/UserHomePage.jpg)

6. Playback of trailer in Home Page

![MoviePlaybackHome](/screenshots/MoviePlaybackHome.jpg)

7. Movie detail page

![MovieDetail](/screenshots/MovieDetail.jpg)

8. Playback of trailer in Movie detail page

![MoviePlaybackDetail](/screenshots/MoviePlaybackDetail.jpg)

9. Movie edit page

![MovieEdit](/screenshots/MovieEdit.jpg)

10. Movie delete page

![MovieDelete](/screenshots/MovieDelete.jpg)


# Running the application

**Note**: 
1. For signup, you need to have smtp backend support through a third party like `sendgrid`. Save the environment variables for
the smtp email user and smtp email password of your smtp applicationin `.env` file in the project's root directory. I used sendgrid.


```
EMAIL_HOST_USER=<your_apikey>
EMAIL_HOST_PASSWORD=<your_password>
```
2. For creating virtual environment, installing the dependencies and loading the environment variables, I used `pipenv`. 


```
# git clone https://github.com/realnitinworks/trailers-app.git
# pipenv install
# pipenv shell
# python manage.py runserver
```





