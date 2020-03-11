"use strict";


$('#search_id').select2({
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
          }
        }
      );


$('#search_form').on('submit', (evt) => {
  console.log(evt.target.innerHTML)
  evt.preventDefault();
  const data = {
    'text': $("#search_id").children()[0].label};
    console.log(data);
  $.get('/search-results', data, (res) => {
    console.log(res);
     
    if (res.type == "artist" || res.type == "tag"){
      for (let art of res.artworks) {
        $('#search').append(`
          <a href="/artwork/${art.art_id}">
          <img src="/${art.url}" class="gallery-crop" alt=${art.art_id}/>
          </a>`);
}
    if (res.type === "title") {
          `<a href="/artwork/${res.artwork_id}">
           <img src="/${res.art_thumb}" class="gallery-crop" alt=${res.artwork_id}/>
           </a>`;
        
        }
      }    
    });
  });




