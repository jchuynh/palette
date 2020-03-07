"use strict";


    $('#search').select2({
    ajax: {
      url: '/search/tags-search', // Using JSON file at locally made route
      dataType: 'json',
      type: 'GET',
      results: (data) => {
          return {'term': data.term}
`<option value="${item}">${item}</option>`
    }
  });
;

// append, otp