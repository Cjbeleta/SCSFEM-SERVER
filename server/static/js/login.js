function onSignIn(googleUser) {
    var profile = googleUser.getBasicProfile();
    console.log('ID: ' + profile.getId()); // Do not send to your backend! Use an ID token instead.
    console.log('Name: ' + profile.getName());
    console.log('Image URL: ' + profile.getImageUrl());
    console.log('Email: ' + profile.getEmail()); // This is null if the 'email' scope is not present.
    var token = googleUser.getAuthResponse().id_token;
    var ttl = googleUser.getAuthResponse().expires_in;
    var name = profile.getName();
    var email = profile.getEmail();
    console.log('Name: ' + name);
    console.log('Email: ' + email);

    login(profile.getName(), profile.getEmail(), token, ttl);
}

function login(name, email, token, ttl) {
        $.ajax({
            type: "POST",
            url: "http://localhost:5000/login",
            data: {"fullname": name, "email": email, "token": token, "ttl": ttl},
            dataType: "json",
            success: function() {
                console.log('Successfully posted data');
            },
            error: function() {
                console.log('Error');
            }
        });

    }

function signOut() {
    var auth2 = gapi.auth2.getAuthInstance();
    auth2.signOut().then(function () {
        console.log('Im here again')
        $.ajax({
           type: "GET",
           contentType: 'application/json; charset=utf-8',
           url: "http://localhost:5000/logout",
           dataType: "json",
                success: function (resp) {
                        if (resp.message = "okay") {
                            alert("Success");
                            console.log("User signed out.")
                            window.location.replace('/')
                        }
                        else{
                            console.log("Something went wrong")
                        }
                }
        });
    });
}

function onLoad() {
      gapi.load('auth2', function() {
        gapi.auth2.init();
      });
    }