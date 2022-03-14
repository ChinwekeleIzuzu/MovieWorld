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
    $('#table').empty();
    $.ajax({
        url: '/movieworld/reviewed_select/',
        type:'POST',
        data:{"sort":option},
        success:function (results) {
            render(results)
        }
    }); 
}


function change(){
    var select = document.getElementById("select");
    var option= select.options[select.selectedIndex].value;
    $('#table').empty(); 
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
    $(result).each(function(i,v){
        $("#table").append('<tr>'+'<td>'+v[0]+'</td>'+'<td>'+v[1]+'</td>'+
            '<td>'+v[2] +'</td>'+'<td>'+v[3]+'</td>'+'<td>'+v[6] 
            +'</td>'+'<td>'+v[4]+'</td>'+'<td>'+v[5]+'</td>'+'</tr>'
        )
    })
}

