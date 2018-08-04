
$(function() {
    console.log( "Page Loaded" );

    $(".event").each(function (index) {
        //Add expand functionality
        $expand_btn = $(this).find(".btn-expander");
        $expand_content = $(this).find(".description");
        $expand_btn.on("click", function(){
            $expand_content.slideToggle(function(){
                $expand_btn.toggleClass("collapsed expanded");
            });
        });

        //Add Go functionality
        console.log($(this));
        $go_btn = $(this).find(".btn-go");
        console.log($go_btn);
        $go_btn.on("click", function(){
            $(this).toggleClass("btn-going btn-not-going");
            console.log("clicked");
        });
    });
});