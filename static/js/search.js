"use strict";


$('#search').select2({
  ajax: {
    url: '/search-test', // Using JSON file at locally made route
    dataType: 'json',
    type: 'GET',
    results: function (term) {
                    return {
                        results: $.map(term.fields, function (field, i) {
                            return {
                                text: field.name,
                                children: $.map(field.children, function(child){
                                    return {
                                        id: child.id,
                                        text: child.name
                                    }
                                })
                            }
                        })
                    }
                }
          }}
      );


const searchTerm = document.getElementById("search").value;

$('#search').on('submit', () => {
  $.get('/search-form', {searchTerm: id}, (res) => {
    $('#search').html(res);
  });
});


