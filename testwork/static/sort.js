$('body').on('click', '#cpu_usage th', function() {
    var field = $(this).text();
    curr_field  = $('#cpu_usage').data('sort-field');
    direction = curr_direction  = $('#cpu_usage').data('sort-direction');
    if (curr_field == field) {
        direction = curr_direction == 'asc' ? 'desc' : 'asc';
    }
    $.post(location.href, {field: field, direction: direction}).done(function(response){$('#cpu_usage').replaceWith(response)});
});