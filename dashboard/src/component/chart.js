import React, { Component } from 'react'
import Highcharts from 'highcharts';
import HighchartsReact from 'highcharts-react-official';
import chartDataService from '../services/chart.service';


class Chart extends Component {
	constructor(props) {
		super(props)
		this.state = {
			options: {	
				chart: {
			    	zoomType: 'xy'
			    },		
				xAxis: [{
	                type: 'datetime',
	                labels: {
	                    formatter: function () {
	                        return Highcharts.dateFormat('%b /%y', this.value);
	                    }
	                },
		            crosshair: true
				}],
	            yAxis: [{ // Primary yAxis
	            	labels: {
			            style: {
			                color: Highcharts.getOptions().colors[1]
			            },
			            enabled: false

			        },
                	title: {
                    	text: null,
                    	style: {
			                color: Highcharts.getOptions().colors[1]
			            }
                	}
	            },
				// Secondary yAxis
	            { 
			        title: {
        	            text: 'Number of People',
			        },
			        labels: {
			            style: {
			                color: Highcharts.getOptions().colors[0]
			            }
			        },
			    }],
			    tooltip: {
			        shared: true
			    },
				series: [
					{
						name: 'Total Cases',
						type: 'spline',
						yAxis: 1,
						data: [],
					},
					{
						name: 'Total Death',
						type: 'column',
	        			yAxis: 1,
						data: [],
					}
				]
			}
		};
		this.initdata = this.initdata.bind(this)
	}
	async initdata() {
		const options = await chartDataService(this.state.options)
		this.setState({
		  options
		});
	}
	componentDidMount() {
		this.initdata()
	}

	render() {
		return (
			<div>
				<HighchartsReact highcharts={Highcharts} options={this.state.options} />
			</div>
		)
	}
}

export default Chart;