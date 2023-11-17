// htmx返回页面回到页首 //

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

// url变化后重新初始化initFlowbite //

let lastURL = location.href;

setInterval(() => {
    if (location.href !== lastURL) {
        lastURL = location.href;
        if (typeof initFlowbite === 'function') {
            initFlowbite();
        }
    }
}, 2000); // 每n毫秒检查一次

// // 监听URL变化的函数
// function observeURLChange(callback) {
//     const observer = new MutationObserver((mutations) => {
//         for (const mutation of mutations) {
//             if (mutation.type === 'childList' && mutation.addedNodes.length) {
//                 for (const addedNode of mutation.addedNodes) {
//                     if (addedNode.tagName === 'A' && addedNode.href !== location.href) {
//                         callback();
//                         return;
//                     }
//                 }
//             }
//         }
//     });

//     observer.observe(document.body, {
//         childList: true,
//         subtree: true,
//     });
// }

// // 使用上面定义的函数，监听URL变化
// observeURLChange(() => {
//     if (typeof initFlowbite === 'function') {
//         initFlowbite();
//     }
// });






