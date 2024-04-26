import alfy from 'alfy';

// 获取天气信息
const API_KEY = '526909f489a8449080f460bd3d14ad2a';
// 皇姑区
const query = '101070110'; 
// https://geoapi.qweather.com/v2/city/lookup?location=shenyang&key=526909f489a8449080f460bd3d14ad2a
const url = 'https://devapi.qweather.com/v7/weather/now?location=' + query + '&key=' + API_KEY;

const data = await alfy.fetch(url);

/**
 *
{
  code: '200',
  updateTime: '2024-04-26T11:43+08:00',
  fxLink: 'https://www.qweather.com/weather/huanggu-101070110.html',
  now: {
    obsTime: '2024-04-26T11:40+08:00',
    temp: '19',
    feelsLike: '18',
    icon: '101',
    text: '多云',
    wind360: '122',
    windDir: '东南风',
    windScale: '2',
    windSpeed: '6',
    humidity: '48',
    precip: '0.0',
    pressure: '1001',
    vis: '30',
    cloud: '91',
    dew: '8'
  },
  refer: { sources: [ 'QWeather' ], license: [ 'CC BY-SA 4.0' ] }
 }
*/

const tq = data.now.text;
const wd = data.now.temp;
const icon = data.now.icon;

const result = tq + ' ' + wd + '℃' + ' ' + data.now.windDir;
const iconPath = "./images/" + icon + ".png";

// 打印天气信息
// console.log(data);
// console.log(result);
// console.log(iconPath);

const items = [{
		"title": result,
		"subtitle": data.now.obsTime,
        "icon": {
            "path": iconPath
        },
		"arg": result
}]

alfy.output(items);

