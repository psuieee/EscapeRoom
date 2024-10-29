(self["webpackChunkhgregeg"] = self["webpackChunkhgregeg"] || []).push([["js/Page/MainSiteJs"],{

/***/ "./apps/Blog/CryptoNews/assets/Webpack/Page/Main/MainSiteJs.js":
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony import */ var _js_Page_Menu_site_menu_js__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__("./apps/Blog/CryptoNews/assets/js/Page/Menu/site_menu.js");
/* harmony import */ var _js_Page_Menu_site_menu_js__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_js_Page_Menu_site_menu_js__WEBPACK_IMPORTED_MODULE_0__);


/***/ }),

/***/ "./apps/Blog/CryptoNews/assets/js/Page/Menu/site_menu.js":
/***/ (() => {

document.addEventListener('DOMContentLoaded', function () {
  var $menuMobileTrigger = $('.js_menu_mobile_trigger');
  var $menuNav = $('.js_menu_nav');
  var isMobileMenuVisible = function isMobileMenuVisible() {
    return $menuMobileTrigger.is(':visible');
  };
  var isMobileMenuOpened = function isMobileMenuOpened() {
    return $menuMobileTrigger.hasClass('active');
  };
  $menuMobileTrigger.on('click', function () {
    $menuMobileTrigger.toggleClass('active');
    $menuNav.slideToggle(200);
  });
  window.addEventListener('resize', function (event) {
    if (isMobileMenuVisible()) {
      if (!isMobileMenuOpened()) {
        $menuNav.hide();
      }
    } else {
      if ($menuNav.is(':hidden')) {
        $menuNav.show();
      }
    }
  });
  $('.js_menu_static_item').on('click', function () {
    if (isMobileMenuVisible() && isMobileMenuOpened()) {
      $menuMobileTrigger.click(); // hide menu
    }
  });
});

/***/ })

},
/******/ __webpack_require__ => { // webpackRuntimeModules
/******/ var __webpack_exec__ = (moduleId) => (__webpack_require__(__webpack_require__.s = moduleId))
/******/ var __webpack_exports__ = (__webpack_exec__("./apps/Blog/CryptoNews/assets/Webpack/Page/Main/MainSiteJs.js"));
/******/ }
]);