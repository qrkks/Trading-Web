document.addEventListener('htmx:afterRequest', function (event) {
    var targetUrl = event.detail.target;
    var scrollToTop = event.target.getAttribute('data-scroll-to-top');
 
    // 检查是否有包含 data-scroll-to-top="true" 属性的元素触发了请求
    if (scrollToTop === 'true') {
        window.scrollTo(0, 0); // 滚动到顶部
    }
});


document.addEventListener('DOMContentLoaded', function () {
    var progressBar = document.getElementById('progress-bar');
    var progressContainer = document.getElementById('progress-container');

    // 监听页面开始加载事件
    document.addEventListener('htmx:send', function () {
        // 显示进度条
        progressContainer.style.display = 'block';
        progressBar.style.width = '0';
        // console.log('htmx:send event listener registered');

    });

    // 监听页面加载完成事件
    document.addEventListener('htmx:afterRequest', function () {
        // 隐藏进度条
        progressContainer.style.display = 'none';
        progressBar.style.width = '0';
        // console.log('htmx:afterRequest event listener registered');

    });

    // 监听页面加载进度事件
    document.addEventListener('htmx:requestProgress', function (event) {
        // 更新进度条的宽度
        progressBar.style.width = event.detail.percent + '%';
        // console.log('htmx:requestProgress event listener registered');

    });
});

// document.addEventListener('htmx:send', function () {
//     // 关闭移动端导航菜单
//     var mobileNav = document.getElementById('mobile-nav');
//     mobileNav.style.display = 'none'; // 或者适当的关闭操作
// });
