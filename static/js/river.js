$(document).ready(function(){
$('.list-subscribe-btn').on('click', function(e) {
    e.preventDefault();


    riverName = $(this).siblings("h2").text();
    riverLevel = $(this).siblings(".single-level").text();


    $('.modal-rivername').text(riverName);
    $('.modal-riverlevel').text(riverLevel);
    $('.hiddenRiverName').val(riverName);

});

$('.admin-single-update').on('click', function(e) {
  e.preventDefault();
      parent_div = $(this).parent()
      txt_container = parent_div.siblings('.admin-single-sub-txt');
      riverName = txt_container.children('.admin_river_name').text();
      riverLevel = txt_container.children('.admin_river_level').text();
      $('.modal-rivername').text(riverName);
      levelStr = riverLevel.substr(riverLevel.indexOf(' ')+1);
      levelFloat = parseFloat(levelStr);
      levelInput = $('form').find('input[type=number]')
      levelInput.val(levelFloat);
      $('.hiddenRiverName').val(riverName);


});


$('.admin-single-delete').on('click', function(e) {
  e.preventDefault();
  parent_div = $(this).parent()
  txt_container = parent_div.siblings('.admin-single-sub-txt');
  riverName = txt_container.children('.admin_river_name').text();
  $('.modal-rivername').text(riverName);
  $('.hiddenRiverName').val(riverName);
  console.log(riverName);
});


if($(".alert").length > 0) {
  setTimeout(function(){
      $(".alert").delay(300).fadeOut();
  }, 3000)
}



});
