import axios from 'axios';


export default async (defaultoptions) => {
  return new Promise((resolve, reject) => {
    axios.get(`http://127.0.0.1:8080/covid19`)
      .then(response => {
        // handle success
        const options = JSON.parse(JSON.stringify(defaultoptions))
        // date_vs_cases
        const series_1 = []
        Object.keys(response.data.date_vs_case).forEach(key=> {
          const cases = []
          cases.push(new Date(key).getTime());
          cases.push(response.data.date_vs_case[key])
          series_1.push(cases);
        })
        options.series[0].data = series_1
        // date_vs_death
        const series_2 = []
        Object.keys(response.data.date_vs_death).forEach(key=> {
          const death = []
          death.push(new Date(key).getTime());
          death.push(response.data.date_vs_death[key])
          series_2.push(death);
        })
        options.series[1].data = series_2
        return resolve(options)
      });
  });
}