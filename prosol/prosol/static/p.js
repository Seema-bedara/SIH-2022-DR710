(function() {
    const CONTAINER = document.querySelector('.container')
    const VMIN = Math.min(window.innerHeight, window.innerWidth) / 100
    CONTAINER.style.setProperty('--width', 425 / VMIN)
    CONTAINER.style.setProperty('--height', 225 / VMIN)
  })()