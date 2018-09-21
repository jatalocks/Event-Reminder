
$(function() {
    console.log( "Page Loaded" );

    //contact api (experimental)
    var settings = {
    "async": true,
    "crossDomain": true,
    url: "https://eventreminder-6487.restdb.io/rest/eventtable?q={}&max=5",
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
        console.log(data);
        
        var fData = []; //the formatted data

        for (var i = 0; i < 2; i++){
            console.log(data[i]);
            event = data[i];
            //find out the langues
            var _nameLgn = "he"
            var _locationLgn = "en";
            var _descriptionLgn = "he";

            //parse date
            var _day;
            var _month;
            var date = event.Date;
            date = date.split("-");
            monthNum = parseInt(date[1]);
            _day = date[2];

            //parse hours
            var _start = parseHour(event["Start Time"]);
            var _end = parseHour(event["End Time"]);

            function parseHour(input){
                if (input == "-"){
                    return "??"; 
                }
                var PM = input.includes("PM");
                if (PM){
                    input = input.replace(" PM", "");
                }
                else{
                    input = input.replace(" AM", "");
                }
                if (input.includes(":")){
                    if (!PM) return input;
                    else{
                        input = input.split(":");
                        return (parseInt(input[0]) + 12 + ":" + input[1]);
                    }
                }
                else{
                    if (PM)
                        input = parseInt(input) + 12;
                    
                    return input + ":00"; 
                }

            }

            switch(monthNum){
                case 1:
                    _month = "JAN";
                    break;
                case 2:
                    _month = "FAB";
                    break;
                case 3:
                    _month = "MAR";
                    break;                    
                case 4:
                    _month = "APR";
                    break;       
                case 5:
                    _month = "MAY";
                    break;       
                case 6:
                    _month = "JUN";
                    break;       
                case 7:
                    _month = "JUL";
                    break;
                case 8:
                    _month = "AUG";
                    break;       
                case 9:
                    _month = "SEP";
                    break;       
                case 10:
                    _month = "OCT";
                    break;       
                case 11:
                    _month = "NOV";
                    break;       
                case 12:
                    _month = "DEC";
                    break;                    
                }


            //
            fData[i] = 
            {
                name: event.Name,
                nameLgn: _nameLgn,
                location: event.Address,
                locationLgn: _locationLgn,
                date: {day: _day, month: _month}, 
                hours: {start: _start, finish: _end},
                description: event.Description,
                descriptionLgn: _descriptionLgn,
                category: "No-Category", 
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
            $go_btn.click(function(){
                //open the dialog window
                $("#go-dialog").css("display", "block");
                //$(this).toggleClass("btn-going btn-not-going");
            });

            //Add close button functionality
            $close_btn = $(".close");
            $close_btn.click(function(){
                $close_btn.parent().parent().css("display", "none");
            });
            $("#go-dialog").click( function(event){
                $(this).css("display", "none");
            });
            $(".go-dialog-content").click(function(event){
                event.stopPropagation();
            })

        });

    }
    

});