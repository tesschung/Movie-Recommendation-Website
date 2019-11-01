# Project_08: 




1. 사진 api 로 배경화면 불러오기 및 설정

```html
  <script>
  // 1. Axios 로 image url을 가져온다.
  // const axios = require('axios')
  const url = 'https://source.unsplash.com/1920x1080/?nature,night'

  axios.get(url)
  .then(function(response) {
    console.log(response)
    const body = document.querySelector('body')
    const imageUrl = response.request.responseURL
    body.background = imageUrl
    // body.position = 'relative'
    console.log(imageUrl) 
  }) 
  </script>
```



2. 시간이랑 문구 JS 로 Element 생성하여 삽입
     • `new Date()` 시간객체 생성  new Date().toLocaleTimeString()   => "오전 9:25:54" 

     ```html
    const clock = document.querySelector('#clock')
       console.log(clock)
       clock.style= 'color:white; font-size:120px; text-align:center; font-family: Nanum Gothic, sans-serif; margin-top:200px; font-weight: bold; letter-spacing: -2px;'
       function showClock() {
         const now = new Date()
         const hour = now.getHours()
         const minute = now.getMinutes()
         const second = now.getSeconds()
         clock.innerHTML = `${hour < 10 ? `0${hour}` : hour}:${minute < 10 ? `0${minute}` : minute}:${second < 10 ? `0${second}` : second}`
       }
       function init() {
         showClock()
         setInterval(showClock, 1000)
       }
       init()
    ```
    
     
    
     • hh:mm 형태로 시간 표현



3. Todo 기능 구현 (advanced)

```html
  button.addEventListener('click', event =>
  {
    const li = document.createElement('li')

    if ( input.value === '' ){
      alert('write your thoguhts')
      return
    }
    
    const deleteButton = document.createElement('Button')
    li.innerText = input.value
    li.style="color: white;"
    deleteButton.innerText = 'delete'

    ul.insertBefore(li, ul.firstElementChild)
    li.appendChild(deleteButton, li.deleteButton)

    deleteButton.addEventListener('click', (event) => {
      fin = confirm('정말로 삭제하시겠습니까?') // 확인시 true 취소시 false
      if (fin === true) {
        li.remove()
      }
    })

  })

```



4. 날씨 API 통해서 오늘의 날씨 불러온 뒤 출력 

```html
let p = document.querySelector('p')
  const weatherDataURL = 'http://api.openweathermap.org/data/2.5/weather?q=Seoul,KR&APPID=cb5b4ab8957d35f370cc1bdd030b1cca'
  axios.get(weatherDataURL)
  .then(function(response){
  console.log(response)
  const weatherCity = response.data.name
  const weatherData = response.data.weather[0].description
  const temperature = (response.data.main.temp - 273.15).toFixed()
  console.log(weatherData)
  p.innerText = `${temperature}°C ${weatherCity} ${weatherData}`
  })

```





https://source.unsplash.com/1920x1080/?nature,ocean