/* 
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

function setTable(what){
    if(document.getElementById(what).style.display=="none"){
        document.getElementById(what).style.display="block";
    }else if(document.getElementById(what).style.display=="block"){
        document.getElementById(what).style.display="none";
    }
}

function toggle(id) {
       var e = document.getElementById(id);
       if(e.style.display == '')
          e.style.display = 'none';
}

function display_rows(tableID){
    var table = document.getElementById(tableID);
    var rows = table.getElementsByTagName('tr');
    for(var i = 0; i < rows.length; i++){
        if (rows[i].style.display =='none'){
            rows[i].style.display ='';
        }
    }
}