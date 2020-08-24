(function(documents { 
  var toggle = document.querySelector('.sidebar-toggle');
  var sidebar = document.querySelector('#sidebar')
  var checkbox = document.querySelector(#sidebar-checkbox');
  
  document.addEventListener('click', function(e) {
    var target = e.target;
    
    if(!checkbox.checked ||
        sidebar.contains(target) ||
        (target === checkbox || target === togle)) return;
        
    checkbox.checked = false;
    } false);
  })(document);
