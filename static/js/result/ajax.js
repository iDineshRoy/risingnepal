$(function(){
    $('#year-option').change(function(){
        $.ajax({
            type: 'POST',
            url: "/get-classes/",
            data: {
                'get-year': $('#year-option').val(),
                'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
            },
            success: searchClasses,
            dataType: 'html'
        });
    });
});
function searchClasses(data)
{
    var city = document.getElementById('search-classes');
    
    var town = document.getElementById('search-terms');
    $(town).empty();
    $('#search-results').html(data);
}