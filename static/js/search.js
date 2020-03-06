

$("form").on("submit", function(evt){
    $.ajax({
        data: {
            tag : $("#tag").val()
        },
        type: "POST",
        url: "/process"
    })
});


$(document).ready(function(){
    var tags=[];

    function searchTags() {
        $.getJSON("/tags", function(data) {
            for (var i = 0; i < data.length; i++) {
                tags.push(data[i].name);
        }

    // function searchTitle() {
    //     $.getJSON("/title", function(data) {
    //         for (var i = 0; i < data.length; i++) {
    //             tags.push(data[i].name);
    // }

    // function searchArtist() {
    //     $.getJSON("/artist", function(data) {
    //         for (var i = 0; i < data.length; i++) {
    //             tags.push(data[i].name);
    // }

    // function searchMedium() {
    //     $.getJSON("/medium", function(data) {
    //         for (var i = 0; i < data.length; i++) {
    //             tags.push(data[i].name);
    // }

});
};

searchTags();

$("#tag").autocomplete ({
    source: tags,
    });

});