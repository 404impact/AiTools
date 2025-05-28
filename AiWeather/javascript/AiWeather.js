import { GoogleGenerativeAI } from "@google/generative-ai";

// Access environment variables from window.ENV
const open_api = window.ENV?.OPENWEATHER_API_KEY 
const aqicn_api = window.ENV?.AQICN_API_KEY 
const gemini_key = window.ENV?.GEMINI_API_KEY 

const getweatherinfo = (lat, long, aqicn_url, gemini_key, open_api) => {

    // gemini related stuffs
    const genAI = new GoogleGenerativeAI(gemini_key);
    const gemini_run = async (temperature, feels, city, weather, aqi, query_text) => {
    // For text-only input, use the gemini-pro model
    const model = genAI.getGenerativeModel({ model: "gemini-2.0-flash"});
    const prompt = `
        taking the following weather data into consideration:
        current temperature: ${temperature}
        feels like temperature: ${feels}
        name of the city: ${city}
        current weather condition: ${weather}
        air quality index: ${aqi}
        based on the question: ${query_text} generate your response in not more than 100 words. If question you received is an empty text, just say that you need a question to answer and refrain from saying anything else. Use emojis whenever required and generate a funny response.
        `
    const result = await model.generateContent(prompt);
    const response = await result.response;
    const text = response.text();
    console.log(query_text)
    // document.write(text)
    // console.log(text);
    document.getElementById("weather-description").innerHTML = text
    }

// weather related stuffs beings from here

    const url = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${long}&appid=${open_api}&units=metric`

    // fetch weather data
    fetch(url)
        .then(response => {
            return response.json();
        })

        .then(data => {
            
            let current_temperature = data['main']['temp']
            let feels_like = data['main']['feels_like']
            let city_name = data['name']
            let weather_condition = data['weather'][0]['description']

            get_basicinfo(current_temperature, feels_like, city_name, weather_condition)
        })

 const get_basicinfo = (current_temperature, feels_like, city_name, weather_condition) => {
        fetch(aqicn_url)
        .then(response => {
            return response.json();
        })
        .then(data => {
            let aqi = data['data']['aqi']
            let element = [".temp", ".feels-like", ".city", ".condition", ".aqi"]
            let weatherinfo = [current_temperature, feels_like, city_name, weather_condition, aqi]

            for(let i = 0; i < element.length; i++){
                let selector = document.querySelector(element[i]);
                selector.textContent += weatherinfo[i]
            }
            const generate_text = () =>{
                let query_text = document.getElementById("query-txt").value
                gemini_run(current_temperature, feels_like, city_name, weather_condition, aqi, query_text)
            }
            document.getElementById("query-btn").addEventListener("click", () =>{generate_text()});

        })
    }


}

// get current location on button press
const getcoords = () => {
    navigator.geolocation.getCurrentPosition(position => {
        let lat = position.coords.latitude;
        let long = position.coords.longitude;
        const aqicn_url = `https://api.waqi.info/feed/geo:${lat};${long}/?token=${aqicn_api}`
        getweatherinfo(lat, long, aqicn_url, gemini_key, open_api)
    })
}

// get location throgh text box
const start = () => {
    // let unit = "metric"
    let city = document.getElementById("location-name").value

// use api key in URL
    const aqicn_url = `https://api.waqi.info/feed/${city}/?token=${aqicn_api}`
    const geocode = `http://api.openweathermap.org/geo/1.0/direct?q=${city},&limit=1&appid=${open_api}`

    fetch(geocode)
    .then(response => {
        return response.json()
    })

    .then(data => {
        console.log(data);
        let lat = data[0]['lat']
        let long = data[0]['lon']
        getweatherinfo(lat, long, aqicn_url, gemini_key, open_api);

        
    })
}

document.getElementById("fetchinfo").addEventListener("click", () =>{start()});
document.getElementById("current-location").addEventListener("click", () => {getcoords()});
