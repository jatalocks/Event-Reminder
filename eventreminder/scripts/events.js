$(function(){
    var data = 
    {
        events: 
        [        
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
            },
            {
                name: "When You Dance",
                nameLgn: "en",
                location: "Haifa, Hastudio",
                locationLgn: "en",
                date: {day: 23, month: "AUG"}, 
                hours: {start: "20:30", finish: "??"},
                description: "The first production of a musical show with original music and lyrics by Shachar Har-Shuv, co-written and choreographed by Adi Ronai.<br> Directed by Jonathan Szwarc, teacher and manager of the acting school \"Hastudio\" in haifa. ",
                category: "Shows", 
                categoryColor: "red",
                image: "https://scontent.ftlv6-1.fna.fbcdn.net/v/t1.0-9/36707879_2140444062693330_3627007294862000128_o.jpg?_nc_cat=0&oh=9d5942075e91a90353538b2b26d4f217&oe=5C0F68F2", 
                going: true
            }, 
        ]
    }
    var rendered = new EJS({url: "events.ejs"}).render(data);
    $("#events").html(rendered);
    
  });