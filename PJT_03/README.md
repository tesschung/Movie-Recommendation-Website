

## Project_03: 

## Web(HTML/CSS를 활용한 웹 사이트 구성)

`python 3.7`

[TOC]



#### Overview

Web(HTML/CSS를 활용한 웹 사이트 구성)



#### Requirements

1. HTML/CSS 환경 구성

2. 웹 페이지를 위한 Assets 다운로드
    index.html 에 마크업을 작성
    layout.css 를 작성
    reboot.css 는 브라우저 기본 설정 CSS를 모두 동일하게 설정하기 위해 사용
    style.css 는 기본으로 제공되는 CSS 활용
    images 폴더에는 활용할 포스터 이미지

  

#### Goal

HTML/CSS 환경 구성



#### Developement Method

```css
/* header */
header {
  /* 상단에 고정시키며(sticky) 다른 영역보다 우선하여 볼 수 있도록 작성하세요. */
  position: fixed;
  top: 0;
  z-index: 1000; /* 가장 앞으로 고정 */
  background: white;
  color: #f1f1f1;
}
```

```css
/* nav */
nav {
  /* navigation 항목을 오른쪽으로 정렬 시키세요.*/
  float: right;
}
```


```css
.nav-items > li {
  /* navigation 항목을 한 줄로 만들어 주세요. */
  display: inline-block;

  /* 좌우 여백을 지정하세요. */
  margin: 0 5px;

  /* li 태그의 bullet point를 제거 해주세요. */
  list-style: none;
}
```

```css
.nav-items > li > a {
  /* a tag는 링크를 나타내며, 기본적으로 글자 색상이 파란색입니다. 원하는 색상으로 바꿔보세요. */
  color: #333;
}
```


```css
.nav-items > li > a:hover {
  /* hover는 마우스 오버시 모습입니다. 
  이때 하이라이트 되도록 다른 색상으로 바꿔보세요. */
  color: violet;

  /* a tag를 마우스 오버하면 밑줄이 나타납니다.
  text를 꾸며주고 있는 밑줄을 없애보세요. */
  text-decoration: none;
}
```


```css
/* title section */
#section-title {
  /* 배경 이미지를 적용 해보세요. (이미지는 images/background.jpg) */
  background-image: url(images/background.jpg);
  background-size: cover;
  background-position: center;
  /* 텍스트를 가운데 정렬 해보세요. */
  text-align: center; 
  /* 텍스트를 수직 가운데 정렬 해보세요. (section-title은 높이가 300px) */
  line-height: 300px;
}
```

```css
.section-title-heading {
  /* font size를 적절하게 조정 해주세요. (h1 기본 2rem) */
  font-size: 2.5rem;
}
```

```css
/* aside */
aside {
  /* aside를 부모인 div#content의 영역에 위치시키세요.
  div#content는 position: relative 입니다.
  */
  position: absolute;

  /* bottom: 0; */
  top: 0;
}
```

```css
.aside-items {
  /* ul 태그의 자동으로 적용된 padding을 제거 해주세요. */
  padding: 0;
}
```

```css
.aside-items > li {
  /* li 태그의 bullet point를 제거 해주세요. */
  text-decoration: none;
}
```


```css

/* footer */
footer {
  /* footer는 항상 바닥에 위치하도록 position을 설정 해주세요. */
  position: fixed;
  bottom: 0;
  /* 텍스트를 가운데 정렬 해주세요. */
  text-align: center; 
  /* 텍스트가 수직정렬 되도록 해주세요. (footer는 높이가 50px) */
  line-height: 50px;
}
```



![1564710231590](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1564710231590.png)