
$(function() {
    console.log( "Page Loaded" );

    //contact api (experimental)
    var settings = {
    "async": true,
    "crossDomain": true,
    url: "https://eventreminder-6487.restdb.io/rest/eventtable",
    type: "GET",
    "headers": {
        "content-type": "application/json",
        "x-apikey": "5b63fd04b0c070454e5b8ed3",
        "cache-control": "no-cache"
        },
    success: loadContent,
    complete: InitializeFunctionality
    }
    $.ajax(settings);

    function loadContent(data){
        var fData = []; //the formatted data

        for (var i = 0; i < 2; i++){
            event = data[i];
            //find out the langues
            var _nameLgn = "he"
            var _locationLgn = "en";

            //decipher date
            var _day;
            var _month;

            //
            fData[i] = 
            {
                name: event.Name,
                nameLgn: _nameLgn,
                location: event.Address,
                locationLgn: _locationLgn,
                date: {day: 10, month: "SEP"}, 
                hours: {start: "10:30", finish: "18:30"},
                description: "This is the event's description. <br> Here is another line. ",
                category: "Parks!", 
                categoryColor: "#4286f4",
                image: event.Image, 
                going: false
            }
        }

        //render formatted content to page
        var rendered = new EJS({url: "events.ejs"}).render({events: fData});
        $("#events").html(rendered);

        //remove "loading sign"
        $("#loading").addClass("invisible");

    }

    function InitializeFunctionality(){
        $(".event").each(function (index) {
            //Add expand functionality
            $expand_btn = $(this).find(".btn-expander");
            var $expand_content = []; //we use an array so we can differ between different description objects of different events, though I am pretty sure there must be a better way to do this. 
            $expand_content[index] = $(this).find(".description");
            $expand_btn.on("click", function(){
                    $expand_content[index].slideToggle();        
                    $(this).toggleClass("collapsed expanded");
                    
                });
            
    
            //Add Go functionality
            $go_btn = $(this).find(".btn-go");
            $go_btn.on("click", function(){
                $(this).toggleClass("btn-going btn-not-going");
            });
        });

    }
    

});