"use strict";

$(document).ready(function() {

    jQuery.validator.addMethod("t8", function(value, element) {
        return this.optional(element) || value.length <= 8;
    }, "Tier8 keywords must be no longer than 8 symbols");

    jQuery.validator.addMethod("t9p", function(value, element) {
        return this.optional(element) || value.length <= 9;
    }, "Tier9+ keywords must be no longer than 9 symbols");

    jQuery.validator.addMethod("t10p", function(value, element) {
        return this.optional(element) || value.length <= 10;
    }, "Tier10+ keywords must be no longer than 10 symbols");

    $("#id_tier").on("change", function(){
        /* Revalidate id_keyword */
        $('#id_keyword').removeData("previousValue").valid();
    });

    $("#orderform").validate({
        rules: {
            keyword: {
                required: true,
                t8: {depends: function(element) {return $("#id_tier").val() == "tier8" }},
                t9p: {depends: function(element) {return $("#id_tier").val() == "tier9+" }},
                t10p: {depends: function(element) {return $("#id_tier").val() == "tier10+" }},
            }
        }
  // 		submitHandler: function(form) {
		// 	// $("#submit").addClass("loading");
        //     form.submit();
        // }
    });

});


$(function() {


});
