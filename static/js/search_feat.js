
$(".search").select2({
    placeholder: "Search options..."
  ajax: {
    url: "tags.json"
    dataType: "json",
    type: "GET",
    results: function (data) {
        return {results: data}
    },
    url: "tags.json",
    data: function (term) {
        return q: term
    }
  }
});

console.log(data)