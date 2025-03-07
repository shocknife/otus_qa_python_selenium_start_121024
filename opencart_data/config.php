<?php
// APPLICATION
define('APPLICATION', 'Catalog');

// HTTP
define('HTTP_SERVER', 'http://192.168.1.242:8082/');

// DIR
define('DIR_OPENCART', '/opt/bitnami/opencart/');
define('DIR_APPLICATION', DIR_OPENCART . 'catalog/');
define('DIR_SYSTEM', DIR_OPENCART . 'system/');
define('DIR_EXTENSION', DIR_OPENCART . 'extension/');
define('DIR_IMAGE', DIR_OPENCART . 'image/');
define('DIR_STORAGE', DIR_SYSTEM . 'storage/');
define('DIR_LANGUAGE', DIR_APPLICATION . 'language/');
define('DIR_TEMPLATE', DIR_APPLICATION . 'view/template/');
define('DIR_CONFIG', DIR_SYSTEM . 'config/');
define('DIR_CACHE', DIR_STORAGE . 'cache/');
define('DIR_DOWNLOAD', DIR_STORAGE . 'download/');
define('DIR_LOGS', DIR_STORAGE . 'logs/');
define('DIR_SESSION', DIR_STORAGE . 'session/');
define('DIR_UPLOAD', DIR_STORAGE . 'upload/');

// DB
define('DB_DRIVER', 'mysqli');
define('DB_HOSTNAME', 'mariadb');
define('DB_USERNAME', 'bn_opencart');
define('DB_PASSWORD', '');
define('DB_DATABASE', 'bitnami_opencart');
define('DB_PREFIX', 'oc_');
define('DB_PORT', '3306');
define('HTTPS_SERVER', 'http://192.168.1.242:8082/');
