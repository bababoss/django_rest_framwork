

        $(function () {

                var processed_json = new Array();   
                $.getJSON('http://127.0.0.1:8000/charts/03/2016/', function(data) {
                    // Populate series
                    for (i = 0; i < data.length; i++){
                        processed_json.push([data[i].days, data[i].user_id]);
                    }
                 
                    // draw chart
                    $('#container1').highcharts({
                    chart: {
                        type: "column"
					
                    },
                    title: {
                        text: "Employee Attendance Chart "
                    },
                    xAxis: {
                        type: 'category',
                        allowDecimals: false,
                        title: {
                            text: "Days"
                        }
                    },
                    yAxis: {
                        title: {
                            text: "Employee"
                        }
                    },
                    series: [{
	                    name: 'Number of Employee on this day:',
                        data: processed_json
						
                    }]
                }); 
            });
        });
