let shouldScrollToTop = false;

document.addEventListener('htmx:beforeRequest', function (event) {
    let triggeringElement = event.detail.elt;
    let scrollToTop = triggeringElement.getAttribute('data-scroll-to-top');
    shouldScrollToTop = (scrollToTop === 'true');
});

document.addEventListener('htmx:afterRequest', function (event) {
    if (shouldScrollToTop) {
        window.scrollTo(0, 0); // 滚动到顶部
    }
    shouldScrollToTop = false; // Reset the flag
});


// window.addEventListener('pageshow', function(event) {
//     if (event.persisted) {
//         Alpine.discoverUninitializedComponents(function(el) {
//             Alpine.initializeComponent(el);
//         });
//     }
// });

