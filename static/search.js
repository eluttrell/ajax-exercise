$(function() {
  $('#search-form').submit(function(event) {
    event.preventDefault();
    var serialData = $('form#search-form').serialize();
    $.get('/search', serialData, function(data) {
      $('ul#result-list').html('');
      for (var i = 0; i < data.length; i++) {
        $('ul#result-list').append('<li>Title: ' + data[i].title + '</li><li>URL: <a href="' + data[i].url + '">' + data[i].url + '</a></li>')
      }
    }, 'json')
  });

})
