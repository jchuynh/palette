"use strict";


    $('#search').select2({
    ajax: {
      url: '/search-test', // Using JSON file at locally made route
      dataType: 'json',
      type: 'GET',
      results: (data) => {
          return {'term': data.term}
`<option value="${item}">${item}</option>`
    }
  });
;

// append, otp

      // data: function(term) {
      //     // Need to return in format in order to use Select2
      //     return {'children': term};
      // },

      // data: function (params) {

      //       var queryParameters = {
      //           q: params.term
      //       }
      //       return queryParameters;

<script type="text/javascript">
  $(document).ready(function() {
  $('#search').select2({
    multiple: true,
    minimumInputLength: 1,
    tokenSeparators: [" "],
    ajax: {
      url: '/search-test', // Using JSON file at locally made route
      dataType: 'json',
      type: 'GET',
      data: function () {
    return {
        json: JSON.stringify(data)
    }
},
      results: function (data, page) {
      return {
          results: $.map(data.fields, function (field, i) {
              return {
                  text: field.text,
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
      // data: function(term) {
      //     // Need to return in format in order to use Select2
      //     return {'children': term};
      // },
  }
  });
  });

</script>

 <input type="hidden" class="search-result-box" />


// const data = {
//     id: 0,
//     text: 'Barn owl'
// };

// const newOption = new Option(data.text, data.id, false, false);
// $('#mySelect2').append(newOption).trigger('change');

// $.each(data, function(index, value) {
//   $('#selectId').append(
//     '<option value="' + data[index].id + '">' + data[index].value1 + '</option>'
//   );
// });

      results: function (data, page) {
      return {
          results: $.map(data.fields, function (field, i) {
              return {
                  text: field.text,
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