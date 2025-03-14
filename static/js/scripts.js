import PhotoSwipeLightbox from "../js/PhotoSwipe-5.4.4/photoswipe-lightbox.esm.min.js"

const lightbox = new PhotoSwipeLightbox({
    gallery: ".gallery--responsive-images",
    children: "a",
    pswpModule: () => import("../js/PhotoSwipe-5.4.4/photoswipe.esm.min.js"),
    bgOpacity: 0.2,
    spacing: 0.5,
    allowPanToNext: true,
})

lightbox.init()