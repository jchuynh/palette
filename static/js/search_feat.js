"use strict";

// <script type="text/javascript">
// $(document).ready(function() {
//   $("#search").select2({
//     ajax: {
//       url: "/tags-test",
//       dataType: 'json',
//       data: function(term) {
//         return {
//           q: term.term
//         };
//       },
//       processResults: function(data) {
//         return {
//           results: $.map(data.items, function(item, index) {
//             return {
//               'id': item.id,
//               'text': item.name
//             };
//           })
//         };
//       }
//     }
//   });
// });




// $('#search').select2({
//   ajax: {
//     url: '/search-test',
//     dataType: 'json',
//     processResults: function(data) {
//       data = data.map(i => {
//         i.children = i.children.map(j => ({ ...j, group: i.text }))
//         return i
//       })
//       return { results: data };
//     }
//   },
//   placeholder: 'Select an option',
//   templateSelection: function(data) {
//     let label = data.group ? data.group + ' - ' : '';
//     return label + data.text;
//   }
// });






<script type="text/javascript">
  $('#search').select2({
    ajax: {
      url: '/search-test', // Using JSON file at locally made route
      dataType: 'json',
      minimumInputLength: 3,
      type: 'GET',
      // data: function(term) {
      //     // Need to return in format in order to use Select2
      //     return {'term': term.term};
      // },
       processResults: function(term) {
        return {
          results: $.map(term.items, function(item, index) {
            return {
              'id': item.id,
              'text': item.name
            };
          })
        };
      }}
  });






