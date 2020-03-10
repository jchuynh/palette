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




// $('#search').on('submit', () => {
//   const searchTerm = document.getElementById("search").value;
//   $.post('/search-form', {searchTerm: }, (res) => {
//     $('#search').html(res);
//   });
// });


// (function (data) {
//   // Here we should have the data object
//   $option.text(data.text).val(data.id); // update the text that is displayed (and maybe even the value)
//   $option.removeData(); // remove any caching data that might be associated
//   $select.trigger('change'); // notify JavaScript components of possible changes
// });


