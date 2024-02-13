$(document).ready(function(){
    // Add an event listener to the anchor link to open the modal
    $('a[data-bs-toggle="modal"]').on('click', function(){
        var target_modal = $(this).attr('data-bs-target');
        $(target_modal).modal('show');
    });
});
