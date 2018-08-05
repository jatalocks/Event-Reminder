$(function(){
    var data = 
    {
        name: "פארק השלג",
        nameLgn: "he",
        location: "Tel Aviv 63508",
        locationLgn: "en",
        date: {day: 10, month: "SEP"}, 
        hours: {start: "10:30", finish: "18:30"},
        description: "This is the event's description. <br> Here is another line. ",
        category: "Parks!", 
        categoryColor: "#4286f4",
        image: "img/demo/snowpark.jpg", 
        going: false
    }
    var rendered = new EJS({url: "events.ejs"}).render(data);
    $("#events").html(rendered);
    
  });