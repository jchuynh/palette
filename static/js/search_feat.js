"use strict";

<script type="text/javascript">
$(document).ready(function() {
  $("#search").select2({
    ajax: {
      url: "/tags.json",
      dataType: 'json',
      data: function(term) {
        return {
          q: term.term
        };
      },
      processResults: function(data) {
        return {
          results: $.map(data.items, function(item, index) {
            return {
              'id': item.id,
              'text': item.name
            };
          })
        };
      }
    }
  });
});