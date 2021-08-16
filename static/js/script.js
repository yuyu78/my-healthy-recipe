$(document).ready(function(){
    $(".sidenav").sidenav({edge: "right"});
    $('.modal').modal();
    $('select').formSelect();
  });

(function () {
    if (typeof EventTarget !== "undefined") {
        let func = EventTarget.prototype.addEventListener;
        EventTarget.prototype.addEventListener = function (type, fn, capture) {
            this.func = func;
            if (typeof capture !== "boolean") {
                capture = capture || {};
                capture.passive = false;
            }
            this.func(type, fn, capture);
        };
    };
}());

// If "cancel" button is clicked, remove the attribute "required"
