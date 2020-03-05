
// not sure how to implement this

$("#select2").select2({
    placeholder: "Select Option",
    minimumInputLength: 2,
    ajax: { 
        url: "/servletToGetMyData",
        dataType: 'json',
        data: function (term, page) { return { term: term }; },
        results: function (data, page) {  return { results: data.results} }
    },
    initSelection : function(element, callback){ callback(initialSelection); },     
    escapeMarkup: function (m) { return m; }
}); 