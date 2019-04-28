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
    $('input#username, input#name_input, textarea#textarea1').characterCounter();

    // Toggle between search and advance search view
    $('#advanced_btn').click(function() {
        $('#advanced_form').toggleClass('hide');
        $(this).text($(this).text() == 'ADVANCED SEARCH' ? 'SEARCH BY NAME' : 'ADVANCED SEARCH'
        );
        $('#search_name').toggleClass('hide');
    });

});