var fixture;

describe('Toggle view between "name search" and "advanced search" option', function() {

    beforeEach(function () {
        loadFixtures('fixtures.html');
        fixture = $('#my-fixture1');
    });
    
    afterEach(function () {
        $('#my-fixture1').remove();
    });

    it('should be defined', function() {
        expect(fixture).toBeDefined();
    });

    it('should have default view of "name search"', function() {
        expect($('#search_name')).not.toHaveClass('hide')
        expect($('#advanced_btn')).not.toHaveText('SEARCH BY NAME')
        expect($('#advanced_form')).toHaveClass('hide')
        expect($('#advanced_btn')).toHaveText('ADVANCED SEARCH')
    });

    it('should change view based on the click event', function() {
        $('#advanced_btn').click(function() {
            $('#advanced_form').toggleClass('hide');
            $(this).text($(this).text() == 'ADVANCED SEARCH' ? 'SEARCH BY NAME' : 'ADVANCED SEARCH'
            );
            $('#search_name').toggleClass('hide');
        });

        var spyEvent = spyOnEvent('#advanced_btn', 'click');
        $('#advanced_btn').click();
        expect('click').toHaveBeenTriggeredOn('#advanced_btn');
        expect(spyEvent).toHaveBeenTriggered();

        expect($('#advanced_form')).not.toHaveClass('hide')
        expect($('#advanced_btn')).not.toHaveText('ADVANCED SEARCH')
        expect($('#search_name')).toHaveClass('hide')
        expect($('#advanced_btn')).toHaveText('SEARCH BY NAME')

        $('#advanced_btn').click();
        expect($('#search_name')).not.toHaveClass('hide')
        expect($('#advanced_btn')).not.toHaveText('SEARCH BY NAME')
        expect($('#advanced_form')).toHaveClass('hide')
        expect($('#advanced_btn')).toHaveText('ADVANCED SEARCH')
    });
                    
});

describe('A text link which enables user to go back to previous view', function() {
    
    beforeEach(function () {
        loadFixtures('fixtures.html');
        fixture = $('#my-fixture2');
    });
    
    afterEach(function () {
        $('#my-fixture2').remove();
    });

    it('should be defined', function() {
        expect(fixture).toBeDefined();
    });

    it('should hide current view and show previous one', function() {
        $('.step-back').click(function() {
            $('#form_validation').hide();
            $('#name_validation').show();
        });

        var spyEvent = spyOnEvent('.step-back', 'click');
        $('.step-back').click();
        expect('click').toHaveBeenTriggeredOn('.step-back');
        expect(spyEvent).toHaveBeenTriggered();

        expect($('#form_validation')).toBeHidden()
        expect($('#name_validation')).not.toBeHidden()
    });
        
});
    