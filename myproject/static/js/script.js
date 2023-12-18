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

// Set up a repeating interval that runs every 2000 milliseconds (2 seconds)
setInterval(() => {
    // Check if the current URL has changed since the last check
    if (location.href !== lastURL) {
        // Update the lastURL variable with the current URL
        lastURL = location.href;
        
        // Check if the initFlowbite function exists
        if (typeof initFlowbite === 'function') {
            // If it does, call the initFlowbite function
            initFlowbite();
        }
    }
}, 2000); // 每n毫秒检查一次 (Check every n milliseconds)

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

function scrollToSection(id) {
    const yOffset = -150; // 固定元素的高度
    const element = document.getElementById(id);
    const y = element.getBoundingClientRect().top + window.scrollY + yOffset;
  
    window.scrollTo({top: y, behavior: 'smooth'}); // or 'smooth'

    // 更新 URL 以包含锚点
    // history.pushState(null, null, '#' + id);
  }




