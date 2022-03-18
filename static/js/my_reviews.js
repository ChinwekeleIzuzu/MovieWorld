
$.ajax({
    url: '/movieworld/reviewed_select/',	
    type:'POST',
    success:function (results) {
        render(results)
    }
}); 

function sort(){
    var sort = document.getElementById("sort");
    var option= sort.options[sort.selectedIndex].value;
    
    $.ajax({
        url: '/movieworld/reviewed_select/',
        type:'POST',
        data:{"sort":option},
        success:function (results) {
            render(results)
        }
    }); 
}

function genre(){
    var genre = document.getElementById("genre");
    var option= genre.options[genre.selectedIndex].value;
    
    $.ajax({
        url: '/movieworld/reviewed_select/',
        type:'POST',
        data:{"genre":option},
        success:function (results) {
            render(results)
        }
    }); 
}

function language(){
    var language = document.getElementById("language");
    var option= language.options[language.selectedIndex].value;
    
    $.ajax({
       url: '/movieworld/reviewed_select/',
       type:'POST',
       data:{"language":option},
       success:function (results) {
          render(results)
       }
    });
} 


function render(result){
     $('#table').empty();

     $("#table").append( '<tr>'+'<td>'+'Title'+'</td>'+'<td>'+'Year'+'</td>'+
            '<td>'+'Genre' +'</td>'+'<td>'+'Language'+'</td>'+'<td>'+'Rating'
            +'</td>'+'<td>'+'Review'+'</td>'+'<td>'+'Datetime'+'</td>'+'</tr>'
        )

    $(result).each(function(i,v){
        $("#table").append( '<tr>'+'<td>'+v[0]+'</td>'+'<td>'+v[1]+'</td>'+
            '<td>'+v[2] +'</td>'+'<td>'+v[3]+'</td>'+'<td>'+v[6] 
            +'</td>'+'<td>'+v[4]+'</td>'+'<td>'+v[5]+'</td>'+'</tr>'
        )
    })
}

