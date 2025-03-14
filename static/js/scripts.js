import PhotoSwipeLightbox from "../js/PhotoSwipe-5.4.4/photoswipe-lightbox.esm.min.js"
// import '../js/PhotoSwipe-5.4.4/photoswipe.css'

const lightbox = new PhotoSwipeLightbox({
    gallery: ".gallery--responsive-images",
    // gallery: "#gallery--individual",
    children: "a",
    pswpModule: () => import("../js/PhotoSwipe-5.4.4/photoswipe.esm.min.js")
})

lightbox.init()