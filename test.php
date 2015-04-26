<?php
/* PHP SDK v4.0.0 */
/* make the API call */
	require_once 'facebook-php-sdk-v4-4.0-dev/autoload.php';
	require_once 'facebook-php-sdk-v4-4.0-dev/src/Facebook/FacebookSession.php';
	use Facebook\FacebookSession;
	use Facebook\FacebookRequest;
	use Facebook\GraphUser;
	use Facebook\FacebookRequestException;
	use Facebook\FacebookRedirectLoginHelper;
 
	$api_key = '1629352680618181';
	$api_secret = 'a0d6d4f6a09d174387ae47e5e1a0aa7c';
	FacebookSession::setDefaultApplication($api_key,$api_secret);
	$session = FacebookSession::newAppSession();
	if ( isset( $session ) )
		echo "yes"
?>