function rechercherDansTable() { 
    var input, filter, table, tr, td, i, txtValue; 
    input = document.getElementById("recherche"); 
    filter = input.value.toUpperCase(); 
    table = document.getElementById("tableDonnees"); 
    tr = table.getElementsByTagName("tr"); 
    
    for (i = 1; i < tr.length; i++) { 
      tr[i].style.display = "none"; 
      td = tr[i].getElementsByTagName("td"); 
      for (var j = 0; j < td.length; j++) { 
        if (td[j]) { 
          txtValue = td[j].textContent || td[j].innerText; 
        if (txtValue.toUpperCase().indexOf(filter) > -1) { 
          tr[i].style.display = ""; 
          break; 
        } 
      } 
    } 
  } 
} 
