$(document).ready(function(){
    
    $('.sidenav').sidenav();
    $('select').formSelect();

    $('#advanced_btn').click(function(){
        $('#advanced_form').toggleClass('hide');
        $('#advanced_btn').toggleClass('grey-text');
      });

  });