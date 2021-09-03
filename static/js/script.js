$(document).ready(function(){
    $(".sidenav").sidenav({edge: "right"});
    $('.modal').modal();
    $('select').formSelect();

    // Credit: Code Institute Mini Project > Adding a task> Materialize Form Validation https://www.youtube.com/watch?v=CG36uQtAzkU&t=279s&ab_channel=MediaUpload
    validateMaterializeSelect();
    function validateMaterializeSelect() {
        if ($("select.validate").prop("required")) {
            $("select.validate").css({ "display": "block", "height": "0", "padding": "0", "width": "0", "position": "absolute" });
        }
    }
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

function formReset() {
    document.getElementById("formAddRecipe").reset();
}
