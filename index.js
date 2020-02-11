var bin = document.querySelectorAll('.binary');

[].forEach.call(bin, function(el) {

  el.dataset.binary = Array(4096).join(el.dataset.binary + ' ')

});

var currentdate = new Date().getTime();