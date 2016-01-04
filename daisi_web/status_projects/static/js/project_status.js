function yearSessions(document) {
    $(document).ready( function() {
        $('[type="year"]').click(function() {
            year = $(this).attr('data');
            $('#panel-year-' + year).load('{% url status/2014 %}'.replace("year",year));
//            $('#panel-year-' + year).load('http://127.0.0.1:8000/status/2014/');
        });
    });
}

function sessionStatus() {
    $('[type="session"]').click(function() {

    });
}