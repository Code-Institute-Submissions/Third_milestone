$(document).ready(function(){
    
    // Initialization of side navigation for mobile devices
    $('.sidenav').sidenav();
    
    // Initialization of select form input
    $('select').formSelect();

    // Initialization of collapsible accordion element
    $('.collapsible').collapsible();

    // Acivation of dropdown menu element
    $(".dropdown-trigger").dropdown();

    // Character counter for text inputs
    $('input#username, textarea#textarea, input#name_input, input#region_input, textarea#textarea1').characterCounter();

    $('#advanced_btn').click(function() {
        $('#advanced_form').toggleClass('hide');
        $('#advanced_btn').toggleClass('grey-text');
        $(this).text($(this).text() == 'Advanced search' ? 'Search by name' : 'Advanced search'
        );
        $('#search_name').toggleClass('hide');
    });

  });