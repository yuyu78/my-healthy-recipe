$(document).ready(function(){
    // jQuery sections from Materalize
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

// Credit: Stackoverflow https://stackoverflow.com/questions/46094912/added-non-passive-event-listener-to-a-scroll-blocking-touchstart-event/55388961#55388961
// To avoid error message
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
    }
}());

function formReset() {
    document.getElementById("formAddRecipe").reset();
}
