
// AJAX for populating items

$(document).ready(function(){
    // On submit start the function
    $("#search").on("submit", function(evt) {
        $.ajax({
            data: {
              tag : $("#tag").val()
        },
        type: "POST", // Request type
        url: "/process" // Route to send to
    })
    .done(function(data){
        if (data.error){
            $("#result").text(data.error).show();
        }
        else {
            $("#result").html(data.tag).show();
        }
    })

    evt.preventDefault();
});
})


$(document).ready(function(){
    var tags=[];

    function searchTags() {

        // Get the JSON information from the /tags URL
        $.getJSON("/tags", function(data) {
            // Start at the first element
            // If the first element is not the last one
            // Increment by 1 
            for (var i = 0; i < data.length; i++) {
                // Show the element
                tags.push(data[i].tag);
        }

});
};

searchTags();

// Using jQuery to to autocomplete the search box as a drop-down
$("tag").autocomplete({
    lookup: tags,
});


















