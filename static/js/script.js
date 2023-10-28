document.addEventListener('htmx:afterRequest', function (event) {
    var targetUrl = event.detail.target;
    var scrollToTop = event.target.getAttribute('data-scroll-to-top');
 
    // 检查是否有包含 data-scroll-to-top="true" 属性的元素触发了请求
    if (scrollToTop === 'true') {
        window.scrollTo(0, 0); // 滚动到顶部
    }
});
