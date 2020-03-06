"use strict";

$(".search").select2({
    placeholder: "Search options..."
  ajax: {
    url: "tags.json", // Using JSON file at locally made route
    dataType: "json",
    type: "GET",
    results: function (data) {
        // Need to return in format in order to use Select2
        return {results: data}
    },
    data: function (term) {
        return q: term
    }
  }
});

// $(".search").on("submit", function(evt){
//     $.ajax({
//         data: {
//             tag : $("#tag").val()
//         },
//         type: "POST",
//         url: "/process"
//     })
// });