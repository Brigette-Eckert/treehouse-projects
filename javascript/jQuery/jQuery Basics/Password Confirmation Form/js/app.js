//problem: Hints are shown even when form is valid
//soultion: Hide and show hints at approriate times
var $password = $("#password");
var $confirm = $("#confirm_password");
	// hide span hints
$("form span").hide();
		
		function isPasswordValid() {
			return $password.val().length > 8;
		}

		function arePasswordsMatching() {
			return $password.val() === $confirm.val();
		}

		function canSubmit() {
			return isPasswordValid() && arePasswordsMatching();
		}

		function passwordEvent() {
			if(isPasswordValid()) {
			$password.next().hide();
			}else {
					//else show hint
			$password.next().show(); 		
			} 
		}

		function confirmPasswordEvent() {

		//find out if password and confirmation match
			if(arePasswordsMatching()) {
				// if passwords match hide second hint
				$confirm.next().hide(); 
			}else {
		// else show hint
		$confirm.next().show(); 
			}
		} 

		function enableSubmitEvent() {
			$("#submit").prop("disable" , !canSubmit());
		}
		//w#passwordhen event happens on password input
		$password.focus(passwordEvent).keyup(passwordEvent).keyup(confirmPasswordEvent).keyup(enableSubmitEvent);
			

		//when event happens on confrimation
		$confirm.focus(confirmPasswordEvent).keyup(confirmPasswordEvent).keyup(enableSubmitEvent);

enableSubmitEvent();