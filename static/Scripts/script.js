console.log("Hello")

const togglesDown = [...document.getElementsByClassName("toggle-down")]
const togglesUp = [...document.getElementsByClassName("toggle-up")]
// carousel
const productContainer = [...document.getElementsByClassName("slider")]
const nxtBtn = [...document.querySelectorAll('.nextBtn')];
const preBtn = [...document.querySelectorAll('.prevBtn')];

togglesDown.forEach(toggle => { 
    toggle.addEventListener('click', () => {
        toggle.parentElement.getElementsByTagName('p')[0].classList.toggle('hidden')
        toggle.classList.toggle('hidden')
        toggle.parentElement.getElementsByClassName('toggle-up')[0].classList.toggle('hidden')
    })
})

togglesUp.forEach(toggle => { 
    toggle.addEventListener('click', () => {
        toggle.parentElement.getElementsByTagName('p')[0].classList.toggle('hidden')
        toggle.classList.toggle('hidden')
        toggle.parentElement.getElementsByClassName('toggle-down')[0].classList.toggle('hidden')
    })
})



productContainer.forEach((item, i) => {
    let containerDimensions = item.getBoundingClientRect();
    let containerWidth = containerDimensions.width;

    nxtBtn[i].addEventListener('click', () => {
        item.scrollLeft += containerWidth;
    })

    preBtn[i].addEventListener('click', () => {
        item.scrollLeft -= containerWidth;
    })
})