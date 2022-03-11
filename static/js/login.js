$('#submit').click(function(e){
    
    //get the values from the template
    var username=document.getElementById('username').value
    var password=document.getElementById('password').value

     //check the username
    if(!username){
          alert('Please enter the username!')
          return false;
    }

    //check the password
    else if (!password){                     
                  alert('Please enter the password!')
                  return false;
    }
     
    // confirm to submit
    else{
            var r=confirm('Confirm submission')
             if(r==true){
                  x='Yes';

               //check exists
                 $.ajax({
                       url:'/movieworld/login_check',
                       type:'POST',
                       data:{'username':username,'password':password},
                       datatype:'json',
                       success:function(data){
                               if(data.res==0){
                                       alert('Invalid information!');
                                       $('#msg').html('Please check and try again.');
                                       return false;
                               }
                               else if(data.res==2){
                                       alert('Your account is disabled.')
                                       return false;
                               }
                               else{
                                       location.href='/movieworld/'  
                               }
                        },
                        error: function(){
                              alert('error')
                        } 
                  })
              }
              else{
                  x='No';
                  return false;
              }
      }
})