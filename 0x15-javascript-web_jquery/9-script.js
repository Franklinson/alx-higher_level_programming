$(document).ready(function () {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
    const helloTranslation = data.hello;

    $('#hello').text(helloTranslation);
  });
});
