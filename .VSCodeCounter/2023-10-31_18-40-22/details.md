# Details

Date : 2023-10-31 18:40:22

Directory c:\\Website\\Real site\\Trading Web

Total : 177 files,  8029 codes, 634 comments, 942 blanks, all 9605 lines

[Summary](results.md) / Details / [Diff Summary](diff.md) / [Diff Details](diff-details.md)

## Files
| filename | language | code | comment | blank | total |
| :--- | :--- | ---: | ---: | ---: | ---: |
| [abstractapp/__init__.py](/abstractapp/__init__.py) | Python | 0 | 0 | 1 | 1 |
| [abstractapp/admin.py](/abstractapp/admin.py) | Python | 14 | 1 | 5 | 20 |
| [abstractapp/custom_context_processors.py](/abstractapp/custom_context_processors.py) | Python | 33 | 5 | 13 | 51 |
| [abstractapp/manager.py](/abstractapp/manager.py) | Python | 6 | 0 | 3 | 9 |
| [abstractapp/middlewares.py](/abstractapp/middlewares.py) | Python | 19 | 28 | 18 | 65 |
| [abstractapp/models.py](/abstractapp/models.py) | Python | 41 | 5 | 16 | 62 |
| [blog/__init__.py](/blog/__init__.py) | Python | 0 | 0 | 1 | 1 |
| [blog/admin.py](/blog/admin.py) | Python | 21 | 2 | 5 | 28 |
| [blog/apps.py](/blog/apps.py) | Python | 4 | 0 | 3 | 7 |
| [blog/migrations/0001_initial.py](/blog/migrations/0001_initial.py) | Python | 89 | 1 | 6 | 96 |
| [blog/migrations/0002_remove_blog_content.py](/blog/migrations/0002_remove_blog_content.py) | Python | 11 | 1 | 5 | 17 |
| [blog/migrations/0003_blog_content.py](/blog/migrations/0003_blog_content.py) | Python | 15 | 1 | 5 | 21 |
| [blog/migrations/0004_blog_category_blog_created_at_blog_custom_order_and_more.py](/blog/migrations/0004_blog_category_blog_created_at_blog_custom_order_and_more.py) | Python | 34 | 1 | 5 | 40 |
| [blog/migrations/0005_alter_blog_options_blog_is_active_blog_is_featured.py](/blog/migrations/0005_alter_blog_options_blog_is_active_blog_is_featured.py) | Python | 21 | 1 | 5 | 27 |
| [blog/migrations/0006_alter_blog_options.py](/blog/migrations/0006_alter_blog_options.py) | Python | 11 | 1 | 5 | 17 |
| [blog/migrations/__init__.py](/blog/migrations/__init__.py) | Python | 0 | 0 | 1 | 1 |
| [blog/models.py](/blog/models.py) | Python | 71 | 5 | 23 | 99 |
| [blog/templates/blog/blog-index.html](/blog/templates/blog/blog-index.html) | HTML | 10 | 0 | 1 | 11 |
| [blog/templates/blog/blog.html](/blog/templates/blog/blog.html) | HTML | 11 | 0 | 2 | 13 |
| [blog/templates/blog/obsolete/blog-detail.html](/blog/templates/blog/obsolete/blog-detail.html) | HTML | 24 | 0 | 1 | 25 |
| [blog/templates/blog/obsolete/blog-list.html](/blog/templates/blog/obsolete/blog-list.html) | HTML | 16 | 0 | 1 | 17 |
| [blog/templates/blog/partial/card-blog.html](/blog/templates/blog/partial/card-blog.html) | HTML | 28 | 0 | 1 | 29 |
| [blog/templates/blog/partial/card-horizontal.html](/blog/templates/blog/partial/card-horizontal.html) | HTML | 49 | 0 | 1 | 50 |
| [blog/templates/blog/partial/main-detail.html](/blog/templates/blog/partial/main-detail.html) | HTML | 30 | 0 | 1 | 31 |
| [blog/templates/blog/partial/main-list.html](/blog/templates/blog/partial/main-list.html) | HTML | 6 | 0 | 1 | 7 |
| [blog/tests.py](/blog/tests.py) | Python | 1 | 1 | 2 | 4 |
| [blog/urls.py](/blog/urls.py) | Python | 7 | 1 | 2 | 10 |
| [blog/views.py](/blog/views.py) | Python | 73 | 24 | 28 | 125 |
| [db.sqlite3](/db.sqlite3) | Database | 1,420 | 0 | 36 | 1,456 |
| [form_handlers/__init__.py](/form_handlers/__init__.py) | Python | 0 | 0 | 1 | 1 |
| [form_handlers/admin.py](/form_handlers/admin.py) | Python | 12 | 3 | 4 | 19 |
| [form_handlers/apps.py](/form_handlers/apps.py) | Python | 7 | 0 | 3 | 10 |
| [form_handlers/forms.py](/form_handlers/forms.py) | Python | 6 | 0 | 2 | 8 |
| [form_handlers/migrations/0001_initial.py](/form_handlers/migrations/0001_initial.py) | Python | 31 | 1 | 6 | 38 |
| [form_handlers/migrations/0002_alter_inquiry_options_alter_inquiry_city_and_more.py](/form_handlers/migrations/0002_alter_inquiry_options_alter_inquiry_city_and_more.py) | Python | 36 | 1 | 5 | 42 |
| [form_handlers/migrations/0003_notificationinbox.py](/form_handlers/migrations/0003_notificationinbox.py) | Python | 25 | 1 | 5 | 31 |
| [form_handlers/migrations/0004_notificationinbox_created_at_and_more.py](/form_handlers/migrations/0004_notificationinbox_created_at_and_more.py) | Python | 17 | 1 | 5 | 23 |
| [form_handlers/migrations/0005_remove_notificationinbox_notification_inbox_and_more.py](/form_handlers/migrations/0005_remove_notificationinbox_notification_inbox_and_more.py) | Python | 17 | 1 | 5 | 23 |
| [form_handlers/migrations/0006_inquiry_created_at_inquiry_updated_at.py](/form_handlers/migrations/0006_inquiry_created_at_inquiry_updated_at.py) | Python | 17 | 1 | 5 | 23 |
| [form_handlers/migrations/0007_inquiry_custom_order_inquiry_is_active_and_more.py](/form_handlers/migrations/0007_inquiry_custom_order_inquiry_is_active_and_more.py) | Python | 37 | 1 | 5 | 43 |
| [form_handlers/migrations/0008_remove_inquiry_custom_order_remove_inquiry_is_active_and_more.py](/form_handlers/migrations/0008_remove_inquiry_custom_order_remove_inquiry_is_active_and_more.py) | Python | 19 | 1 | 5 | 25 |
| [form_handlers/migrations/__init__.py](/form_handlers/migrations/__init__.py) | Python | 0 | 0 | 1 | 1 |
| [form_handlers/models.py](/form_handlers/models.py) | Python | 26 | 3 | 9 | 38 |
| [form_handlers/signals.py](/form_handlers/signals.py) | Python | 20 | 17 | 8 | 45 |
| [form_handlers/templates/form_handlers/deprecated/inquiry_create.html](/form_handlers/templates/form_handlers/deprecated/inquiry_create.html) | HTML | 103 | 0 | 8 | 111 |
| [form_handlers/templates/form_handlers/indicator-submitted.html](/form_handlers/templates/form_handlers/indicator-submitted.html) | HTML | 18 | 0 | 1 | 19 |
| [form_handlers/templates/form_handlers/inquiry.html](/form_handlers/templates/form_handlers/inquiry.html) | HTML | 104 | 3 | 2 | 109 |
| [form_handlers/tests.py](/form_handlers/tests.py) | Python | 1 | 1 | 2 | 4 |
| [form_handlers/urls.py](/form_handlers/urls.py) | Python | 5 | 0 | 2 | 7 |
| [form_handlers/views.py](/form_handlers/views.py) | Python | 33 | 3 | 12 | 48 |
| [manage.py](/manage.py) | Python | 15 | 3 | 5 | 23 |
| [mysite/__init__.py](/mysite/__init__.py) | Python | 0 | 0 | 1 | 1 |
| [mysite/asgi.py](/mysite/asgi.py) | Python | 4 | 8 | 5 | 17 |
| [mysite/settings.py](/mysite/settings.py) | Python | 111 | 56 | 54 | 221 |
| [mysite/urls.py](/mysite/urls.py) | Python | 18 | 20 | 7 | 45 |
| [mysite/wsgi.py](/mysite/wsgi.py) | Python | 4 | 8 | 5 | 17 |
| [news/__init__.py](/news/__init__.py) | Python | 0 | 0 | 1 | 1 |
| [news/admin.py](/news/admin.py) | Python | 1 | 1 | 2 | 4 |
| [news/apps.py](/news/apps.py) | Python | 4 | 0 | 3 | 7 |
| [news/migrations/__init__.py](/news/migrations/__init__.py) | Python | 0 | 0 | 1 | 1 |
| [news/models.py](/news/models.py) | Python | 1 | 1 | 2 | 4 |
| [news/tests.py](/news/tests.py) | Python | 1 | 1 | 2 | 4 |
| [news/views.py](/news/views.py) | Python | 1 | 1 | 2 | 4 |
| [pages/__init__.py](/pages/__init__.py) | Python | 0 | 0 | 1 | 1 |
| [pages/admin.py](/pages/admin.py) | Python | 48 | 9 | 19 | 76 |
| [pages/apps.py](/pages/apps.py) | Python | 4 | 0 | 3 | 7 |
| [pages/migrations/0001_initial.py](/pages/migrations/0001_initial.py) | Python | 21 | 1 | 6 | 28 |
| [pages/migrations/0002_delete_recipe.py](/pages/migrations/0002_delete_recipe.py) | Python | 10 | 1 | 5 | 16 |
| [pages/migrations/0003_initial.py](/pages/migrations/0003_initial.py) | Python | 31 | 1 | 6 | 38 |
| [pages/migrations/0004_homecarouselimage_header_homecarouselimage_paragraph.py](/pages/migrations/0004_homecarouselimage_header_homecarouselimage_paragraph.py) | Python | 17 | 1 | 5 | 23 |
| [pages/migrations/0005_homecarouselimage_learn_more.py](/pages/migrations/0005_homecarouselimage_learn_more.py) | Python | 12 | 1 | 5 | 18 |
| [pages/migrations/0006_alter_homecarouselimage_learn_more.py](/pages/migrations/0006_alter_homecarouselimage_learn_more.py) | Python | 12 | 1 | 5 | 18 |
| [pages/migrations/0007_contactinformation_socialmedia.py](/pages/migrations/0007_contactinformation_socialmedia.py) | Python | 61 | 1 | 5 | 67 |
| [pages/migrations/0008_rename_detail_socialmedia_link.py](/pages/migrations/0008_rename_detail_socialmedia_link.py) | Python | 12 | 1 | 5 | 18 |
| [pages/migrations/0009_rename_detail_contactinformation_info_and_more.py](/pages/migrations/0009_rename_detail_contactinformation_info_and_more.py) | Python | 22 | 1 | 5 | 28 |
| [pages/migrations/0010_faq.py](/pages/migrations/0010_faq.py) | Python | 31 | 1 | 5 | 37 |
| [pages/migrations/0011_contactinformation_link.py](/pages/migrations/0011_contactinformation_link.py) | Python | 12 | 1 | 5 | 18 |
| [pages/migrations/0012_contactinformation_link_template.py](/pages/migrations/0012_contactinformation_link_template.py) | Python | 17 | 1 | 5 | 23 |
| [pages/migrations/0013_alter_contactinformation_link.py](/pages/migrations/0013_alter_contactinformation_link.py) | Python | 14 | 1 | 5 | 20 |
| [pages/migrations/0014_cta_alter_homecarouselimage_image.py](/pages/migrations/0014_cta_alter_homecarouselimage_image.py) | Python | 42 | 1 | 5 | 48 |
| [pages/migrations/0015_home_delete_cta.py](/pages/migrations/0015_home_delete_cta.py) | Python | 38 | 1 | 5 | 44 |
| [pages/migrations/0016_banner_delete_home.py](/pages/migrations/0016_banner_delete_home.py) | Python | 38 | 1 | 5 | 44 |
| [pages/migrations/__init__.py](/pages/migrations/__init__.py) | Python | 0 | 0 | 1 | 1 |
| [pages/models.py](/pages/models.py) | Python | 28 | 2 | 12 | 42 |
| [pages/templates/pages/about.html](/pages/templates/pages/about.html) | HTML | 192 | 0 | 1 | 193 |
| [pages/templates/pages/contact.html](/pages/templates/pages/contact.html) | HTML | 33 | 0 | 2 | 35 |
| [pages/templates/pages/index.html](/pages/templates/pages/index.html) | HTML | 57 | 0 | 1 | 58 |
| [pages/templates/pages/partial/banner.html](/pages/templates/pages/partial/banner.html) | HTML | 42 | 5 | 1 | 48 |
| [pages/templates/pages/partial/carousel-hero.html](/pages/templates/pages/partial/carousel-hero.html) | HTML | 59 | 3 | 1 | 63 |
| [pages/templates/pages/partial/faq.html](/pages/templates/pages/partial/faq.html) | HTML | 34 | 2 | 4 | 40 |
| [pages/templates/pages/partial/section.html](/pages/templates/pages/partial/section.html) | HTML | 188 | 0 | 26 | 214 |
| [pages/tests.py](/pages/tests.py) | Python | 1 | 1 | 2 | 4 |
| [pages/urls.py](/pages/urls.py) | Python | 7 | 1 | 4 | 12 |
| [pages/views.py](/pages/views.py) | Python | 43 | 3 | 15 | 61 |
| [products/__init__.py](/products/__init__.py) | Python | 0 | 0 | 1 | 1 |
| [products/admin.py](/products/admin.py) | Python | 59 | 19 | 24 | 102 |
| [products/apps.py](/products/apps.py) | Python | 4 | 0 | 3 | 7 |
| [products/migrations/0001_initial.py](/products/migrations/0001_initial.py) | Python | 174 | 1 | 6 | 181 |
| [products/migrations/0002_remove_product_view_count.py](/products/migrations/0002_remove_product_view_count.py) | Python | 11 | 1 | 5 | 17 |
| [products/migrations/0003_product_view_count.py](/products/migrations/0003_product_view_count.py) | Python | 19 | 1 | 5 | 25 |
| [products/migrations/0004_alter_product_tags_alter_product_view_count.py](/products/migrations/0004_alter_product_tags_alter_product_view_count.py) | Python | 32 | 1 | 5 | 38 |
| [products/migrations/0005_alter_product_description_alter_product_name.py](/products/migrations/0005_alter_product_description_alter_product_name.py) | Python | 17 | 1 | 5 | 23 |
| [products/migrations/__init__.py](/products/migrations/__init__.py) | Python | 0 | 0 | 1 | 1 |
| [products/models.py](/products/models.py) | Python | 104 | 41 | 37 | 182 |
| [products/templates/deprecated/product-detail.html](/products/templates/deprecated/product-detail.html) | HTML | 12 | 2 | 4 | 18 |
| [products/templates/deprecated/product-index.html](/products/templates/deprecated/product-index.html) | HTML | 25 | 2 | 1 | 28 |
| [products/templates/deprecated/product-list.html](/products/templates/deprecated/product-list.html) | HTML | 12 | 5 | 2 | 19 |
| [products/templates/products/partial/card-product.html](/products/templates/products/partial/card-product.html) | HTML | 33 | 0 | 1 | 34 |
| [products/templates/products/partial/carousel-product.html](/products/templates/products/partial/carousel-product.html) | HTML | 55 | 4 | 2 | 61 |
| [products/templates/products/partial/deprecated/card-product copy.html](/products/templates/products/partial/deprecated/card-product%20copy.html) | HTML | 155 | 98 | 34 | 287 |
| [products/templates/products/partial/deprecated/detail-main.html](/products/templates/products/partial/deprecated/detail-main.html) | HTML | 17 | 0 | 1 | 18 |
| [products/templates/products/partial/deprecated/list-main.html](/products/templates/products/partial/deprecated/list-main.html) | HTML | 25 | 0 | 3 | 28 |
| [products/templates/products/partial/deprecated/main-index.html](/products/templates/products/partial/deprecated/main-index.html) | HTML | 16 | 0 | 2 | 18 |
| [products/templates/products/partial/featured-section.html](/products/templates/products/partial/featured-section.html) | HTML | 66 | 0 | 1 | 67 |
| [products/templates/products/partial/main-detail.html](/products/templates/products/partial/main-detail.html) | HTML | 53 | 0 | 1 | 54 |
| [products/templates/products/partial/main-list.html](/products/templates/products/partial/main-list.html) | HTML | 10 | 0 | 1 | 11 |
| [products/templates/products/product-index.html](/products/templates/products/product-index.html) | HTML | 13 | 0 | 1 | 14 |
| [products/templates/products/product.html](/products/templates/products/product.html) | HTML | 14 | 0 | 1 | 15 |
| [products/tests.py](/products/tests.py) | Python | 1 | 1 | 2 | 4 |
| [products/urls.py](/products/urls.py) | Python | 7 | 3 | 3 | 13 |
| [products/views.py](/products/views.py) | Python | 101 | 54 | 55 | 210 |
| [search/__init__.py](/search/__init__.py) | Python | 0 | 0 | 1 | 1 |
| [search/admin.py](/search/admin.py) | Python | 1 | 1 | 2 | 4 |
| [search/apps.py](/search/apps.py) | Python | 4 | 0 | 3 | 7 |
| [search/migrations/__init__.py](/search/migrations/__init__.py) | Python | 0 | 0 | 1 | 1 |
| [search/models.py](/search/models.py) | Python | 1 | 1 | 2 | 4 |
| [search/templates/search/partial/deprecated/search-results.html](/search/templates/search/partial/deprecated/search-results.html) | HTML | 13 | 0 | 1 | 14 |
| [search/templates/search/partial/deprecated/searchbar-header copy.html](/search/templates/search/partial/deprecated/searchbar-header%20copy.html) | HTML | 43 | 0 | 12 | 55 |
| [search/templates/search/partial/search-results.html](/search/templates/search/partial/search-results.html) | HTML | 47 | 0 | 1 | 48 |
| [search/templates/search/partial/searchbar-header.html](/search/templates/search/partial/searchbar-header.html) | HTML | 59 | 0 | 7 | 66 |
| [search/templates/search/partial/searchbar-product.html](/search/templates/search/partial/searchbar-product.html) | HTML | 43 | 0 | 1 | 44 |
| [search/templates/search/svg/search.svg](/search/templates/search/svg/search.svg) | XML | 9 | 0 | 0 | 9 |
| [search/tests.py](/search/tests.py) | Python | 1 | 1 | 2 | 4 |
| [search/urls.py](/search/urls.py) | Python | 7 | 0 | 3 | 10 |
| [search/views.py](/search/views.py) | Python | 106 | 38 | 33 | 177 |
| [static/css/style.css](/static/css/style.css) | CSS | 31 | 2 | 3 | 36 |
| [static/js/alpine/2.8.2/alpine.min.js](/static/js/alpine/2.8.2/alpine.min.js) | JavaScript | 1 | 7 | 0 | 8 |
| [static/js/flowbite/1.8.1/flowbite.min.js](/static/js/flowbite/1.8.1/flowbite.min.js) | JavaScript | 1 | 0 | 0 | 1 |
| [static/js/htmx/1.9.6/htmx.min.js](/static/js/htmx/1.9.6/htmx.min.js) | JavaScript | 1 | 0 | 0 | 1 |
| [static/js/hyperscript/0.9.12/hyperscript.min.js](/static/js/hyperscript/0.9.12/hyperscript.min.js) | JavaScript | 1 | 0 | 0 | 1 |
| [static/js/script.js](/static/js/script.js) | JavaScript | 21 | 27 | 16 | 64 |
| [templates/base.html](/templates/base.html) | HTML | 75 | 4 | 1 | 80 |
| [templates/partial/button-contact.html](/templates/partial/button-contact.html) | HTML | 107 | 0 | 1 | 108 |
| [templates/partial/faq.html](/templates/partial/faq.html) | HTML | 23 | 0 | 0 | 23 |
| [templates/partial/footer.html](/templates/partial/footer.html) | HTML | 223 | 0 | 30 | 253 |
| [templates/partial/nav-list.html](/templates/partial/nav-list.html) | HTML | 183 | 0 | 1 | 184 |
| [templates/partial/obsolete/button-contact copy.html](/templates/partial/obsolete/button-contact%20copy.html) | HTML | 48 | 0 | 7 | 55 |
| [templates/partial/obsolete/nav-list.html](/templates/partial/obsolete/nav-list.html) | HTML | 34 | 4 | 1 | 39 |
| [templates/partial/pagination.html](/templates/partial/pagination.html) | HTML | 81 | 5 | 1 | 87 |
| [templates/partial/sidebar.html](/templates/partial/sidebar.html) | HTML | 72 | 1 | 1 | 74 |
| [templates/snippet/breadcrumbs.html](/templates/snippet/breadcrumbs.html) | HTML | 31 | 0 | 1 | 32 |
| [templates/snippet/deprecated/breadcrumbs.html](/templates/snippet/deprecated/breadcrumbs.html) | HTML | 24 | 0 | 0 | 24 |
| [templates/snippet/learn-more.html](/templates/snippet/learn-more.html) | HTML | 3 | 0 | 0 | 3 |
| [templates/snippet/page-title.html](/templates/snippet/page-title.html) | HTML | 7 | 0 | 0 | 7 |
| [templates/snippet/pagination-prev-next.html](/templates/snippet/pagination-prev-next.html) | HTML | 47 | 0 | 1 | 48 |
| [templates/svg/contact/email.svg](/templates/svg/contact/email.svg) | XML | 7 | 0 | 0 | 7 |
| [templates/svg/contact/phone.svg](/templates/svg/contact/phone.svg) | XML | 7 | 0 | 0 | 7 |
| [templates/svg/contact/qq.svg](/templates/svg/contact/qq.svg) | XML | 1 | 0 | 0 | 1 |
| [templates/svg/contact/wechat.svg](/templates/svg/contact/wechat.svg) | XML | 1 | 0 | 0 | 1 |
| [templates/svg/contact/whatsapp.svg](/templates/svg/contact/whatsapp.svg) | XML | 1 | 0 | 0 | 1 |
| [theme/__init__.py](/theme/__init__.py) | Python | 0 | 0 | 1 | 1 |
| [theme/apps.py](/theme/apps.py) | Python | 3 | 0 | 3 | 6 |
| [theme/static/css/dist/styles.css](/theme/static/css/dist/styles.css) | CSS | 2 | 0 | 1 | 3 |
| [theme/static_src/package-lock.json](/theme/static_src/package-lock.json) | JSON | 1,613 | 0 | 1 | 1,614 |
| [theme/static_src/package.json](/theme/static_src/package.json) | JSON | 29 | 0 | 1 | 30 |
| [theme/static_src/postcss.config.js](/theme/static_src/postcss.config.js) | JavaScript | 7 | 0 | 1 | 8 |
| [theme/static_src/src/styles.css](/theme/static_src/src/styles.css) | CSS | 19 | 4 | 8 | 31 |
| [theme/static_src/tailwind.config.js](/theme/static_src/tailwind.config.js) | JavaScript | 22 | 43 | 7 | 72 |
| [theme/templates/base.html](/theme/templates/base.html) | HTML | 18 | 0 | 2 | 20 |
| [utils/__init__.py](/utils/__init__.py) | Python | 0 | 0 | 1 | 1 |
| [utils/admin.py](/utils/admin.py) | Python | 1 | 1 | 2 | 4 |
| [utils/apps.py](/utils/apps.py) | Python | 4 | 0 | 3 | 7 |
| [utils/migrations/0001_initial.py](/utils/migrations/0001_initial.py) | Python | 21 | 1 | 6 | 28 |
| [utils/migrations/__init__.py](/utils/migrations/__init__.py) | Python | 0 | 0 | 1 | 1 |
| [utils/models.py](/utils/models.py) | Python | 3 | 1 | 2 | 6 |
| [utils/tests.py](/utils/tests.py) | Python | 1 | 1 | 2 | 4 |
| [utils/views.py](/utils/views.py) | Python | 1 | 1 | 2 | 4 |

[Summary](results.md) / Details / [Diff Summary](diff.md) / [Diff Details](diff-details.md)