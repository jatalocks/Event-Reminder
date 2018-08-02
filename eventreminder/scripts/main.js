
$(function() {
    console.log( "Page Loaded" );

    $(".event").each(function (index) {
        //Add expand functionality
        $expand_btn = $(this).find(".btn-expander");
        $expand_content = $(this).find(".description");

        $expand_btn.on("click", function(){
            $expand_content.slideToggle();
        });
    });
});