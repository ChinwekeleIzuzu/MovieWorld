
function select_lan(){
    var select = document.getElementById("select_lan");
    var option= select.options[select.selectedIndex].value;
    
    $.ajax({
       url: '/movieworld/movies_select/',
       type:'POST',
       data:{"language":option},
       success:function (results) {
  location.href='/movieworld/reviews_all/'
       }
    });
}

function select_genre(){
    var select = document.getElementById("select_genre");
    var option= select.options[select.selectedIndex].value;
    
    $.ajax({
       url: '/movieworld/movies_select/',
       type:'POST',
       data:{"genre":option},
       success:function (results) {
  location.href='/movieworld/reviews_all/'
       }
    });
} 
