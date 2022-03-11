$('#submit').click(function() {

    //set i to check if meet all the conditions 
    var i=0   

    //check the username 
    var username=document.getElementById('username').value
        if(!username){
        usernameSpan="Please enter the username!"
        $('#usernameSpan').html(usernameSpan)
        $('#usernameSpan').css('color','red')
    }

    //check the password
    else{
        $('#usernameSpan').html('') 
        var password=document.getElementById('password').value
            if(!password){
                passwordSpan="Please enter the password!"
                $('#passwordSpan').html(passwordSpan) 
                $('#passwordSpan').css('color','red')
             }

	//check other conditions of the password
            else{ 
                $('#passwordSpan').html('')
                $('#confirmSpan').html('')
                $('#firstline').css('color','black');
                $('#secondline').css('color','black');
                $('#thirdline').css('color','black');
                $('#fourthline').css('color','black');
                passwordSpan="Please enter a valid password!"

	//check the length and space of the password  
                var space=new RegExp(/\s+/g);
	if (space.test(password)){
                    $('#firstline').css('color','red');
                    $('#passwordSpan').html(passwordSpan) 
                    $('#passwordSpan').css('color','red')
                }
                else{          
                     i=i+1
                     $('#firstline').css('color','black');
                }    
                var len=password.length
              	if (len<8){
                    $('#firstline').css('color','red');
                    $('#passwordSpan').html(passwordSpan) 
                    $('#passwordSpan').css('color','red')
                }
                else{          
                     i=i+1
                    $('#firstline').css('color','black');
                }                

	//check if there is a lowercase letter
                    var lower=/[a-z]/;
                    if(lower.test(password)==false){
                        $('#secondline').css('color','red');
                        $('#passwordSpan').html(passwordSpan) 
                        $('#passwordSpan').css('color','red')
                    }
                    else{
                         i=i+1
                        $('#secondline').css('color','black');
                    }
	
	//check if there is an uppercase letter
                     var upper=/[A-Z]/;
                     if(upper.test(password)==false){
                            $('#thirdline').css('color','red');
                            $('#passwordSpan').html(passwordSpan)
                            $('#passwordSpan').css('color','red')
                     }              
                     else{
                           i=i+1
                          $('#thirdline').css('color','black');  
                     }  

	//check if there is a number
                    var number=/[0-9]/;
                    if(number.test(password)==false){
                          $('#fourthline').css('color','red');
                          $('#passwordSpan').html(passwordSpan);
                          $('#passwordSpan').css('color','red')
                    }             
                    else{
                        i=i+1
                        $('#fourthline').css('color','black');  
                    }      

         	//check the confirm password
                //when i=5 means password meets all conditions                
                  if(i==5){ 
                     var confirm=document.getElementById('confirm').value
                      if(!confirm){
                          confirmSpan='Please enter the confirm password!'
                          $('#confirmSpan').html(confirmSpan)
                          $('#confirmSpan').css('color','red')
                      }
	  
                    // check if password and confirm match
                     else{
                           $('#confirmSpan').html('')
                          if(password!=confirm){
                                 confirmSpan='Your password and confirmation password do not match!'
                                 $('#confirmSpan').html(confirmSpan)  
                                 $('#confirmSpan').css('color','red')
                           }
                          else{
                                $('#confirmSpan').html('')
                                i=i+1
                          }
                      } 
                 }          
           }
    }

    //when i=6 means meet all conditions                
         if(i==6){ 
            return true; 
         }
         else{   
           return false;
         }
});
