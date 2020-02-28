$(document).ready(function(){
    var tags=[];

    function searchTags() {
        $.getJSON("/tags", function(data, status, xhr) {
            for (var i = 0; i < data.length; i++) {
                tags.push(data[i].name);
        }

});
};

searchTags();

$("#tag").autocomplete ({
    source: tags,
    });

});