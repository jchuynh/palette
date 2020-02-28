

$(document).ready(function(){
    $("#search").on("submit", function(evt) {
    $.ajax({
        data: {
            tag:$("#tag").val()
        },
        type: "POST",
        url: "/process"
    })
    .done(function(data1){
        if (data1.error){
            $("#result").text(data.error).show();
        }
        else {
            $("#result").html(data.tag).show()
        }
    })

    evt.preventDefault();
});
})


$(document).ready(function(){
    var tags=[];

    function searchTags() {

        // double check input 

        $.getJSON("/tags", function(data) {
            for (var i = 0; i < data.length; i++) {
                tags.push(data[i].tag);
        }

});
};

searchTags();

$("#tag").autocomplete({
    source: tags,
    });

});
