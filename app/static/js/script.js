//Tabs function - Access Page
        function hide_content() {
                var tabs = document.getElementsByClassName('tab_content');
                for (i=0; i < tabs.length; i++) {
                tabs[i].style.display = 'none';
                                }               }
        
        $(document).ready(function() {
        $("#info_button").click(function() {
                hide_content();
                $("#info").show();	});

        $("#edit_button").click(function() {
                hide_content();
                $("#edit_acc").show();      });

	$("#password_button").click(function() {
		hide_content();
		$("#change_pass").show();   });

	$("#delete_button").click(function() {
		hide_content();
		$("#delete").show();	    });
});


/*Registration and Login*/
        $(document).ready(function() {
                $("#smile").hide();
                switch ("{{ access }}")
                        {
                                case 'Register': alert("You are not registered. Please sign up")
                                break;

                                case 'Granted': window.location="{{ url_for('auth.access') }}";
                                break;

                                case 'Denied': alert("Invalid username or password.");
                                break; 
                        }

        $("#register_link").click(function() {
                $("#signup").hide(function(){
                var title = $("#form_description").get(0);
                change_title = title.childNodes[0];
                change_title.nodeValue = "Registration";
                $("#register").show();
                $("#smile").show(); 
                });
                });

         $("#signup_link").click(function() {
                $("#register").hide( function(){
                var title = $("#form_description").get(0);
                change_title = title.childNodes[0];
                change_title.nodeValue = "User Login";
                $("#signup").show(); 
                $("#smile").hide();
                });
                });
                                });


/*Update User Account*/
function update_content() {
	var form = document.getElementById("update")
	var update_form = FormData(form);
	var xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function() {
	  if (this.readyState == 4 && this.status == 200) {
  	  	alert("Account Information Successfully Updated")
 						           }
						}
	xhttp.open("POST", "/auth/access", true);
	xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded;charset=UTF-8");
	xhttp.send(update_form)

}

						













