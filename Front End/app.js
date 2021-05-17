// Need to add d3 JSON to collect data
    // Feel free to change or delete any of the code you see in this editor!
    var svg = d3.select("body").append("svg")
      .attr("width", 960)
      .attr("height", 500)

    d3.json('https://jsonplaceholder.typicode.com/posts', {
      method:"POST",
      body: JSON.stringify({
        //   Below would the "names" (use d3 query to grab them)
        // title: 'Hello',
        // body: '_d3-fetch_ is it',
        // userId: 1,
        // friends: [2,3,4]
        
      }), 
      headers: {
        "Content-type": "application/json; charset=UTF-8"
      }
    })
    .then(json => {
     svg.append("text")
      .text(JSON.stringify(json))
      .attr("y", 200)
      .attr("x", 120)
      .attr("font-size", 16)
      .attr("font-family", "monospace")
    });

    positions['cf'] = d3.select('.cf').text()
    positions['ktch'] = d3.select('.ktch').text()
    positions['car'] = d3.select('.car').text()
    positions['year'] = d3.select('.year').text()
    positions['f1'] = d3.select('.f1').text()
    positions['cond'] = d3.select('.cond').text()
    positions['fbath'] = d3.select('.fbath').text()
    positions['bed'] = d3.select('bed').text()
    positions['f2'] = d3.select('.f2').text()
    positions['lot'] = d3.select('.lot').text()
    positions['hbath'] = d3.select('.hbath').text()

    filter_list = Object.values(positions).filter(item => item.length > 1)